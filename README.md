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
├── .env              # SHOULD NOT be committed
├── .gitignore
├── README.md
 </pre>

---

## 🔧 Setup

### 1. Create `.env` file
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/yourdb
OPENAI_API_KEY=sk-...


### 2. Install requirements:
```bash
pip install -r requirements.txt


### 3. Run the app
uvicorn app.main:app --reload


📄 License

MIT