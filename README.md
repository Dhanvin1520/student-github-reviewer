# 🐙 The Student GitHub & Portfolio Reviewer

An AI-powered tool designed to analyze a student's GitHub portfolio and provide personalized mentor-like feedback. It extracts data from a user's GitHub profile and leverages LangGraph and Groq to generate actionable insights on how to improve their portfolio, coding habits, and project presentations.

## 🚀 Architecture

The project is split into two main components:
- **Backend API (`FastAPI`)**: Uses LangGraph and LangChain to fetch GitHub data and orchestrate the LLM (Groq) to generate mentor feedback.
- **Frontend UI (`Streamlit`)**: A clean, interactive web interface where users can input a GitHub username and view the extracted statistics alongside the AI mentor's feedback.

## 🛠️ Tech Stack
- **Python 3.x**
- **FastAPI / Uvicorn** (Backend Routing & Server)
- **LangGraph & LangChain** (AI Agent Orchestration)
- **Groq** (LLM Provider)
- **Streamlit** (Frontend UI)

## 📦 Project Structure
```text
.
├── agent/                  # LangGraph agent definitions (nodes, state, graph logic)
├── ui/                     # Frontend Streamlit application
│   └── app.py              # The main Streamlit UI code
├── main.py                 # FastAPI backend entry point
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (API Keys, etc.)
```

## ⚙️ Local Setup & Installation

**1. Clone the repository and navigate into it**
```bash
git clone https://github.com/Dhanvin1520/student-github-reviewer.git
cd student-github-reviewer
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
Create a `.env` file in the root directory and add your Groq API key (and optionally a GitHub token if needed by the agent logic):
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 🏃 Running the Application

This application requires both the FastAPI backend and the Streamlit frontend to be running simultaneously.

**Step 1: Start the FastAPI Backend**
In a new terminal window, run the following command to start the API:
```bash
uvicorn main:app --reload
```
The backend will be available at `http://127.0.0.1:8000`.

**Step 2: Start the Streamlit UI**
Open a second terminal window (ensure your virtual environment is activated) and run:
```bash
streamlit run ui/app.py
```
This will open the web interface in your default browser at `http://localhost:8501`.

## ☁️ Deployment

- **Backend**: Can be hosted easily on platforms like Render, Heroku, or Railway as a standard Python Web Service running Uvicorn.
- **Frontend**: The Streamlit application can be hosted for free natively on **Streamlit Community Cloud** or Hugging Face Spaces.
