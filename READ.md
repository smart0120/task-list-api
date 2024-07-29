# FastAPI Task Management Application

This is a simple task management application built with FastAPI (Python) for the backend and React/TypeScript for the frontend.

## Prerequisites

- Python 3.7+
- Node.js 12+ and npm (for frontend)

## Backend Setup

### 1. Create a Virtual Environment

It's recommended to create a virtual environment to manage your dependencies.

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- On Linux/MacOS:
```bash
source venv/bin/activate
```

- On Windows:
```bash
source venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```bash
uvicorn main:app --reload
```