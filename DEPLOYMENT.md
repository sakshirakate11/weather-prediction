# Deployment Guide

## Quick Deploy to Render

1. **Create Account**: Go to [Render.com](https://render.com) and sign up

2. **New Web Service**: Click "New +" → "Web Service"

3. **Connect Repository**:
   - Connect your GitHub/GitLab
   - Select this repository

4. **Configuration**:
   ```
   Name: weather-prediction-system
   Environment: Python 3
   Build Command: pip install -r requirements.txt && python train_model.py
   Start Command: gunicorn app:app
   ```

5. **Environment Variables**:
   - Add `VITE_SUPABASE_URL`
   - Add `VITE_SUPABASE_ANON_KEY`

6. **Deploy**: Click "Create Web Service"

7. **Done**: Your app will be live at `https://weather-prediction-system.onrender.com`

## Deploy to Railway

1. **Create Account**: Go to [Railway.app](https://railway.app)

2. **New Project**: Click "New Project" → "Deploy from GitHub"

3. **Select Repository**: Choose your repository

4. **Configuration**: Railway auto-detects Python and uses `Procfile`

5. **Environment Variables**:
   - Add `VITE_SUPABASE_URL`
   - Add `VITE_SUPABASE_ANON_KEY`

6. **Deploy**: Automatic deployment starts

7. **Domain**: Railway provides a public URL

## Deploy to Heroku

1. **Install Heroku CLI**:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. **Login**:
   ```bash
   heroku login
   ```

3. **Create App**:
   ```bash
   heroku create weather-prediction-ml
   ```

4. **Set Environment Variables**:
   ```bash
   heroku config:set VITE_SUPABASE_URL=your_url
   heroku config:set VITE_SUPABASE_ANON_KEY=your_key
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

6. **Open App**:
   ```bash
   heroku open
   ```

## Local Development

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train Models**:
   ```bash
   python train_model.py
   ```

3. **Set Environment Variables**:
   Create `.env` file:
   ```
   VITE_SUPABASE_URL=your_url
   VITE_SUPABASE_ANON_KEY=your_key
   ```

4. **Run Server**:
   ```bash
   python app.py
   ```

5. **Access**: Open `http://localhost:5000`

## Important Notes

- **Model Files**: The `.pkl` files are large (46MB total). Ensure they're trained before deployment
- **API Key**: OpenWeatherMap API key is already included in `fetch_weather.py`
- **Database**: Supabase table `weather_predictions` must exist
- **Port**: Most platforms auto-assign PORT. Code handles this with `os.environ.get('PORT', 5000)`

## Troubleshooting

### Models Not Found
```bash
python train_model.py
```

### Database Connection Error
Check environment variables:
```bash
echo $VITE_SUPABASE_URL
echo $VITE_SUPABASE_ANON_KEY
```

### API Error
- Verify OpenWeatherMap API key is valid
- Check city spelling
- Ensure internet connectivity

## Performance Tips

1. **Caching**: Add Redis for API response caching
2. **CDN**: Use CDN for static assets
3. **Compression**: Enable gzip in gunicorn
4. **Database**: Add indexes on frequently queried columns (already done)

## Security Checklist

- [x] API keys in environment variables
- [x] CORS configured properly
- [x] SQL injection prevented (using ORM)
- [x] Input validation in place
- [x] RLS enabled on database tables
- [x] No secrets in code
- [x] HTTPS enforced (platform handles this)

## Monitoring

Add application monitoring:
- **Sentry**: Error tracking
- **LogRocket**: Session replay
- **New Relic**: Performance monitoring
- **Uptime Robot**: Availability monitoring

## Cost Estimation

### Free Tier (Sufficient for Project)
- Render: Free tier available
- Railway: $5/month credit
- Heroku: Limited free dyno hours
- Supabase: Free tier (500MB, 50K queries/month)
- OpenWeatherMap: Free tier (60 calls/min)

### Paid (Production Scale)
- Render: Starting $7/month
- Railway: Pay-as-you-go
- Heroku: $7/month per dyno
- Supabase: $25/month Pro tier
- OpenWeatherMap: $40/month for 200K calls/month
