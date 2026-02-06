# Islamic Scholar AI - Backend

FastAPI backend for answering Islamic questions using GPT-4.

## Quick Deploy to Render.com

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create new repository: `islamic-scholar-backend`
3. Make it Public
4. Don't add README (we have one)

### Step 2: Upload Code to GitHub

```bash
# In your terminal, navigate to this folder
cd islamic-scholar-backend

# Initialize git
git init
git add .
git commit -m "Initial commit"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/islamic-scholar-backend.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render.com

1. Go to https://render.com
2. Click "Sign Up" (use GitHub account - easier)
3. Click "New +" → "Web Service"
4. Connect your GitHub repository: `islamic-scholar-backend`
5. Fill in settings:
   - **Name:** islamic-scholar-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Click "Advanced" → "Add Environment Variable":
   - **Key:** `OPENAI_API_KEY`
   - **Value:** Your OpenAI API key (sk-...)
7. Click "Create Web Service"
8. Wait 5-10 minutes for deployment
9. You'll get a URL like: `https://islamic-scholar-api.onrender.com`

### Step 4: Test Your API

Once deployed, test it:

```bash
# Health check
curl https://islamic-scholar-api.onrender.com/health

# Ask a question
curl "https://islamic-scholar-api.onrender.com/api/rag/ask?q=Who%20was%20Hamza"
```

### Step 5: Update Frontend

In your website code, update the API URL:

```typescript
// src/services/api.ts
const API_BASE_URL = 'https://islamic-scholar-api.onrender.com';
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
export OPENAI_API_KEY="sk-your-key"

# Run server
python main.py

# Server runs at http://localhost:8000
```

## API Endpoints

- `GET /` - Root info
- `GET /health` - Health check
- `GET /api/rag/ask?q=question` - Answer Islamic question

## Environment Variables

- `OPENAI_API_KEY` - Required - Your OpenAI API key
- `PORT` - Optional - Server port (default 8000)

## Cost Estimate

- Render.com: Free tier (enough for 1000s of requests)
- OpenAI API: ~$0.03 per question (GPT-4)
- Total: ~$30-50/month for moderate usage
