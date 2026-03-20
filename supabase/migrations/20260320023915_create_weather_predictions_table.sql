/*
  # Weather Predictions History Table

  1. New Tables
    - `weather_predictions`
      - `id` (uuid, primary key) - Unique identifier for each prediction
      - `city` (text) - City name
      - `country` (text) - Country code
      - `current_temperature` (real) - Current temperature from API
      - `predicted_temperature` (real) - ML predicted temperature
      - `humidity` (real) - Humidity percentage
      - `pressure` (real) - Atmospheric pressure
      - `wind_speed` (real) - Wind speed
      - `rain_prediction` (boolean) - Rain prediction (true/false)
      - `rain_probability` (real) - Rain probability (0-1)
      - `weather_condition` (text) - Weather condition description
      - `created_at` (timestamptz) - Timestamp of prediction
  
  2. Security
    - Enable RLS on `weather_predictions` table
    - Add policy for public read access (weather data is public)
    - Add policy for anonymous insert (allow storing predictions)
*/

CREATE TABLE IF NOT EXISTS weather_predictions (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  city text NOT NULL,
  country text NOT NULL,
  current_temperature real NOT NULL,
  predicted_temperature real NOT NULL,
  humidity real NOT NULL,
  pressure real NOT NULL,
  wind_speed real NOT NULL,
  rain_prediction boolean NOT NULL,
  rain_probability real NOT NULL,
  weather_condition text NOT NULL,
  created_at timestamptz DEFAULT now()
);

ALTER TABLE weather_predictions ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Anyone can view weather predictions"
  ON weather_predictions
  FOR SELECT
  TO anon, authenticated
  USING (true);

CREATE POLICY "Anyone can insert weather predictions"
  ON weather_predictions
  FOR INSERT
  TO anon, authenticated
  WITH CHECK (true);

CREATE INDEX idx_weather_predictions_city ON weather_predictions(city);
CREATE INDEX idx_weather_predictions_created_at ON weather_predictions(created_at DESC);
