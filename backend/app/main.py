from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import shutil
from pathlib import Path
from .parser import extract_text_from_file
from .ai_service import enhance_resume_text
from .ats_client import get_ats_score

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-resume-agent.vercel.app",   # your frontend
        "http://localhost:3000",                # for local testing
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = Path('/tmp/uploads')
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.post('/api/upload')
async def upload(file: UploadFile = File(...)):
    fp = UPLOAD_DIR / file.filename
    with open(fp,"wb") as f:
        shutil.copyfileobj(file.file,f)
    text = extract_text_from_file(str(fp))
    raw = get_ats_score(text)
    enhanced = enhance_resume_text(text)
    enh_score = get_ats_score(enhanced)
    return JSONResponse({
        "original_text": text[:5000],
        "enhanced_text": enhanced[:5000],
        "original_score": raw,
        "enhanced_score": enh_score
    })

@app.post('/api/manual')
async def manual(name: str = Form(...), email: str = Form(...), skills: str = Form(...), experience: str = Form(...)):
    txt = f"Name: {name}\nEmail: {email}\nSkills: {skills}\nExperience: {experience}"
    raw = get_ats_score(txt)
    enh = enhance_resume_text(txt)
    enh_s = get_ats_score(enh)
    return JSONResponse({
        "original_text": txt,
        "enhanced_text": enh,
        "original_score": raw,
        "enhanced_score": enh_s
    })

@app.get("/health")
def h():
    return {"status":"ok"}
