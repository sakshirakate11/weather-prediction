# Real-Time Weather Prediction System
https://web-production-54d55.up.railway.app/
A production-ready weather prediction system that combines live weather data from OpenWeatherMap API with Machine Learning models to predict temperature trends and rain probability.

## Features

- **Live Weather Data**: Fetches real-time weather information for any city worldwide
- **ML Predictions**: Uses Random Forest models to predict:
  - Future temperature (next hour trend)
  - Rain probability with confidence score
- **Bilingual Support**: Full interface in English and Marathi (मराठी)
- **Database Storage**: Stores prediction history in Supabase
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Production Ready**: Deployable to Render, Railway, or any cloud platform

## Technology Stack

### Backend
- **Flask**: Python web framework
- **scikit-learn**: Random Forest models for predictions
- **OpenWeatherMap API**: Live weather data
- **Supabase**: PostgreSQL database for prediction history

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **Vanilla JavaScript**: No heavy frameworks needed
- **Fetch API**: RESTful communication

## Project Structure

```
weather-real/
├── app.py                      # Flask backend server
├── train_model.py              # ML model training script
├── fetch_weather.py            # Weather API integration
├── rain_model.pkl              # Trained rain prediction model
├── temp_model.pkl              # Trained temperature prediction model
├── requirements.txt            # Python dependencies
├── Procfile                    # Deployment configuration
├── templates/
│   └── index.html             # Frontend UI
└── .env                       # Environment variables
```

## How It Works

1. **User Input**: Enter any city name (e.g., Mumbai, London, New York)
2. **API Call**: System fetches live weather data from OpenWeatherMap
3. **ML Processing**: Features (temperature, humidity, pressure, wind speed) are fed into trained models
4. **Predictions**:
   - Random Forest Classifier predicts rain (Yes/No)
   - Random Forest Regressor predicts temperature trend
5. **Database**: Prediction is stored in Supabase for history tracking
6. **Display**: Results shown in beautiful bilingual interface

## Installation

### Prerequisites
- Python 3.8+
- pip
- OpenWeatherMap API key
- Supabase account

### Setup

1. Clone the repository:
```bash
git clone <your-repo>
cd weather-real
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the ML models:
```bash
python train_model.py
```

4. Set up environment variables in `.env`:
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_key
```

5. Run the application:
```bash
python app.py
```

6. Open browser to `http://localhost:5000`

## ML Model Details

### Rain Prediction Model
- **Algorithm**: Random Forest Classifier
- **Features**: Temperature, Humidity, Pressure, Wind Speed
- **Accuracy**: ~69%
- **Output**: Binary (Rain/No Rain) + Probability Score

### Temperature Prediction Model
- **Algorithm**: Random Forest Regressor
- **Features**: Temperature, Humidity, Pressure, Wind Speed
- **R² Score**: 0.96
- **Output**: Predicted temperature for next hour

### Training Data
- 5,000 synthetic samples based on realistic weather patterns
- Relationships between humidity, pressure, and rain
- Temperature variations with weather conditions

## API Endpoints

### `GET /`
Returns the main HTML interface

### `POST /api/predict`
Predicts weather for a given city

**Request Body:**
```json
{
  "city": "Mumbai"
}
```

**Response:**
```json
{
  "current_weather": {
    "city": "Mumbai",
    "country": "IN",
    "temperature": 30.5,
    "humidity": 78,
    "pressure": 1009,
    "wind_speed": 4.5,
    "weather": "Clouds"
  },
  "predictions": {
    "rain": true,
    "rain_probability": 0.73,
    "predicted_temperature": 29.8
  },
  "timestamp": "2024-03-20T12:30:00"
}
```

### `GET /api/translations/<lang>`
Returns translations for the specified language (en/mr)

### `GET /api/history/<city>`
Returns last 10 predictions for the specified city

## Deployment

### Render / Railway

1. Create new Web Service
2. Connect your repository
3. Set environment variables:
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
4. Deploy automatically uses `Procfile`

### Environment Variables Required

```
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

## Database Schema

### weather_predictions table
```sql
- id (uuid, primary key)
- city (text)
- country (text)
- current_temperature (real)
- predicted_temperature (real)
- humidity (real)
- pressure (real)
- wind_speed (real)
- rain_prediction (boolean)
- rain_probability (real)
- weather_condition (text)
- created_at (timestamptz)
```

## Key Differentiators

This project stands out because:

1. **Real API Integration**: Unlike projects using static datasets, this fetches live data
2. **Dual Output**: Shows both API current data AND ML predictions
3. **Production Quality**: Database storage, error handling, responsive design
4. **Bilingual**: Supports multiple languages for wider audience
5. **Startup-Level**: Professional architecture suitable for real products

## Interview Talking Points

**Q: Why use ML when API already provides weather?**

**A:** "The API provides current conditions, but our ML models analyze patterns in temperature, humidity, pressure, and wind speed to predict future trends. This is valuable for:
- Short-term forecasting (next few hours)
- Pattern recognition across different weather conditions
- Learning from historical prediction accuracy
- Providing confidence scores for predictions"

**Q: How accurate are your predictions?**

**A:** "Our rain prediction model achieves 69% accuracy, and temperature model has an R² score of 0.96. These are strong baselines that can be improved with:
- More training data from API history
- Location-specific models
- Seasonal pattern recognition
- Integration with multiple weather APIs"

## Future Enhancements

- [ ] 7-day forecast predictions
- [ ] Weather alerts and notifications
- [ ] Historical data visualization
- [ ] Location-based automatic predictions
- [ ] Mobile app version
- [ ] Model retraining with accumulated data


## Credits

- OpenWeatherMap API for live weather data
- scikit-learn for ML framework

