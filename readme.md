# Password Strength Analyzer

A command-line tool built in Python that analyzes password strength, checks against real-world data breaches, generates secure passwords, and saves audit reports.

---

## 🔍 What It Does

- **Strength Analysis** — scores passwords from 0-100 based on length, complexity and patterns
- **Breach Detection** — checks if your password appears in known data breaches using the HaveIBeenPwned API
- **Password Generator** — generates cryptographically strong random passwords
- **Audit Reports** — saves all checks to a local report file for review
- **Detailed Feedback** — tells you exactly why a password is weak and how to fix it

---

## 🛠️ Built With

- Python 3.14
- [requests](https://pypi.org/project/requests/) — HaveIBeenPwned API calls
- [rich](https://pypi.org/project/rich/) — formatted CLI output
- [colorama](https://pypi.org/project/colorama/) — terminal colors
- [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3) — breach database

---

## 🔐 How Breach Detection Works

This tool uses the **k-Anonymity model** — your full password is never sent over the internet. Instead:
1. The password is hashed using SHA-1
2. Only the first 5 characters of the hash are sent to the API
3. The API returns all matching hashes
4. The tool checks locally if your full hash is in the results

This means your password stays completely private. ✅

---

## 🚀 Getting Started

### Requirements
- Windows 10/11
- Python 3.8+

### Installation

1. Clone the repository:
```
git clone https://github.com/DanEmmanuel1/password-strength-analyzer.git
cd password-strength-analyzer
```

2. Create and activate a virtual environment:
```
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

---

## 💻 Usage
```
py analyzer.py
```

Then choose from the menu:
```
1 — Analyze a password
2 — Generate strong passwords
3 — Exit
```

---

## 📊 Scoring System

| Score | Strength |
|-------|---------|
| 80-100 | Strong |
| 60-79 | Moderate |
| 40-59 | Weak |
| 0-39 | Very Weak |

---

## 📁 Project Structure
```
password-strength-analyzer/
├── analyzer.py       # Main entry point & scoring engine
├── checker.py        # HaveIBeenPwned breach detection
├── generator.py      # Strong password generator
├── reporter.py       # Audit report saving
└── requirements.txt  # Project dependencies
```

---

## ⚠️ Disclaimer

This tool is intended for personal use to improve your own password security. Never analyze passwords belonging to other people or systems without permission.

---

## 👤 Author

**DanEmmanuel1**
- GitHub: [@DanEmmanuel1](https://github.com/DanEmmanuel1)