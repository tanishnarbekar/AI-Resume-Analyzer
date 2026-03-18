# 🧠 ResumeIQ — AI-Powered Resume Analyzer

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Click_Here-brightgreen?style=for-the-badge)](https://resumeiq-rqsw.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![NLP](https://img.shields.io/badge/NLP-Regex_Based-orange?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> Upload your resume → Get an instant score, skill gap analysis & ATS keyword report.
> Built with **Python · Flask · NLP · HTML/CSS/JS**

🌐 **Live Demo:** [resumeiq-rqsw.onrender.com](https://resumeiq-rqsw.onrender.com)

---

## 📸 Screenshots

### 🏠 Home Page
<!-- ============================================================
     Take a screenshot of the homepage at resumeiq-rqsw.onrender.com
     Save it as: screenshots/homepage.png
     ============================================================ -->
![Home Page] # 🧠 ResumeIQ — AI-Powered Resume Analyzer

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Click_Here-brightgreen?style=for-the-badge)](https://resumeiq-rqsw.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![NLP](https://img.shields.io/badge/NLP-Regex_Based-orange?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> Upload your resume → Get an instant score, skill gap analysis & ATS keyword report.
> Built with **Python · Flask · NLP · HTML/CSS/JS**

🌐 **Live Demo:** [resumeiq-rqsw.onrender.com](https://resumeiq-rqsw.onrender.com)

---

## 📸 Screenshots

### 🏠 Home Page
<!-- ============================================================
     Take a screenshot of the homepage at resumeiq-rqsw.onrender.com
     Save it as: screenshots/homepage.png
     ============================================================ -->
![Home Page]# 🧠 ResumeIQ — AI-Powered Resume Analyzer

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Click_Here-brightgreen?style=for-the-badge)](https://resumeiq-rqsw.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![NLP](https://img.shields.io/badge/NLP-Regex_Based-orange?style=for-the-badge)](https://docs.python.org/3/library/re.html)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

> Upload your resume → Get an instant score, skill gap analysis & ATS keyword report.
> Built with **Python · Flask · NLP · HTML/CSS/JS**

🌐 **Live Demo:** [resumeiq-rqsw.onrender.com](https://resumeiq-rqsw.onrender.com)

---

## 📸 Screenshots

### 🏠 Home Page
<!-- ============================================================
     Take a screenshot of the homepage at resumeiq-rqsw.onrender.com
     Save it as: screenshots/homepage.png
     ============================================================ -->
![Home Page]
<img width="1919" height="1079" alt="Screenshot 2026-03-18 135106" src="https://github.com/user-attachments/assets/3f0b4323-da3a-4312-87e2-51a14372f963" />

### 📊 Results Dashboard
<!-- ============================================================
     Upload the sample resume and take a screenshot of the
     results page showing score ring + skill pills
     Save it as: screenshots/results.png
     ============================================================ -->
![Results Dashboard]
<img width="1919" height="1079" alt="Screenshot 2026-03-18 135912" src="https://github.com/user-attachments/assets/0e125914-f4c7-4686-ade8-94423b8ac31b" />


### 💡 Suggestions & Keyword Density
<!-- ============================================================
     Scroll down on results page and capture the keyword
     density bars + suggestion cards
     Save it as: screenshots/suggestions.png
     ============================================================ -->
![Suggestions]
<img width="1919" height="1079" alt="Screenshot 2026-03-18 140013" src="https://github.com/user-attachments/assets/9a67d3dd-c89a-4235-9cd1-fe9ed5aeab7f" />


---

## 📌 About

**ResumeIQ** is a free, open-source web application that helps job seekers evaluate and improve their resumes using **NLP-based skill detection** and a **transparent weighted scoring algorithm** — the same approach used by real-world Applicant Tracking Systems (ATS).

The system reads your resume, identifies your technical skills, compares them against job-role requirements, calculates a score, and tells you exactly what is missing and how to fix it — instantly, with no account required.

> 🎓 Final Year Project — TY B.Sc. Computer Science
> 📍 Sancheti College of Arts, Commerce and Science, Pune | 2025–2026
> 👨‍💻 **Team:** Tanish Narbekar · Sahil Sutar · Dattatray Kulkarni

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Multi-format Support** | Accepts PDF, DOCX, and TXT resume files |
| 🎯 **Job Role Matching** | Matches skills against 8 job roles |
| 📊 **Weighted Scoring** | Core Skills (65%) + Bonus Skills (20%) + Structure (15%) |
| 🔍 **ATS Keyword Density** | Counts keyword frequency like real ATS tools |
| 💡 **Smart Suggestions** | Categorized tips — Critical, Improvement, Warning, Structure |
| 📋 **Section Detection** | Checks for 6 standard resume sections |
| 🚀 **No Paid APIs** | Fully free, no account needed |

---

## ⚙️ How It Works

```
User uploads Resume (PDF / DOCX / TXT)
              ↓
    Flask Backend receives file
              ↓
  resume_parser.py extracts raw text
              ↓
  skill_matcher.py detects skills (NLP)
              ↓
  Compares with job role skill database
              ↓
  Calculates weighted score (65/20/15%)
              ↓
  Generates improvement suggestions
              ↓
  JSON response rendered in browser
```

---

## 🏗️ Project Structure

```
resume-analyzer/
│
├── app.py                  # Flask server — handles routes and file uploads
├── resume_parser.py        # Extracts text from PDF, DOCX, TXT files
├── skill_matcher.py        # NLP skill detection, scoring, suggestions
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
├── .python-version         # Pins Python 3.11
├── README.md
│
├── uploads/                # Temporary storage for uploaded files
├── templates/
│   └── index.html          # Single-page UI
└── static/
    ├── style.css           # Dark-themed stylesheet
    └── script.js           # Async API calls + dynamic rendering
```

---

## 🧮 Scoring Formula

| Component | Weight | Description |
|---|---|---|
| **Core Skills** | 65% | Must-have skills for the selected job role |
| **Bonus Skills** | 20% | Good-to-have skills that add extra value |
| **Resume Structure** | 15% | Presence of standard resume sections |

| Score | Grade | Label |
|---|---|---|
| 85 – 100 | A | Excellent |
| 70 – 84 | B | Good |
| 55 – 69 | C | Average |
| 40 – 54 | D | Needs Work |
| 0 – 39 | F | Poor |

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

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11, Flask 2.3 |
| **NLP / Parsing** | Regex (`re`), PyPDF2, python-docx |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Server** | Gunicorn |
| **Deployment** | Render (Free Tier) |
| **Version Control** | Git + GitHub |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/tanishnarbekar/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
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

## 🔮 Future Enhancements

- [ ] spaCy NLP for smarter skill extraction
- [ ] BERT / Transformers for semantic understanding
- [ ] GPT API for personalized AI-generated suggestions
- [ ] SQLite to store and track analysis history
- [ ] Export full analysis report as PDF
- [ ] LinkedIn profile integration

---

## 🧠 AI Concept Used

This project implements a **Rule-Based Expert System** — a classical branch of AI where domain knowledge is encoded as rules. It mimics how real ATS tools work by using:
- Word boundary regex (`\b`) for context-aware NLP
- A weighted decision algorithm for scoring
- Rule-driven suggestions based on detected skill gaps

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| **Tanish Narbekar** | Backend Development, NLP Engine |
| **Sahil Sutar** | Frontend Development, UI Design |
| **Dattatray Kulkarni** | System Design, Testing & Documentation |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If you found this project helpful, please give it a **star ⭐** — it means a lot to us!

---

### 📊 Results Dashboard
<!-- ============================================================
     Upload the sample resume and take a screenshot of the
     results page showing score ring + skill pills
     Save it as: screenshots/results.png
     ============================================================ -->
![Results Dashboard](screenshots/results.png)

### 💡 Suggestions & Keyword Density
<!-- ============================================================
     Scroll down on results page and capture the keyword
     density bars + suggestion cards
     Save it as: screenshots/suggestions.png
     ============================================================ -->
![Suggestions](screenshots/suggestions.png)

---

## 📌 About

**ResumeIQ** is a free, open-source web application that helps job seekers evaluate and improve their resumes using **NLP-based skill detection** and a **transparent weighted scoring algorithm** — the same approach used by real-world Applicant Tracking Systems (ATS).

The system reads your resume, identifies your technical skills, compares them against job-role requirements, calculates a score, and tells you exactly what is missing and how to fix it — instantly, with no account required.

> 🎓 Final Year Project — TY B.Sc. Computer Science
> 📍 Sancheti College of Arts, Commerce and Science, Pune | 2025–2026
> 👨‍💻 **Team:** Tanish Narbekar · Sahil Sutar · Dattatray Kulkarni

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Multi-format Support** | Accepts PDF, DOCX, and TXT resume files |
| 🎯 **Job Role Matching** | Matches skills against 8 job roles |
| 📊 **Weighted Scoring** | Core Skills (65%) + Bonus Skills (20%) + Structure (15%) |
| 🔍 **ATS Keyword Density** | Counts keyword frequency like real ATS tools |
| 💡 **Smart Suggestions** | Categorized tips — Critical, Improvement, Warning, Structure |
| 📋 **Section Detection** | Checks for 6 standard resume sections |
| 🚀 **No Paid APIs** | Fully free, no account needed |

---

## ⚙️ How It Works

```
User uploads Resume (PDF / DOCX / TXT)
              ↓
    Flask Backend receives file
              ↓
  resume_parser.py extracts raw text
              ↓
  skill_matcher.py detects skills (NLP)
              ↓
  Compares with job role skill database
              ↓
  Calculates weighted score (65/20/15%)
              ↓
  Generates improvement suggestions
              ↓
  JSON response rendered in browser
```

---

## 🏗️ Project Structure

```
resume-analyzer/
│
├── app.py                  # Flask server — handles routes and file uploads
├── resume_parser.py        # Extracts text from PDF, DOCX, TXT files
├── skill_matcher.py        # NLP skill detection, scoring, suggestions
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
├── .python-version         # Pins Python 3.11
├── README.md
│
├── uploads/                # Temporary storage for uploaded files
├── templates/
│   └── index.html          # Single-page UI
└── static/
    ├── style.css           # Dark-themed stylesheet
    └── script.js           # Async API calls + dynamic rendering
```

---

## 🧮 Scoring Formula

| Component | Weight | Description |
|---|---|---|
| **Core Skills** | 65% | Must-have skills for the selected job role |
| **Bonus Skills** | 20% | Good-to-have skills that add extra value |
| **Resume Structure** | 15% | Presence of standard resume sections |

| Score | Grade | Label |
|---|---|---|
| 85 – 100 | A | Excellent |
| 70 – 84 | B | Good |
| 55 – 69 | C | Average |
| 40 – 54 | D | Needs Work |
| 0 – 39 | F | Poor |

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

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11, Flask 2.3 |
| **NLP / Parsing** | Regex (`re`), PyPDF2, python-docx |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Server** | Gunicorn |
| **Deployment** | Render (Free Tier) |
| **Version Control** | Git + GitHub |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/tanishnarbekar/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
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

## 🔮 Future Enhancements

- [ ] spaCy NLP for smarter skill extraction
- [ ] BERT / Transformers for semantic understanding
- [ ] GPT API for personalized AI-generated suggestions
- [ ] SQLite to store and track analysis history
- [ ] Export full analysis report as PDF
- [ ] LinkedIn profile integration

---

## 🧠 AI Concept Used

This project implements a **Rule-Based Expert System** — a classical branch of AI where domain knowledge is encoded as rules. It mimics how real ATS tools work by using:
- Word boundary regex (`\b`) for context-aware NLP
- A weighted decision algorithm for scoring
- Rule-driven suggestions based on detected skill gaps

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| **Tanish Narbekar** | Backend Development, NLP Engine |
| **Sahil Sutar** | Frontend Development, UI Design |
| **Dattatray Kulkarni** | System Design, Testing & Documentation |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If you found this project helpful, please give it a **star ⭐** — it means a lot to us!

---

*Built with ❤️ as a Final Year Project by Team ResumeIQ*

### 📊 Results Dashboard
<!-- ============================================================
     Upload the sample resume and take a screenshot of the
     results page showing score ring + skill pills
     Save it as: screenshots/results.png
     ============================================================ -->
![Results Dashboard](screenshots/results.png)

### 💡 Suggestions & Keyword Density
<!-- ============================================================
     Scroll down on results page and capture the keyword
     density bars + suggestion cards
     Save it as: screenshots/suggestions.png
     ============================================================ -->
![Suggestions](screenshots/suggestions.png)

---

## 📌 About

**ResumeIQ** is a free, open-source web application that helps job seekers evaluate and improve their resumes using **NLP-based skill detection** and a **transparent weighted scoring algorithm** — the same approach used by real-world Applicant Tracking Systems (ATS).

The system reads your resume, identifies your technical skills, compares them against job-role requirements, calculates a score, and tells you exactly what is missing and how to fix it — instantly, with no account required.

> 🎓 Final Year Project — TY B.Sc. Computer Science
> 📍 Sancheti College of Arts, Commerce and Science, Pune | 2025–2026
> 👨‍💻 **Team:** Tanish Narbekar · Sahil Sutar · Dattatray Kulkarni

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **Multi-format Support** | Accepts PDF, DOCX, and TXT resume files |
| 🎯 **Job Role Matching** | Matches skills against 8 job roles |
| 📊 **Weighted Scoring** | Core Skills (65%) + Bonus Skills (20%) + Structure (15%) |
| 🔍 **ATS Keyword Density** | Counts keyword frequency like real ATS tools |
| 💡 **Smart Suggestions** | Categorized tips — Critical, Improvement, Warning, Structure |
| 📋 **Section Detection** | Checks for 6 standard resume sections |
| 🚀 **No Paid APIs** | Fully free, no account needed |

---

## ⚙️ How It Works

```
User uploads Resume (PDF / DOCX / TXT)
              ↓
    Flask Backend receives file
              ↓
  resume_parser.py extracts raw text
              ↓
  skill_matcher.py detects skills (NLP)
              ↓
  Compares with job role skill database
              ↓
  Calculates weighted score (65/20/15%)
              ↓
  Generates improvement suggestions
              ↓
  JSON response rendered in browser
```

---

## 🏗️ Project Structure

```
resume-analyzer/
│
├── app.py                  # Flask server — handles routes and file uploads
├── resume_parser.py        # Extracts text from PDF, DOCX, TXT files
├── skill_matcher.py        # NLP skill detection, scoring, suggestions
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
├── .python-version         # Pins Python 3.11
├── README.md
│
├── uploads/                # Temporary storage for uploaded files
├── templates/
│   └── index.html          # Single-page UI
└── static/
    ├── style.css           # Dark-themed stylesheet
    └── script.js           # Async API calls + dynamic rendering
```

---

## 🧮 Scoring Formula

| Component | Weight | Description |
|---|---|---|
| **Core Skills** | 65% | Must-have skills for the selected job role |
| **Bonus Skills** | 20% | Good-to-have skills that add extra value |
| **Resume Structure** | 15% | Presence of standard resume sections |

| Score | Grade | Label |
|---|---|---|
| 85 – 100 | A | Excellent |
| 70 – 84 | B | Good |
| 55 – 69 | C | Average |
| 40 – 54 | D | Needs Work |
| 0 – 39 | F | Poor |

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

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.11, Flask 2.3 |
| **NLP / Parsing** | Regex (`re`), PyPDF2, python-docx |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Server** | Gunicorn |
| **Deployment** | Render (Free Tier) |
| **Version Control** | Git + GitHub |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/tanishnarbekar/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### 2. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac / Linux
python -m venv venv
source venv/bin/activate
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

## 🔮 Future Enhancements

- [ ] spaCy NLP for smarter skill extraction
- [ ] BERT / Transformers for semantic understanding
- [ ] GPT API for personalized AI-generated suggestions
- [ ] SQLite to store and track analysis history
- [ ] Export full analysis report as PDF
- [ ] LinkedIn profile integration

---

## 🧠 AI Concept Used

This project implements a **Rule-Based Expert System** — a classical branch of AI where domain knowledge is encoded as rules. It mimics how real ATS tools work by using:
- Word boundary regex (`\b`) for context-aware NLP
- A weighted decision algorithm for scoring
- Rule-driven suggestions based on detected skill gaps

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| **Tanish Narbekar** | Backend Development, NLP Engine |
| **Sahil Sutar** | Frontend Development, UI Design |
| **Dattatray Kulkarni** | System Design, Testing & Documentation |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If you found this project helpful, please give it a **star ⭐** — it means a lot to us!

---
