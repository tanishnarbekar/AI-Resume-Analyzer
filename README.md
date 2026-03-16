# 🧠 ResumeIQ — AI Resume Analyzer

A final year project that uses NLP and skill matching to analyze resumes, generate scores, and provide actionable improvement suggestions.

---

## 🚀 Features

- 📄 Upload PDF, DOCX, or TXT resumes
- 🔍 NLP-based skill detection
- 🎯 Job role matching (8 roles supported)
- 📊 Resume score with grade (A–F)
- 💡 Smart improvement suggestions
- 🔎 ATS keyword density analysis
- 📋 Resume section detection

## 🏗 Tech Stack

| Layer    | Technology           |
|----------|----------------------|
| Backend  | Python, Flask        |
| NLP      | Regex + Skill DB     |
| Parser   | PyPDF2, python-docx  |
| Frontend | HTML, CSS, JavaScript|

---

## ⚙️ Setup & Run

### 1. Clone / download the project
```bash
cd resume-analyzer
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
```
http://localhost:5000
```

---

## 📂 Project Structure

```
resume-analyzer/
├── app.py              # Flask backend & routes
├── resume_parser.py    # PDF/DOCX/TXT text extraction
├── skill_matcher.py    # NLP skill detection & scoring
├── requirements.txt
├── uploads/            # Temporary upload storage
├── templates/
│   └── index.html      # Single-page UI
└── static/
    ├── style.css
    └── script.js
```

---

## 🎯 Supported Job Roles

- Data Scientist
- AI Engineer
- ML Engineer
- Backend Developer
- Frontend Developer
- Full Stack Developer
- Data Analyst
- DevOps Engineer

---

## 📈 Scoring Formula

| Component         | Weight |
|-------------------|--------|
| Core Skills Match | 65%    |
| Bonus Skills      | 20%    |
| Resume Structure  | 15%    |

---

## 🔮 Future Enhancements

- [ ] spaCy NLP for smarter skill extraction
- [ ] GPT-powered personalized suggestions
- [ ] Multi-resume comparison
- [ ] LinkedIn profile integration
- [ ] Export report as PDF

---

## 💼 Resume Line

> *Built an AI-powered resume analyzer that extracts skills from resumes using NLP, evaluates candidate-job fit through skill matching, and generates actionable improvement suggestions with ATS keyword density analysis.*

---

**Built with ❤️ as a Final Year Project**
