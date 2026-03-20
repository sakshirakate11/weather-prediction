import requests
from fetch_weather import get_weather_data, get_features_for_ml
import pickle
import numpy as np

def test_weather_api():
    print("Testing Weather API...")
    weather = get_weather_data("Mumbai")
    if weather:
        print(f"✅ Weather API: {weather['city']}, {weather['temperature']}°C")
        return True
    else:
        print("❌ Weather API failed")
        return False

def test_ml_models():
    print("\nTesting ML Models...")
    try:
        with open('rain_model.pkl', 'rb') as f:
            rain_model = pickle.load(f)
        with open('temp_model.pkl', 'rb') as f:
            temp_model = pickle.load(f)

        X = np.array([[30, 75, 1010, 5]])
        rain_pred = rain_model.predict(X)[0]
        temp_pred = temp_model.predict(X)[0]

        print(f"✅ Rain Model: {'Rain' if rain_pred else 'No Rain'}")
        print(f"✅ Temp Model: {temp_pred:.1f}°C")
        return True
    except Exception as e:
        print(f"❌ ML Models failed: {e}")
        return False

def test_full_prediction():
    print("\nTesting Full Prediction Pipeline...")
    weather = get_weather_data("London")
    if not weather:
        print("❌ Could not fetch weather data")
        return False

    features = get_features_for_ml(weather)
    print(f"Features: {features}")

    try:
        with open('rain_model.pkl', 'rb') as f:
            rain_model = pickle.load(f)
        with open('temp_model.pkl', 'rb') as f:
            temp_model = pickle.load(f)

        X = np.array([[
            features['temperature'],
            features['humidity'],
            features['pressure'],
            features['wind_speed']
        ]])

        rain_pred = rain_model.predict(X)[0]
        rain_prob = rain_model.predict_proba(X)[0][1]
        temp_pred = temp_model.predict(X)[0]

        print(f"✅ Current: {weather['city']}, {weather['temperature']}°C")
        print(f"✅ Predicted Temp: {temp_pred:.1f}°C")
        print(f"✅ Rain: {'Yes' if rain_pred else 'No'} ({rain_prob*100:.1f}%)")
        return True
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Real-Time Weather Prediction System\n")
    print("=" * 50)

    results = []
    results.append(test_weather_api())
    results.append(test_ml_models())
    results.append(test_full_prediction())

    print("\n" + "=" * 50)
    print(f"\n✅ Tests Passed: {sum(results)}/{len(results)}")

    if all(results):
        print("🎉 All systems operational!")
    else:
        print("⚠️  Some tests failed. Check errors above.")
