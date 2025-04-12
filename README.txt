# Study Planner App - Full Version

## 🔧 How to Set Up (Windows + VS Code)

1. **Extract this ZIP** into: C:\Users\<YourName>\Documents\study_planner_app_full
2. **Open in VS Code**
   - File > Open Folder > Select 'study_planner_app_full'
3. **Open Terminal in VS Code**
   - Terminal > New Terminal

## 🐍 Create & Activate Virtual Environment

```powershell
python -m venv venv
.env\Scriptsctivate
```

If script error occurs:
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

## 📦 Install Requirements

```powershell
pip install -r requirements.txt
```

## 🧾 Register New User

```powershell
python -m streamlit run signup.py
```

## 🚀 Launch Dashboard

```powershell
python -m streamlit run app.py
```

## ✅ Features Included

- Login/Signup with roles (Student/Admin)
- Task management with deadlines
- Personalized plans for:
  - Competitive exams
  - College or school syllabus
- Weekly email reminders
- Export schedule to PDF
- Google Calendar integration

