import re
from resume_parser import extract_email, extract_phone, extract_name, get_keyword_density

# ── Job Role Definitions ──────────────────────────────────────────────────────
JOB_ROLES = {
    "data_scientist": {
        "title": "Data Scientist",
        "required": ["python", "machine learning", "deep learning", "statistics",
                     "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
                     "sql", "data visualization", "feature engineering"],
        "good_to_have": ["spark", "aws", "gcp", "docker", "mlflow", "nlp",
                         "computer vision", "tableau", "power bi"]
    },
    "ai_engineer": {
        "title": "AI Engineer",
        "required": ["python", "machine learning", "deep learning", "nlp",
                     "pytorch", "tensorflow", "transformers", "api development",
                     "docker", "git", "model deployment"],
        "good_to_have": ["kubernetes", "mlops", "langchain", "huggingface",
                         "aws", "azure", "fastapi", "vector database"]
    },
    "backend_developer": {
        "title": "Backend Developer",
        "required": ["python", "flask", "django", "rest api", "sql", "git",
                     "authentication", "docker", "postgresql", "mongodb"],
        "good_to_have": ["redis", "celery", "aws", "microservices", "graphql",
                         "kubernetes", "ci/cd", "fastapi", "rabbitmq"]
    },
    "frontend_developer": {
        "title": "Frontend Developer",
        "required": ["html", "css", "javascript", "react", "git",
                     "responsive design", "typescript", "rest api"],
        "good_to_have": ["next.js", "vue", "tailwind", "webpack", "testing",
                         "figma", "redux", "graphql", "node.js"]
    },
    "fullstack_developer": {
        "title": "Full Stack Developer",
        "required": ["html", "css", "javascript", "react", "python",
                     "flask", "sql", "git", "rest api", "docker"],
        "good_to_have": ["typescript", "next.js", "mongodb", "aws",
                         "ci/cd", "redis", "graphql", "testing"]
    },
    "ml_engineer": {
        "title": "ML Engineer",
        "required": ["python", "machine learning", "mlops", "docker",
                     "git", "sql", "feature engineering", "model deployment",
                     "scikit-learn", "tensorflow", "pytorch"],
        "good_to_have": ["kubernetes", "airflow", "spark", "aws sagemaker",
                         "mlflow", "ci/cd", "monitoring", "data pipelines"]
    },
    "data_analyst": {
        "title": "Data Analyst",
        "required": ["sql", "excel", "python", "data visualization", "statistics",
                     "pandas", "tableau", "power bi", "reporting"],
        "good_to_have": ["r", "machine learning", "google analytics", "looker",
                         "etl", "hadoop", "spark", "storytelling"]
    },
    "devops_engineer": {
        "title": "DevOps Engineer",
        "required": ["docker", "kubernetes", "ci/cd", "linux", "git",
                     "aws", "terraform", "ansible", "monitoring", "bash"],
        "good_to_have": ["gcp", "azure", "jenkins", "prometheus", "grafana",
                         "helm", "python", "security", "networking"]
    }
}

# ── General Skills Pool ───────────────────────────────────────────────────────
ALL_SKILLS = list(set(
    skill
    for role in JOB_ROLES.values()
    for skill in role["required"] + role["good_to_have"]
))

# ── Resume Sections ───────────────────────────────────────────────────────────
SECTION_KEYWORDS = {
    "education":    ["education", "qualification", "degree", "university", "college", "b.tech", "b.e", "m.tech"],
    "experience":   ["experience", "work experience", "employment", "internship", "worked at"],
    "projects":     ["projects", "personal projects", "academic projects"],
    "skills":       ["skills", "technical skills", "core competencies"],
    "certifications": ["certifications", "certificates", "courses", "training"],
    "achievements": ["achievements", "awards", "honors", "accomplishments"]
}

def detect_sections(text):
    text_lower = text.lower()
    found = []
    for section, keywords in SECTION_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                found.append(section)
                break
    return found

def score_resume_structure(sections):
    """Score based on completeness of resume sections."""
    important = ["education", "experience", "skills", "projects"]
    bonus = ["certifications", "achievements"]
    score = 0
    for s in important:
        if s in sections:
            score += 15
    for s in bonus:
        if s in sections:
            score += 5
    return min(score, 70)  # max 70 from structure

