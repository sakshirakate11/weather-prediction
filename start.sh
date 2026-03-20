#!/bin/bash

echo "🌍 Starting Real-Time Weather Prediction System..."
echo ""

if [ ! -f "rain_model.pkl" ] || [ ! -f "temp_model.pkl" ]; then
    echo "📊 Training ML models (first time only)..."
    python3 train_model.py
    echo ""
fi

echo "🚀 Starting Flask server..."
echo "🌐 Open http://localhost:5000 in your browser"
echo ""

python3 app.py
