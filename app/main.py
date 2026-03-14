from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import re
import string
import os

app = FastAPI(title="Bangla SMS Spam Detector", version="1.0.0")

# ─── Mount static files & templates ───────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# ─── Load model & vectorizer ──────────────────────────────────────────────────
MODEL_PATH = os.path.join(BASE_DIR, "svm_smishing_model.pkl")
TFIDF_PATH = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(TFIDF_PATH, "rb") as f:
    tfidf = pickle.load(f)

# ─── Text cleaning (same as training) ─────────────────────────────────────────
def clean_text(text: str) -> str:
    text = str(text)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    text = text.lower()
    return text

# ─── Label mapping ─────────────────────────────────────────────────────────────
LABEL_MAP = {
    "spam":   {"label": "Spam",        "color": "red",    "icon": "🚨"},
    "promo":  {"label": "Promotional", "color": "orange", "icon": "📢"},
    "normal": {"label": "Normal",      "color": "green",  "icon": "✅"},
    # fallback for binary datasets (ham/spam)
    "ham":    {"label": "Normal",      "color": "green",  "icon": "✅"},
}

# ─── Request / Response schemas ───────────────────────────────────────────────
class SMSRequest(BaseModel):
    message: str

class SMSResponse(BaseModel):
    original_message: str
    cleaned_message: str
    prediction: str
    label: str
    color: str
    icon: str
    confidence_note: str

# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_model=SMSResponse)
async def predict(data: SMSRequest):
    cleaned = clean_text(data.message)
    vec = tfidf.transform([cleaned])
    raw_pred = model.predict(vec)[0].lower()

    meta = LABEL_MAP.get(raw_pred, {"label": raw_pred.title(), "color": "gray", "icon": "❓"})

    confidence_note = (
        "High-confidence spam signal detected."     if meta["color"] == "red"    else
        "Promotional/marketing content detected."   if meta["color"] == "orange" else
        "Message appears safe and normal."
    )

    return SMSResponse(
        original_message=data.message,
        cleaned_message=cleaned,
        prediction=raw_pred,
        label=meta["label"],
        color=meta["color"],
        icon=meta["icon"],
        confidence_note=confidence_note,
    )


@app.get("/health")
async def health():
    return {"status": "ok", "model": "LinearSVC", "vectorizer": "TF-IDF"}
