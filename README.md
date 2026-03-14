# 🛡️ Bangla SMS Spam Detector — FastAPI

A web app to classify Bangla SMS messages as **Spam**, **Promotional**, or **Normal**
using your trained LinearSVC + TF-IDF model.

---

## 📁 Project Structure

```
smishing-detector/
├── app/
│   └── main.py                  # FastAPI app
├── templates/
│   └── index.html               # Frontend UI
├── static/                      # (optional: CSS/JS assets)
├── svm_smishing_model.pkl       # ← YOUR saved model
├── tfidf_vectorizer.pkl         # ← YOUR saved vectorizer
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Place your model files
Copy both pickle files into the project root:
```
svm_smishing_model.pkl
tfidf_vectorizer.pkl
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Open in browser
```
http://localhost:8000
```

---

## 🔌 API Endpoints

### `POST /predict`
Classify a message.

**Request body:**
```json
{ "message": "আপনার বিকাশ একাউন্ট বন্ধ হতে যাচ্ছে" }
```

**Response:**
```json
{
  "original_message": "আপনার বিকাশ একাউন্ট বন্ধ হতে যাচ্ছে",
  "cleaned_message": "আপনার বিকাশ একাউন্ট বন্ধ হতে যাচ্ছে",
  "prediction": "spam",
  "label": "Spam",
  "color": "red",
  "icon": "🚨",
  "confidence_note": "High-confidence spam signal detected."
}
```

### `GET /health`
Health check — confirms model is loaded.

---

## 🏷️ Label Mapping

| Model output | Display label | Meaning         |
|-------------|---------------|-----------------|
| `spam`      | 🚨 Spam        | Phishing/smishing |
| `promo`     | 📢 Promotional | Marketing SMS    |
| `normal`    | ✅ Normal       | Legitimate SMS   |
| `ham`       | ✅ Normal       | (binary fallback)|

> **Note:** If your model uses only `spam`/`ham` labels, it will still work — `ham` maps to Normal.

---

## 🚀 Deploy to Production (optional)

### With Gunicorn
```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### With Docker
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
```bash
docker build -t sms-detector .
docker run -p 8000:8000 sms-detector
```
