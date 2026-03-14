# 🛡️ Bangla SMS Spam Detector

A machine learning web app that classifies Bangla SMS messages as **Spam**, **Promotional**, or **Normal** in real time.

Built with FastAPI + LinearSVC trained on the BangalaBarta Bangla Smishing dataset.

---

## 🌐 Live Demo

👉 [sms-spam-detector.onrender.com](https://sms-spam-detector.onrender.com)

> Note: Free tier may take ~30 seconds to wake up on first visit.

---

## 📸 Screenshot

> _(Add a screenshot of your app here)_

---

## 🧠 How It Works

1. User pastes a Bangla SMS message
2. Text is cleaned (URLs, numbers, punctuation removed)
3. TF-IDF vectorizer converts text to features
4. LinearSVC model predicts the class
5. Result is shown instantly with color-coded label

| Label | Meaning |
|-------|---------|
| 🚨 Spam | Phishing / smishing attempts |
| 📢 Promotional | Marketing or offer messages |
| ✅ Normal | Legitimate everyday SMS |

---

## 🗂️ Project Structure

```
smishing-detector/
├── app/
│   └── main.py                  # FastAPI backend
├── templates/
│   └── index.html               # Frontend UI
├── static/                      # Static assets
├── svm_smishing_model.pkl       # Trained LinearSVC model
├── tfidf_vectorizer.pkl         # Fitted TF-IDF vectorizer
├── render.yaml                  # Render deployment config
├── requirements.txt
└── README.md
```

---

## ⚙️ Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/smishing-detector.git
cd smishing-detector

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install fastapi "uvicorn[standard]" scikit-learn jinja2 python-multipart

# 4. Run the server
python -m uvicorn app.main:app --reload
```

Open **http://localhost:8000**

---

## 🔌 API

### `POST /predict`

**Request:**
```json
{ "message": "আপনার বিকাশ একাউন্ট বন্ধ হতে যাচ্ছে" }
```

**Response:**
```json
{
  "prediction": "spam",
  "label": "Spam",
  "icon": "🚨",
  "confidence_note": "High-confidence spam signal detected."
}
```

### `GET /health`
Returns model status.

---

## 🏗️ Tech Stack

- **Backend:** FastAPI, Python
- **ML Model:** LinearSVC (scikit-learn)
- **Vectorizer:** TF-IDF (unigram + bigram, 5000 features)
- **Frontend:** HTML, CSS, Vanilla JS
- **Hosting:** Render

---

## 📈 Model Performance

**Test Accuracy: 98.2%** (evaluated on 20% holdout set)

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| Normal | 0.98 | 0.97 | 0.98 | 185 |
| Promo | 0.99 | 0.99 | 0.99 | 185 |
| Smish | 0.97 | 0.98 | 0.98 | 185 |
| **Weighted Avg** | **0.98** | **0.98** | **0.98** | **555** |

**Training details:**
- Algorithm: LinearSVC
- Vectorizer: TF-IDF (unigram + bigram, max 5000 features)
- Split: 80% train / 20% test (stratified)
- Cross-validation: 5-fold CV

---

## 📊 Dataset

Trained on the **BangalaBarta Bangla Spam SMS / Smishing** dataset containing labeled Bangla SMS messages across spam, promotional, and normal categories.

**Citation:**
> Shahriyar, Md Farhan; Tanbhir, Gazi (2025), "Bangalabarta : A Spam / Smishing SMS Dataset Bangla", Mendeley Data, V2, doi: [10.17632/jfkfbw3gzh.2](https://doi.org/10.17632/jfkfbw3gzh.2)

---

## 👤 Author

**Nihal Ahmed**  
[GitHub](https://github.com/yourusername) · [LinkedIn](https://linkedin.com/in/yourusername)
