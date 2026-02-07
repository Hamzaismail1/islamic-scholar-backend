## Islamic Scholar AI - FastAPI Backend
# FIXED VERSION - Uses GPT-3.5-Turbo (works with all API keys)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from typing import List, Dict
import re

app = FastAPI(title="Islamic Scholar AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
async def root():
    return {
        "message": "Islamic Scholar AI API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "openai_configured": bool(os.getenv("OPENAI_API_KEY"))
    }

@app.get("/api/rag/ask")
async def ask_question(q: str):
    """Answer ANY Islamic question using GPT-3.5-Turbo"""
    
    if not q or len(q.strip()) < 3:
        raise HTTPException(status_code=400, detail="Question must be at least 3 characters")
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        # Using gpt-3.5-turbo (available to all users)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert Islamic scholar AI assistant. 

When answering questions:
1. Provide accurate Islamic knowledge based on Quran and Hadith
2. Cite specific sources (Surah:Verse or Hadith collection and number)
3. If discussing fiqh, mention different madhab opinions
4. Be respectful and scholarly in tone
5. If unsure, recommend consulting a qualified scholar

Format with sections:
- Direct answer
- Evidence from Quran (cite Surah:Verse)
- Evidence from Hadith (cite collection and number)
- Madhab opinions (if relevant)
- Practical application"""
                },
                {"role": "user", "content": q}
            ],
            temperature=0.3,
            max_tokens=1500
        )
        
        answer_text = response.choices[0].message.content
        citations = extract_citations(answer_text)
        sources = parse_sources(answer_text)
        
        return {
            "question": q,
            "answer": answer_text,
            "sources": sources,
            "citations": citations,
            "confidence": 0.85
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def extract_citations(text: str) -> List[str]:
    citations = []
    quran_matches = re.findall(r'(?:Quran|Surah)[^\d]*(\d+):(\d+)', text, re.IGNORECASE)
    for match in quran_matches:
        citations.append(f"Quran {match[0]}:{match[1]}")
    hadith_matches = re.findall(r'(Sahih Bukhari|Sahih Muslim|Abu Dawud|Tirmidhi|Nasa\'i|Ibn Majah)[^\d]*(\d+)', text, re.IGNORECASE)
    for match in hadith_matches:
        citations.append(f"{match[0]} {match[1]}")
    return list(set(citations))

def parse_sources(text: str) -> Dict:
    sources = {"quran_verses": [], "hadiths": []}
    quran_matches = re.findall(r'(?:Quran|Surah)[^\d]*(\d+):(\d+)', text, re.IGNORECASE)
    for match in quran_matches:
        sources["quran_verses"].append({
            "surah": int(match[0]),
            "verse": int(match[1]),
            "reference": f"Quran {match[0]}:{match[1]}"
        })
    hadith_matches = re.findall(r'(Sahih Bukhari|Sahih Muslim|Abu Dawud|Tirmidhi)[^\d]*(\d+)', text, re.IGNORECASE)
    for match in hadith_matches:
        sources["hadiths"].append({
            "collection": match[0],
            "number": int(match[1]),
            "reference": f"{match[0]} {match[1]}"
        })
    return sources

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
