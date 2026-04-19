import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load .env from the same directory as this script
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use Groq (free alternative to OpenAI)
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


class SummarizeRequest(BaseModel):
    url: str
    quick: bool = False


def is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def fetch_text(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch URL: {str(e)}")

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)
    return text[:3000]


QUICK_PROMPT = """Analyze this content and return a response in exactly this format, with no extra commentary:

Key Points:
- <most important point>
- <second most important point>
- <third most important point>

Verdict: <Read / Skip / Optional> - <1-line reason>

Content:
{text}"""

FULL_PROMPT = """Analyze this content and return a structured response in exactly this format, with no extra commentary:

Summary:
<2-3 sentence summary>

Key Points:
- <key point 1>
- <key point 2>
- <key point 3>
- <key point 4>
- <key point 5>

Reading Time: <estimated reading time, e.g. "4 min read">

Target Audience: <Beginner / Intermediate / Advanced> - <1-line reason why>

Verdict: <Read / Skip / Optional> - <1-line reason>

Key Takeaway:
<single most important insight, in one sentence>

Content:
{text}"""


@app.get("/")
def serve_frontend():
    return FileResponse("index.html")


@app.post("/summarize")
def summarize(body: SummarizeRequest):
    url = body.url.strip()
    if not url:
        raise HTTPException(status_code=422, detail="URL is empty.")

    if not is_url(url):
        raise HTTPException(status_code=422, detail="Invalid URL format.")

    text = fetch_text(url)

    if not text.strip():
        raise HTTPException(status_code=422, detail="Could not extract any content.")

    prompt = (QUICK_PROMPT if body.quick else FULL_PROMPT).format(text=text)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Free Groq model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=400 if body.quick else 900,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")

    result = response.choices[0].message.content
    return {"result": result, "quick": body.quick}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
