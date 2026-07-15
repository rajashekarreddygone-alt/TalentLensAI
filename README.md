# 🎯 TalentLens AI

TalentLens AI is an AI-powered recruitment intelligence and career guidance platform designed to support both recruiters and job candidates.

The platform combines resume parsing, Natural Language Processing (NLP), semantic similarity, machine learning, candidate ranking, recruitment analytics, explainable recommendations, and AI-powered insights to provide a comprehensive recruitment decision-support system.

---

## 🚀 Project Overview

Traditional recruitment processes often involve manually reviewing large numbers of resumes and comparing candidate qualifications against job requirements. TalentLens AI demonstrates how Artificial Intelligence, Machine Learning, and Natural Language Processing can assist this process by providing structured and explainable candidate evaluations.

The platform provides two main perspectives:

- **Recruiter Dashboard** — Helps recruiters analyze, rank, filter, compare, shortlist, and manage candidates.
- **Candidate Dashboard** — Helps candidates evaluate their resume against a job description and receive personalized career guidance.

TalentLens AI is designed as a **decision-support system**. Final hiring decisions should remain with human recruiters and organizations.

---

## ✨ Key Features

### 👨‍💼 Recruiter Features

- 📄 **Resume Parsing** — Extract and analyze information from candidate resumes.
- 🎯 **Semantic Resume–Job Matching** — Evaluate alignment between resumes and job descriptions.
- ⭐ **Candidate Ranking** — Rank candidates using a recruiter-focused evaluation score.
- 🔍 **Advanced Search & Filtering** — Filter candidates based on score, recommendation, and required skills.
- 💡 **Explainable Recommendations** — Display candidate strengths, weaknesses, and areas for improvement.
- ⭐ **Shortlist Management** — Manage shortlisted candidates during the recruitment process.
- 📝 **Recruiter Notes & Status Tracking** — Record notes and track candidate recruitment status.
- ⚖️ **Candidate Comparison** — Compare candidates side-by-side using relevant evaluation criteria.
- 🤖 **AI Recruiter Assistant** — Ask questions about analyzed candidates and receive AI-powered insights.
- 📊 **Recruitment Analytics** — Visualize candidate scores, recommendations, strengths, and weaknesses.
- 📥 **Candidate Reports** — Generate downloadable candidate evaluation reports.

### 🎓 Candidate Features

- 📄 **Resume Analysis** — Upload and analyze a resume against a selected job description.
- 🎯 **Job Compatibility Scoring** — Measure resume-job alignment using a Job Compatibility Score.
- ✅ **Skill Match Analysis** — Identify skills matching the job requirements.
- ❌ **Missing Skill Detection** — Highlight important skills that may need improvement.
- 💼 **Application Recommendation** — Help candidates understand whether they should consider applying.
- 🤖 **AI Resume Analysis** — Generate AI-powered insights about resume-job alignment.
- 💡 **Resume Improvement Suggestions** — Provide personalized recommendations to strengthen the resume.
- 🎓 **AI Career Roadmap** — Recommend priority skills and a structured learning plan.
- 📚 **Learning Recommendations** — Suggest relevant learning areas and courses.
- 💻 **Project Recommendations** — Suggest practical projects for skill development.
- 🚀 **Career Opportunities** — Identify potential career paths based on the candidate profile.
- 🎯 **Interview Preparation** — Generate technical, behavioral, and HR interview questions.
- 📥 **Career Reports** — Generate a downloadable career analysis report.

---

## 📊 Evaluation Approach

TalentLens AI uses different evaluation perspectives for recruiters and candidates.

### Job Compatibility Score

The Candidate Dashboard calculates a Job Compatibility Score to estimate how well a candidate's resume aligns with a selected job description.

The evaluation considers factors such as:

- Skills
- Experience
- Education
- Keyword coverage
- Semantic similarity

### Recruiter Ranking Score

The Recruiter Dashboard uses a broader recruiter-focused evaluation approach to help compare and prioritize multiple candidates.

Because these scores serve different purposes, the **Job Compatibility Score** and **Recruiter Ranking Score** may differ for the same candidate.

---

## ⚙️ How TalentLens AI Works

### For Recruiters

