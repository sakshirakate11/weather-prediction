# Quick Start Guide

## Test Locally (3 Simple Steps)

### 1. Run the Start Script
```bash
./start.sh
```

Or manually:
```bash
python3 train_model.py  # First time only
python3 app.py          # Start server
```

### 2. Open Browser
Navigate to: `http://localhost:5000`

### 3. Test the System
- Enter a city name (e.g., "Mumbai", "London", "New York")
- Click "Predict Weather"
- See live weather data + ML predictions!

## Test the System
```bash
python3 test_system.py
```

Expected output: All 3 tests should pass ✅

## Features to Try

### English Interface
1. Enter "Mumbai" → See predictions in English
2. High humidity → Model predicts rain
3. View current temperature vs predicted temperature

### Marathi Interface
1. Click "मराठी" button at top
2. Enter "पुणे" or any city
3. See all labels in Marathi

### Database Storage
Every prediction is automatically stored in Supabase. Check your Supabase dashboard to see the `weather_predictions` table filling up!

## Example Cities to Test

**India:**
- Mumbai (typically humid, high rain probability)
- Delhi (dry, lower rain probability)
- Bangalore (moderate climate)
- Kolkata (humid)

**International:**
- London (often cloudy, moderate rain)
- Dubai (hot, very low rain)
- New York (variable)
- Tokyo (moderate)

## What to Look For

### Current Weather (API Data)
- Temperature in Celsius
- Humidity percentage
- Pressure in hPa
- Wind speed in m/s
- Weather condition icon

### ML Predictions
- **Predicted Temperature**: Usually within ±2-3°C of current
- **Rain Prediction**: Binary Yes/No
- **Rain Probability**: 0-100% confidence score
  - Above 60% → High chance
  - 40-60% → Moderate chance
  - Below 40% → Low chance

## Understanding the Results

### Why Temperature Prediction Changes
- High humidity → Temperature tends to drop
- Rain conditions → Cooler temperature
- High pressure → More stable temperature

### Why Rain Prediction Works
- Humidity > 75% → Higher rain probability
- Low pressure → Storm systems, more rain
- Combined with temperature creates pattern

## Demo Flow for Presentation

1. **Introduction**: "This is a real-time weather prediction system combining live API data with machine learning."

2. **Show Live Data**: Enter "Mumbai" → "See, this is live temperature from OpenWeatherMap API right now: 25.5°C"

3. **Show ML Prediction**: "Our Random Forest model analyzes humidity (78%), pressure (1009 hPa), and wind to predict: Temperature will be 24.2°C, 73% rain probability"

4. **Show Bilingual**: Switch to Marathi → "Full interface in regional language"

5. **Show Database**: Open Supabase dashboard → "Every prediction stored for history tracking"

6. **Explain Value**: "Unlike simple API display, we're doing actual prediction and pattern analysis"

## Interview Talking Points

### Technical Stack
- "Full-stack application: Flask backend, responsive frontend"
- "Machine Learning: scikit-learn Random Forest models"
- "Database: Supabase PostgreSQL with Row Level Security"
- "API Integration: OpenWeatherMap for live data"

### Architecture Decisions
- "Separated concerns: fetch_weather.py for API, app.py for Flask, train_model.py for ML"
- "Stored predictions in database for tracking accuracy and patterns"
- "Bilingual support shows scalability thinking"

### ML Approach
- "Generated 5,000 realistic training samples"
- "Random Forest chosen for: handles non-linear relationships, provides probability scores, resistant to overfitting"
- "69% rain accuracy, 0.96 R² for temperature - good baseline for improvement"

### Production Readiness
- "Error handling for invalid cities"
- "CORS enabled for API access"
- "Environment variables for security"
- "Gunicorn for production deployment"
- "Database indexes for performance"

## Common Issues & Fixes

### "City not found"
- Check spelling
- Try with country: "Paris,FR"
- Use English city names

### "API Error"
- Check internet connection
- Verify API key in fetch_weather.py (already included)
- OpenWeatherMap might have rate limits

### "Models not found"
- Run: `python3 train_model.py`
- Check if .pkl files exist: `ls -lh *.pkl`

### Database Connection Error
- Verify .env file exists
- Check VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY
- Test connection in Supabase dashboard

## Performance Tips

The system typically:
- Fetches weather data: 200-500ms
- ML prediction: < 50ms
- Database insert: 100-300ms
- **Total response time: < 1 second**

## Next Steps

After testing locally:
1. Read `DEPLOYMENT.md` for cloud deployment
2. Check `README.md` for full documentation
3. Explore code to understand implementation
4. Consider enhancements (7-day forecast, mobile app, etc.)

## Questions?

Review the main `README.md` for detailed explanations of:
- How ML models work
- API endpoint documentation
- Database schema
- Deployment options
- Interview preparation

**Ready to deploy?** → See `DEPLOYMENT.md`

**Want to understand code?** → See `README.md`

**Just want to demo?** → Run `./start.sh` and visit localhost:5000!
