# Development Environment Setup

Complete guide to setting up the AI-Powered Task Manager development environment.

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- PostgreSQL 12 or higher
- Git

## Backend Setup

### 1. Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start
```

**Mac OS**
```bash
brew install postgresql
brew services start postgresql
```
### 2. Create Database and User

```bash
# Create PostgreSQL user
sudo -u postgres psql -c "CREATE USER taskapp_user WITH PASSWORD 'your_password';"

# Grant user permissions
sudo -u postgres psql -c "ALTER USER taskapp_user CREATEDB;"

# Create database
sudo -u postgres psql -c "CREATE DATABASE taskmanager_db OWNER taskapp_user;"

# Grant schema permissions
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE taskmanager_db TO taskapp_user;"
sudo -u postgres psql -d taskmanager_db -c "GRANT ALL ON SCHEMA public TO taskapp_user;"
sudo -u postgres psql -d taskmanager_db -c "GRANT CREATE ON SCHEMA public TO taskapp_user;"
```
### 3. Python Virtual Environment

``` bash
cd backend
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose[cryptography] passlib[bcrypt] python-dotenv
```

### 5. Configure Environment Variables

Create backend/.env:

```bash
DATABASE_URL=postgresql://taskapp_user:your_password@localhost/taskmanager_db
SECRET_KEY=generate-with-command-below
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Generate a secure SECRET_KEY:

```bash
python -c 'import secrets; print(secrets.token_urlsafe(32))'
```

### 6. Initialize Database Tables

```bash
python init_db.py
```

Verify tables were created:

```bash
psql -U taskapp_user -h localhost -d taskmanager_db -c "\dt"
```
You should see:

- users
- tasks
- ai_interactions

### 7. Run the Backend Server

```bash
uvicorn main:app --reload
```

Visit http://localhost:8000/docs to see the API documentation.

## Frontend Setup

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment Variables
Create frontend/.env:

```bash
REACT_APP_API_URL=http://localhost:8000
```

### 3. Run the Development Server

```bash
npm start
```

Visit http://localhost:3000

## Next Steps

- See ![Database Schema]() for database design details
- See ![API Documentation]() for API endpoints (coming soon)