1. Provide a job description.
2. Upload multiple candidate resumes.
3. TalentLens AI parses and analyzes the resumes.
4. Resume-job alignment and candidate evaluation scores are calculated.
5. Candidates can be ranked, searched, filtered, and compared.
6. Recruiters can review strengths, weaknesses, recommendations, and AI-generated insights.
7. Candidates can be shortlisted and managed through the recruitment workflow.

### For Candidates

1. Upload a resume.
2. Provide a target job description.
3. TalentLens AI analyzes resume-job compatibility.
4. Matched and missing skills are identified.
5. The platform provides an application recommendation.
6. AI-powered resume feedback and career guidance are generated.
7. Candidates receive learning recommendations, project ideas, career opportunities, and interview preparation questions.

---

## 🛠️ Technology Stack

TalentLens AI is built using:

- **Python** — Core application and backend logic
- **Streamlit** — Interactive web application and dashboard interface
- **Machine Learning & NLP** — Resume and job-description analysis
- **Sentence Transformers** — Semantic similarity and resume-job matching
- **spaCy** — Natural language processing and text analysis
- **Scikit-learn** — Machine learning and similarity-based evaluation
- **Plotly** — Interactive recruitment analytics and data visualization
- **Google Gemini API** — AI-powered recruitment and career guidance features

---

## 📁 Project Structure

```text
TalentLensAI/
│
├── .streamlit/
│   └── config.toml
│
├── app/
│   ├── components/
│   └── pages/
│
├── assets/
├── data/
├── models/
├── notebooks/
├── reports/
│
├── src/
│   └── ai/
│
├── tests/
│
├── main.py
├── pdf_generator.py
├── requirements.txt
├── .gitignore
└── README.md
```

> Note: Environment files, virtual environments, model files, API keys, and Streamlit secrets are excluded from version control where appropriate.

---

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rajashekarreddygone-alt/TalentLensAI.git
```

Navigate to the project directory:

```bash
cd TalentLensAI
```

### 2. Create a Virtual Environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Configuration

Some AI-powered features require an API key.

Create a `.env` file in the project root and configure the required environment variable according to the application's configuration.

Example:

```text
GEMINI_API_KEY=your_api_key_here
```

**Important:** Never commit API keys or the `.env` file to a public GitHub repository.

The project's `.gitignore` is configured to exclude `.env` files and Streamlit secrets.

---

## ▶️ Running the Application

After installing the dependencies and configuring the required environment variables, run:

```bash
streamlit run main.py
```

The application should open automatically in your browser.

If it does not open automatically, use the local URL displayed in the terminal.

---

## 🧪 Testing

The project contains test files for major components, including:

- Resume and job parsing
- Semantic similarity
- Job matching
- Candidate scoring
- Analysis and recommendation logic
- AI integration
- Processing pipeline

Tests can be executed using the appropriate Python or pytest commands depending on the test configuration.

For example:

```bash
pytest
```

---

## 📈 Application Modules

The application contains the following primary sections:

### 🏠 Home

Provides an introduction and overview of the TalentLens AI platform.

### 👨‍💼 Recruiter

Provides recruiter-focused candidate evaluation, ranking, filtering, comparison, shortlisting, AI assistance, and candidate management.

### 📊 Analytics

Provides recruitment analytics and visual insights into candidate evaluation results.

### 🎓 Candidate

Provides resume-job compatibility analysis, skill-gap identification, application recommendations, AI career guidance, resume improvement suggestions, and interview preparation.

### ℹ️ About

Explains the platform's features, evaluation approach, workflow, technology stack, and project objective.

---

## 🎯 Project Objective

The objective of TalentLens AI is to demonstrate how Artificial Intelligence, Machine Learning, Natural Language Processing, and semantic matching can be combined to create an intelligent recruitment support platform.

The system aims to improve transparency in candidate evaluation by providing explainable scores, strengths, weaknesses, skill-gap analysis, and recommendations rather than relying only on a single ranking value.

TalentLens AI is intended as a recruitment decision-support and career-guidance platform. Final hiring decisions should remain with human recruiters and organizations.

---

## ⚠️ Disclaimer

TalentLens AI is a project developed for educational and demonstration purposes.

AI-generated recommendations and candidate evaluation scores should be treated as decision-support information and should not be used as the sole basis for employment decisions. Human review and appropriate recruitment practices should always be maintained.

---

## 👨‍💻 Author

**Rajashekar Reddy Gone**

Machine Learning Intern

---

## 📌 Project Status

**Full Application Completed & Functional ✅**
