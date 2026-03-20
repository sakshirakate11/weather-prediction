from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
from fetch_weather import get_weather_data, get_features_for_ml
from datetime import datetime
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


supabase_url = os.getenv('VITE_SUPABASE_URL')
supabase_key = os.getenv('VITE_SUPABASE_ANON_KEY')
supabase = None
# supabase: Client = create_client(supabase_url, supabase_key)  # Optional DB

with open('rain_model.pkl', 'rb') as f:
    rain_model = pickle.load(f)

with open('temp_model.pkl', 'rb') as f:
    temp_model = pickle.load(f)

TRANSLATIONS = {
    'en': {
        'title': 'Real-Time Weather Prediction',
        'subtitle': 'Live Weather Data + ML Predictions',
        'city_label': 'Enter City Name',
        'city_placeholder': 'e.g., Mumbai, London, New York',
        'predict_btn': 'Predict Weather',
        'current_weather': 'Current Weather',
        'temperature': 'Temperature',
        'feels_like': 'Feels Like',
        'humidity': 'Humidity',
        'pressure': 'Pressure',
        'wind_speed': 'Wind Speed',
        'ml_predictions': 'ML Predictions',
        'predicted_temp': 'Predicted Temperature (Next Hour)',
        'rain_prediction': 'Rain Prediction',
        'yes': 'Yes',
        'no': 'No',
        'rain_probability': 'Rain Probability',
        'error': 'Error',
        'city_not_found': 'City not found. Please check the spelling.',
        'api_error': 'Unable to fetch weather data. Please try again.'
    },
    'mr': {
        'title': 'रिअल-टाइम हवामान अंदाज',
        'subtitle': 'थेट हवामान डेटा + ML अंदाज',
        'city_label': 'शहराचे नाव टाका',
        'city_placeholder': 'उदा., मुंबई, पुणे, नागपूर',
        'predict_btn': 'हवामान अंदाज',
        'current_weather': 'सध्याचे हवामान',
        'temperature': 'तापमान',
        'feels_like': 'जाणवते',
        'humidity': 'आर्द्रता',
        'pressure': 'दाब',
        'wind_speed': 'वाऱ्याचा वेग',
        'ml_predictions': 'ML अंदाज',
        'predicted_temp': 'अंदाजित तापमान (पुढील तास)',
        'rain_prediction': 'पाऊस अंदाज',
        'yes': 'होय',
        'no': 'नाही',
        'rain_probability': 'पाऊस संभाव्यता',
        'error': 'त्रुटी',
        'city_not_found': 'शहर सापडले नाही. कृपया स्पेलिंग तपासा.',
        'api_error': 'हवामान डेटा मिळवू शकत नाही. कृपया पुन्हा प्रयत्न करा.'
    }
}


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return jsonify({"message": "API working 🚀"})

@app.route('/api/translations/<lang>')
def get_translations(lang):
    return jsonify(TRANSLATIONS.get(lang, TRANSLATIONS['en']))

@app.route('/api/history/<city>')
def get_history(city):
    if not supabase:
        return jsonify({'error': 'Database not configured'}), 503
    try:
        result = supabase.table('weather_predictions')\
            .select('*')\
            .eq('city', city)\
            .order('created_at', desc=True)\
            .limit(10)\
            .execute()
        return jsonify({'history': result.data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        city = data.get('city', '').strip()

        if not city:
            return jsonify({'error': 'City name is required'}), 400

        weather_data = get_weather_data(city)

        if not weather_data:
            return jsonify({'error': 'City not found or API error'}), 404

        features = get_features_for_ml(weather_data)
        X = np.array([[
            features['temperature'],
            features['humidity'],
            features['pressure'],
            features['wind_speed']
        ]])

        rain_prediction = rain_model.predict(X)[0]
        rain_probability = rain_model.predict_proba(X)[0][1]
        predicted_temp = temp_model.predict(X)[0]

        if supabase:
            try:
                supabase.table('weather_predictions').insert({
                    'city': weather_data['city'],
                    'country': weather_data['country'],
                    'current_temperature': float(weather_data['temperature']),
                    'predicted_temperature': float(predicted_temp),
                    'humidity': float(weather_data['humidity']),
                    'pressure': float(weather_data['pressure']),
                    'wind_speed': float(weather_data['wind_speed']),
                    'rain_prediction': bool(rain_prediction),
                    'rain_probability': float(rain_probability),
                    'weather_condition': weather_data['weather']
                }).execute()
            except Exception as db_error:
                print(f"Database error: {db_error}")
        else:
            print("Database not configured - skipping insert")

        response = {
            'current_weather': weather_data,
            'predictions': {
                'rain': bool(rain_prediction),
                'rain_probability': float(rain_probability),
                'predicted_temperature': float(predicted_temp)
            },
            'timestamp': datetime.now().isoformat()
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
