# python

# Django List Management Project

A simple Django-based list management application where users can register, log in, and manage personal lists and items. The project uses MySQL as the database backend.

## Features

- User registration and login
- Create, read, update, and delete (CRUD) operations for lists and items
- MySQL database integration

## Technologies Used

- **Django** - Web framework
- **MySQL** - Database backend

## Prerequisites

- Python (version 3.6+ recommended)
- MySQL
- pip
- Virtual environment

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:vinda-halarnkar/python.git
cd task_manager
```

### If you have virtualenv installed
```bash
virtualenv venv
```

# Activate your virtual environment
```bash
source venv/bin/activate
```

# Install Dependencies
```bash
pip install -r requirements.txt
```

# Setup environment variables
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
```

# Create migrations
```bash
python manage.py makemigrations
```

# Apply migrations
```bash
python manage.py migrate
```

# Run the Development Server
```bash
python manage.py runserver
```




