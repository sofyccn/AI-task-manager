# AI-Powered Task Management App

A full-stack task management application with AI-powered features for intelligent task breakdown, natural language processing, and productivity analytics.

![Project Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![React](https://img.shields.io/badge/react-18+-blue)

## 🚀 Features

- ✅ **User Authentication**: Secure JWT-based authentication
- 🤖 **AI Task Breakdown**: Automatically split complex tasks into manageable subtasks
- 💬 **Natural Language Input**: Create tasks using conversational language
- 📊 **Productivity Analytics**: Visualize your progress with interactive charts
- 🔄 **Task Hierarchy**: Organize tasks with unlimited subtask nesting
- ⚡ **Real-time Updates**: Fast, responsive UI with optimistic updates

## 🛠️ Tech Stack

### Frontend
- **React** 18 with TypeScript
- **Tailwind CSS** for styling
- **Recharts** for data visualization
- **Axios** for API calls

### Backend
- **FastAPI** (Python) - Modern, fast web framework
- **SQLAlchemy** - Powerful ORM
- **PostgreSQL** - Robust relational database
- **JWT** - Secure authentication
- **OpenAI API** - AI-powered features

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- OpenAI API key (for AI features)

## 🏁 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/sofyccn/AI-task-manager.git
cd AI-task-manager
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL (see docs/setup.md for details)
# Create .env file with your credentials

# Initialize database
python init_db.py

# Run server
uvicorn main:app --reload
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Run development server
npm start
```
Frontend will run at: http://localhost:3000

## 📚 Documentation

- Complete Setup Guide - Detailed installation instructions
- Database Schema - Database design and relationships
- API Documentation - API endpoints (coming soon)
- Architecture Overview - System design (coming soon)

## 🎯 Project Goals

This project demonstrates:

F- ull-stack development with modern technologies
- RESTful API design and implementation
- Database design and relationships
- Authentication and authorization
- AI/LLM integration
- Frontend state management
- Deployment and DevOps practices

## 📸 Screenshots

Coming soon...

## 🚀 Deployment

Deployment guide coming soon...

## 🤝 Contributing

This is a portfolio project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 👤 Author

Sofia Cobo Navas

- GitHub: @sofyccn
- LinkedIn: [sofia-cobo](https://www.linkedin.com/in/sofia-cobo/)

## 🙏 Acknowledgments

Built as part of a full-stack development learning journey
Inspired by modern task management tools like Todoist and ClickUp
AI features powered by OpenAI