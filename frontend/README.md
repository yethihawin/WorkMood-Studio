# WorkMood Studio Frontend

A Streamlit frontend for WorkMood Studio that sends email and meeting transcript input to a backend API at `http://localhost:8000`.

## Setup

1. Create and activate a virtual environment.
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Run

```powershell
streamlit run streamlit_app.py
```

## Notes

- The app expects a backend service at `http://localhost:8000`.
- Change `BACKEND_URL` in `streamlit_app.py` if your API runs on a different host or port.
