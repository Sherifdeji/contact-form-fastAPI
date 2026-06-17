# Contact Form API

A lightweight FastAPI application demonstrating `POST` requests, Pydantic data validation, and JSON responses.

## Quick Start

```bash
# 1. Setup environment
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
uvicorn main:app --reload
```

## API Docs

Once running, view the interactive auto-generated documentation at:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## Endpoints

- **`GET /`** - Health check.
- **`POST /contact`** - Submit a contact message.
  - **Payload Rules:**
    - `name` (str): Required
    - `email` (str): Required, valid email format
    - `message` (str): Required, min length 10
    - `subject` (str): Optional, defaults to "General Inquiry"
