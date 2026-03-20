import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split

np.random.seed(42)

def generate_training_data(n_samples=5000):
    data = []

    for _ in range(n_samples):
        temp = np.random.uniform(10, 45)
        humidity = np.random.uniform(30, 100)
        pressure = np.random.uniform(980, 1030)
        wind_speed = np.random.uniform(0, 25)

        rain_prob = (humidity - 30) / 70 * 0.7
        if temp < 15:
            rain_prob *= 0.5
        if pressure < 1000:
            rain_prob *= 1.3

        rain = 1 if np.random.random() < rain_prob else 0

        future_temp = temp + np.random.uniform(-3, 3)
        if rain:
            future_temp -= np.random.uniform(0, 2)

        data.append({
            'temperature': temp,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed,
            'rain': rain,
            'future_temperature': future_temp
        })

    return pd.DataFrame(data)

print("Generating training data...")
df = generate_training_data()

features = ['temperature', 'humidity', 'pressure', 'wind_speed']
X = df[features]

y_rain = df['rain']
X_train_rain, X_test_rain, y_train_rain, y_test_rain = train_test_split(
    X, y_rain, test_size=0.2, random_state=42
)

print("Training Rain Prediction Model...")
rain_model = RandomForestClassifier(n_estimators=100, random_state=42)
rain_model.fit(X_train_rain, y_train_rain)
rain_accuracy = rain_model.score(X_test_rain, y_test_rain)
print(f"Rain Model Accuracy: {rain_accuracy:.2%}")

y_temp = df['future_temperature']
X_train_temp, X_test_temp, y_train_temp, y_test_temp = train_test_split(
    X, y_temp, test_size=0.2, random_state=42
)

print("Training Temperature Prediction Model...")
temp_model = RandomForestRegressor(n_estimators=100, random_state=42)
temp_model.fit(X_train_temp, y_train_temp)
temp_score = temp_model.score(X_test_temp, y_test_temp)
print(f"Temperature Model R² Score: {temp_score:.2f}")

with open('rain_model.pkl', 'wb') as f:
    pickle.dump(rain_model, f)

with open('temp_model.pkl', 'wb') as f:
    pickle.dump(temp_model, f)

print("\n✅ Models saved successfully!")
print("- rain_model.pkl")
print("- temp_model.pkl")
