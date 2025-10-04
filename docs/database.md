# Database Schema

Database design and relationships for the Task Manager application.

## Technologies

- **Database**: PostgreSQL 12+
- **ORM**: SQLAlchemy 2.0
- **Migrations**: SQLAlchemy Core (future: Alembic)

## Schema Overview

### Tables

1. **users** - User accounts and authentication
2. **tasks** - User tasks with hierarchy support
3. **ai_interactions** - History of AI-powered features

## Table Schemas

### users

Stores user account information and authentication credentials.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique user identifier |
| email | VARCHAR | UNIQUE, NOT NULL | User email address |
| password_hash | VARCHAR | NOT NULL | Bcrypt hashed password |
| created_at | TIMESTAMP | DEFAULT NOW() | Account creation timestamp |

**Indexes:**
- Primary key on `id`
- Unique index on `email`

**Relationships:**
- One-to-Many with `tasks` (one user has many tasks)
- One-to-Many with `ai_interactions`

---

### tasks

Stores user tasks with support for subtasks (hierarchical structure).

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique task identifier |
| title | VARCHAR | NOT NULL | Task title |
| description | TEXT | NULLABLE | Detailed task description |
| status | VARCHAR | DEFAULT 'todo' | Task status (todo, in_progress, done) |
| priority | VARCHAR | DEFAULT 'medium' | Priority level (low, medium, high) |
| user_id | INTEGER | FOREIGN KEY → users.id | Task owner |
| parent_task_id | INTEGER | FOREIGN KEY → tasks.id | Parent task (for subtasks) |
| created_at | TIMESTAMP | DEFAULT NOW() | Task creation timestamp |
| due_date | TIMESTAMP | NULLABLE | Optional due date |

**Indexes:**
- Primary key on `id`
- Foreign key on `user_id`
- Foreign key on `parent_task_id` (self-referencing)

**Relationships:**
- Many-to-One with `users` (many tasks belong to one user)
- Self-referencing: tasks can have subtasks

**Status Values:**
- `todo` - Not started
- `in_progress` - Currently working on
- `done` - Completed

**Priority Values:**
- `low` - Nice to have
- `medium` - Standard priority
- `high` - Urgent

---

### ai_interactions

Logs all AI-powered interactions for analytics and debugging.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Unique interaction identifier |
| user_id | INTEGER | FOREIGN KEY → users.id | User who made the request |
| prompt | TEXT | NOT NULL | User's input to AI |
| response | TEXT | NOT NULL | AI's response |
| created_at | TIMESTAMP | DEFAULT NOW() | Interaction timestamp |

**Indexes:**
- Primary key on `id`
- Foreign key on `user_id`

**Relationships:**
- Many-to-One with `users`

---

## Design Decisions

### Why PostgreSQL?

- **ACID compliance**: Ensures data consistency
- **Complex queries**: Efficient joins and aggregations
- **JSON support**: Can store flexible data when needed
- **Industry standard**: Used by major companies
- **Free and open-source**

### Why Self-Referencing for Subtasks?

Instead of a separate `subtasks` table, we use `parent_task_id`:

**Benefits:**
- ✅ Unlimited nesting depth
- ✅ Simpler queries
- ✅ Easy to move tasks around
- ✅ Cleaner data model

### Why Store AI Interactions?

- **Analytics**: Understand usage patterns
- **Debugging**: Investigate issues
- **Compliance**: Audit trail
- **Improvement**: Train better prompts

---

## Future Enhancements

- [ ] Add `tags` table for task categorization
- [ ] Add `task_history` for tracking changes
- [ ] Add `user_preferences` for customization
- [ ] Add full-text search indexes
- [ ] Implement soft deletes (deleted_at column)

## Database Migrations

Currently using SQLAlchemy's `create_all()` for development.

**Production TODO**: Implement Alembic for proper migrations:
```bash
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head