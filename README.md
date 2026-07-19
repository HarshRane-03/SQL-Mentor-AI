# 🤖 SQL Mentor AI

SQL Mentor AI is an intelligent, interactive web application designed to help developers, data analysts, and students master SQL. By leveraging the power of Generative AI, the application acts as a personal mentor—explaining complex queries, fixing syntax errors, optimizing slow-performing code, and generating optimized SQL statements from natural language.

Whether you are looking to debug a broken `JOIN` or learn how to write advanced window functions, SQL Mentor AI breaks down the logic in an easy-to-understand, step-by-step format.

---

## 🚀 Key Features

*   **Natural Language to SQL:** Write what data you want in plain English, and get a syntactically correct, optimized SQL query.
*   **Query Explainer:** Paste any complex SQL query to get an inline, human-readable breakdown of what the code does.
*   **Error Debugger & Fixer:** Input a failing query along with the database error message, and the AI will pinpoint the bug and provide the corrected script.
*   **Performance Optimization:** Analyzes your queries to suggest index improvements, structural rewrites, and performance tuning tips.
*   **Database Dialect Selection:** Supports multiple SQL flavors including PostgreSQL, MySQL, SQLite, and SQL Server.

---

## 🛠️ Tech Stack

*   **Frontend & UI:** Streamlit (Python-based interactive web framework)
*   **LLM Orchestration:** Google Gemini API (or OpenAI API / LangChain depending on your choice)
*   **Language:** Python 3.9+
*   **Environment Management:** Dotenv (`.env` for secure API key handling)

---

## 💻 Local Setup & Installation

Follow these steps to get your own instance of SQL Mentor AI running locally on your machine.

### Prerequisites

Make sure you have the following installed:
*   [Python 3.9 or higher](https://www.python.org/downloads/)
*   A Git client

### Step 1: Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/HarshRane-03/SQL-Mentor-AI.git](https://github.com/HarshRane-03/SQL-Mentor-AI.git)
cd SQL-Mentor-AI
```
### Step 2: Create a Virtual Environment (Recommended)
Isolate your project dependencies by setting up a virtual environment:
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
source venv/bin/activate

### Step 3: Install Dependencies
Install all the required Python libraries using the requirements.txt file:
pip install -r requirements.txt

### Step 4: Configure Environment Variables
The application requires an API key to communicate with the AI model.
Create a new file named .env in the root directory of the project.
Add your API key into the file like this:

GEMINI_API_KEY=your_actual_api_key_here
# Note: If you used OpenAI, name it OPENAI_API_KEY=your_key

### Step 5: Launch the Application
Start the Streamlit server using:
streamlit run app.py

Once running, the terminal will provide a local URL (usually http://localhost:8501). Open this link in your web browser to start using SQL Mentor AI!

