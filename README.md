# Smart Feedback Assistant – Backend

This is the FastAPI backend for the Smart Feedback Assistant app.  
It accepts raw performance feedback, uses OpenAI to generate polished summaries, and stores them in a PostgreSQL database.

---

## 🛠️ Stack

- FastAPI (Python 3)
- OpenAI API
- PostgreSQL
- SQLAlchemy
- dotenv for config

---

## 📁 Project Structure

<pre> smart-feedback-backend/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── database.py
│   └── schemas.py
├── requirements.txt
├── .env 
├── .gitignore
├── README.md
 </pre>

---

## 🔧 Setup

### 1. Create `.env` file
<pre>```ini
DATABASE_URL=postgresql://user:password@localhost:5432/yourdb
OPENAI_API_KEY=sk-...
</pre>

### 2. Install requirements:
<pre>```bash
pip install -r requirements.txt
</pre>

### 3. Run the app
<pre>uvicorn app.main:app --reload
</pre>

📄 License

MIT
