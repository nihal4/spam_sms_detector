<img src="screenshoot/Screenshot%202026-03-14%20at%207.58.53%E2%80%AFPM.png" width="700">
<p>A machine learning web app that classifies Bangla SMS messages as <b>Spam</b>, <b>Promotional</b>, or <b>Normal</b> in real time. Built with FastAPI + LinearSVC trained on the BangalaBarta Bangla Smishing dataset.</p>



<h2>Live Demo</h2>

[sms-spam-detector.onrender.com](https://sms-spam-detector.onrender.com)

> Note: Uisng free tier may take ~30 seconds to wake up on first visit.

<h2>Screenshot</h2>

<table>
  <tr>
    <td align="center">
      <img src="screenshoot/Screenshot%202026-03-14%20at%2010.03.12%E2%80%AFPM.png" width="350">
    </td>
    <td align="center">
      <img src="screenshoot/Screenshot%202026-03-14%20at%2010.03.21%E2%80%AFPM.png" width="350">
    </td>
    <td align="center">
      <img src="screenshoot/Screenshot%202026-03-14%20at%2010.03.29%E2%80%AFPM.png" width="350">
    </td>
  </tr>
</table>



<h2>How It Works</h2>

<ol>
  <li>User pastes a Bangla SMS message</li>
  <li> Text is cleaned (URLs, numbers, punctuation removed)</li>
  <li>TF-IDF vectorizer converts text to features</li>
  <li>LinearSVC model predicts the class</li>
  <li>Result is shown instantly with color-coded label</li>
</ol>
<table>
  <tr>
    <th>Label</th>
    <th>Meaning</th>
  </tr>
  <tr>
    <td>🚨 Spam</td>
    <td>Phishing / smishing attempts</td>
  </tr>
  <tr>
    <td>📢 Promotional </td>
    <td>Marketing or offer messages</td>
  </tr>
  <tr>
    <td>✅ Normal</td>
    <td>Legitimate everyday SMS</td>
  </tr>
</table>


<h2>Run Locally</h2>

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



<h2>Tech Stack</h2>
<ul>
  <li>
    <b>Backend:</b>FastAPI, Python
  </li>
  <li>
    <b>ML Model:</b>LinearSVC (scikit-learn)
  </li>
    <li>
    <b>Vectorizer:</b>TF-IDF (unigram + bigram, 5000 features)
  </li>
   <li>
    <b>Frontend:</b> HTML, CSS, Vanilla JS
  </li>
  <li>
    <b>Hosting:</b>Render
  </li>
</ul>

<h2>Model Performance</h2>

<h3 align="center"></h3>

<table>
  <caption>Test Accuracy: 98.2% (evaluated on 20% holdout set)</caption>
  <thead>
    <tr>
      <th>Class</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
      <th>Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Normal</td>
      <td>0.98</td>
      <td>0.97</td>
      <td>0.98</td>
      <td>185</td>
    </tr>
    <tr>
      <td>Promo</td>
      <td>0.99</td>
      <td>0.99</td>
      <td>0.99</td>
      <td>185</td>
    </tr>
    <tr>
      <td>Smish</td>
      <td>0.97</td>
      <td>0.98</td>
      <td>0.98</td>
      <td>185</td>
    </tr>
    <tr>
      <td><b>Weighted Avg</b></td>
      <td><b>0.98</b></td>
      <td><b>0.98</b></td>
      <td><b>0.98</b></td>
      <td><b>555</b></td>
    </tr>
  </tbody>
</table>

<h2>Training details:</h2>
<ul>
  <li>Algorithm: LinearSVC</li>
  <li>Vectorizer: TF-IDF (unigram + bigram, max 5000 features)</li>
  <li>Train & Test Split: 80% train / 20% test (stratified)</li>
  <li>Cross-validation: 5-fold CV</li>
</ul>


<h2>Dataset</h2>

<p>Trained on the <b><i>BangalaBarta Bangla Spam SMS / Smishing</i></b> dataset containing labeled Bangla SMS messages across spam, promotional, and normal categories.</p>


<h4>Citation:</h4>
<p>
<cite>
Shahriyar, Md Farhan; Tanbhir, Gazi (2025), 
"<i>Bangalabarta: A Spam / Smishing SMS Dataset Bangla</i>", 
Mendeley Data, V2, doi: 
<a href="https://doi.org/10.17632/jfkfbw3gzh.2" target="_blank">10.17632/jfkfbw3gzh.2</a>
</cite>
</p>


<h2>Author</h2>

<b>S. M. Nihal Ahmed</b> <br>
[LinkedIn](https://www.linkedin.com/in/smnahmed28/)