def analyze_resume(text, job_role_key):
    """Main analysis function — returns full result dict."""
    role = JOB_ROLES.get(job_role_key, JOB_ROLES["data_scientist"])
    text_lower = text.lower()

    # ── Skill Matching ──
    required   = role["required"]
    good_to_have = role["good_to_have"]

    matched_required = [s for s in required   if re.search(r'\b' + re.escape(s) + r'\b', text_lower)]
    matched_bonus    = [s for s in good_to_have if re.search(r'\b' + re.escape(s) + r'\b', text_lower)]
    missing_required = [s for s in required   if s not in matched_required]

    # ── Other Skills in Resume ──
    other_skills = [s for s in ALL_SKILLS
                    if s not in required and s not in good_to_have
                    and re.search(r'\b' + re.escape(s) + r'\b', text_lower)]

    # ── Score Calculation ──
    required_score = (len(matched_required) / len(required)) * 65  # 65% weight
    bonus_score    = (len(matched_bonus) / max(len(good_to_have), 1)) * 20  # 20% weight
    sections       = detect_sections(text)
    structure_score = (len(sections) / 6) * 15  # 15% weight

    total_score = round(required_score + bonus_score + structure_score)
    total_score = max(0, min(100, total_score))

    # ── Grade ──
    if total_score >= 85:
        grade, grade_label = "A", "Excellent"
    elif total_score >= 70:
        grade, grade_label = "B", "Good"
    elif total_score >= 55:
        grade, grade_label = "C", "Average"
    elif total_score >= 40:
        grade, grade_label = "D", "Needs Work"
    else:
        grade, grade_label = "F", "Poor"

    # ── Keyword Density ──
    all_matched = matched_required + matched_bonus
    density = get_keyword_density(text, all_matched)

    # ── Smart Suggestions ──
    suggestions = []
    if missing_required:
        suggestions.append({
            "type": "critical",
            "icon": "🚨",
            "title": "Add Missing Core Skills",
            "detail": f"You're missing {len(missing_required)} required skills: {', '.join(missing_required[:5])}{'...' if len(missing_required) > 5 else ''}."
        })
    if len(matched_bonus) < 3:
        missing_bonus = [s for s in good_to_have if s not in matched_bonus][:3]
        suggestions.append({
            "type": "improvement",
            "icon": "💡",
            "title": "Add Bonus Skills",
            "detail": f"Consider adding: {', '.join(missing_bonus)} to stand out."
        })
    if "projects" not in sections:
        suggestions.append({
            "type": "structure",
            "icon": "📁",
            "title": "Add a Projects Section",
            "detail": "Recruiters love seeing real projects. Add 2-3 projects with tech stack and outcomes."
        })
    if "certifications" not in sections:
        suggestions.append({
            "type": "structure",
            "icon": "🏅",
            "title": "Add Certifications",
            "detail": "Certifications from Coursera, Google, or AWS significantly boost credibility."
        })
    if len(text.split()) < 300:
        suggestions.append({
            "type": "warning",
            "icon": "⚠️",
            "title": "Resume Seems Too Short",
            "detail": "A strong resume should be at least 400-600 words. Expand your experience and projects sections."
        })
    if not extract_email(text):
        suggestions.append({
            "type": "critical",
            "icon": "📧",
            "title": "Missing Contact Email",
            "detail": "Make sure your email is clearly visible at the top of the resume."
        })

    return {
        "score":             total_score,
        "grade":             grade,
        "grade_label":       grade_label,
        "role_title":        role["title"],
        "matched_required":  matched_required,
        "missing_required":  missing_required,
        "matched_bonus":     matched_bonus,
        "other_skills":      other_skills[:10],
        "sections_found":    sections,
        "keyword_density":   density,
        "word_count":        len(text.split()),
        "suggestions":       suggestions,
        "stats": {
            "required_matched": len(matched_required),
            "required_total":   len(required),
            "bonus_matched":    len(matched_bonus),
            "bonus_total":      len(good_to_have),
        }
    }
