# COMPLETE DEPLOYMENT GUIDE - Step by Step

## 🎯 Goal
Deploy the Islamic Scholar AI backend so your website can answer ANY Islamic question.

---

## 📦 What You Have Now

I've created a complete backend with these files:
- `main.py` - FastAPI application with GPT-4 integration
- `requirements.txt` - Python dependencies
- `README.md` - Documentation
- `.gitignore` - Git ignore rules

---

## 🚀 DEPLOYMENT STEPS (15 minutes)

### Step 1: Get Your OpenAI API Key (5 minutes)

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Name it "Islamic Scholar AI"
4. Copy the key (starts with `sk-...`)
5. **SAVE IT SOMEWHERE SAFE** - you can't see it again!

**Cost:** ~$0.03 per question. $20 credit = ~600 questions.

---

### Step 2: Create GitHub Repository (3 minutes)

1. Go to https://github.com/new
2. Repository name: `islamic-scholar-backend`
3. Make it **Public**
4. **DO NOT** add README, .gitignore, or license (we have them)
5. Click "Create repository"
6. **KEEP THIS PAGE OPEN** - you'll need the commands

---

### Step 3: Upload Code to GitHub (2 minutes)

**Option A: If you have git installed**

Download the backend folder I created, then:

```bash
cd islamic-scholar-backend

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/islamic-scholar-backend.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

**Option B: If no git - Use GitHub Upload**

1. Download all 4 files (main.py, requirements.txt, README.md, .gitignore)
2. Go to your GitHub repository
3. Click "uploading an existing file"
4. Drag all 4 files
5. Click "Commit changes"

---

### Step 4: Deploy on Render.com (5 minutes)

1. **Go to:** https://render.com
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (easiest)
4. Once signed in, click **"New +"** → **"Web Service"**

5. **Connect Repository:**
   - Click "Connect account" if needed
   - Find and select: `islamic-scholar-backend`
   - Click "Connect"

6. **Configure Service:**
   
   Fill in these fields:
   
   | Field | Value |
   |-------|-------|
   | **Name** | `islamic-scholar-api` |
   | **Region** | (Choose closest to you) |
   | **Branch** | `main` |
   | **Root Directory** | (leave blank) |
   | **Runtime** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt` |
   | **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
   | **Instance Type** | **Free** |

7. **Add Environment Variable:**
   - Scroll down to "Environment Variables"
   - Click "Add Environment Variable"
   - **Key:** `OPENAI_API_KEY`
   - **Value:** (paste your OpenAI key from Step 1)
   - Click "Add"

8. Click **"Create Web Service"**

9. **Wait 5-10 minutes** while it deploys
   - You'll see logs scrolling
   - Wait for "Build successful" and "Deploy live"

10. **Get Your API URL:**
    - At the top, you'll see: `https://islamic-scholar-api.onrender.com`
    - **COPY THIS URL** - you'll need it!

---

### Step 5: Test Your API (1 minute)

**In your browser, go to:**
```
https://islamic-scholar-api.onrender.com/health
```

You should see:
```json
{
  "status": "healthy",
  "openai_configured": true
}
```

**Test asking a question:**
```
https://islamic-scholar-api.onrender.com/api/rag/ask?q=Who%20was%20Hamza
```

You should see a JSON response with an answer!

---

### Step 6: Connect Website to Backend (2 minutes)

**Tell the AI website maker:**

"Update the API URL to connect to my deployed backend:

```typescript
// src/services/api.ts
const API_BASE_URL = 'https://islamic-scholar-api.onrender.com';

// Remove 'localhost:8000' and replace with the URL above
```

Test by asking questions like:
- How did Hamza die?
- What surah is best for forgiveness?
- Who was Abu Bakr?
"

---

## ✅ Verification Checklist

- [ ] OpenAI API key obtained
- [ ] GitHub repository created
- [ ] Code uploaded to GitHub
- [ ] Render.com account created
- [ ] Web service deployed
- [ ] `/health` endpoint returns healthy
- [ ] Test question returns answer
- [ ] Website API URL updated
- [ ] Website can ask questions successfully

---

## 🎉 Success!

Your backend is now live and can answer ANY Islamic question!

**Your API URL:** `https://islamic-scholar-api.onrender.com`

**API Documentation:** `https://islamic-scholar-api.onrender.com/docs`

---

## 💰 Cost Breakdown

| Service | Cost |
|---------|------|
| Render.com | **FREE** (750 hrs/month) |
| OpenAI API | ~$0.03/question |
| **Total** | ~$20-30/month for 600 questions |

---

## 🐛 Troubleshooting

**Problem:** Build failed on Render
- Check that `requirements.txt` is uploaded
- Check Start Command is correct

**Problem:** Health check returns 500 error
- Check OPENAI_API_KEY is set in Environment Variables
- Check the key is valid

**Problem:** Questions return errors
- Check OpenAI API has credits ($20 minimum)
- Check API key has permissions

**Problem:** Website still shows "Backend offline"
- Make sure you updated API_BASE_URL in website code
- Remove `http://localhost:8000` completely

---

## 🔄 To Update Code Later

```bash
cd islamic-scholar-backend
# Make changes to main.py
git add .
git commit -m "Update: description of changes"
git push

# Render will auto-deploy in ~5 minutes
```

---

## 📞 Need Help?

If stuck, check:
1. Render logs (click "Logs" tab)
2. API docs at `/docs`
3. Test with curl or browser

Common issues:
- Forgot to add OPENAI_API_KEY
- Wrong Start Command
- OpenAI account has no credits
