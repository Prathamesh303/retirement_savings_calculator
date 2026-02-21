# Retirement Savings Calculator

A FastAPI-based REST API for managing retirement savings with transaction validation, returns calculation.

## Prerequisites

- Python 3.12+
- pip

## Installation

```bash
# Clone and setup
git clone <repository-url>
cd retirement_savings_calculator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Development (with auto-reload)
uvicorn app.main:app --host 0.0.0.0 --port 5477 --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 5477
```

Application runs at: `http://localhost:5477`

## API Documentation

Access the interactive API docs at: `http://localhost:5477/docs`

## Project Structure

```
app/
├── main.py                 # FastAPI app entry point
├── api/v1/
│   ├── router.py          # Routes configuration
│   └── endpoints/         # API endpoints
│       ├── transactions.py
│       ├── returns.py
│       └── performance.py
├── services/              # Business logic
├── middleware/            # Metrics middleware
└── models/               # Data models
```

## API Endpoints (v1)

- `POST /api/v1/transactions/*` - Transaction validation and filtering
- `POST /api/v1/returns/*` - Returns calculation
- `POST /api/v1/performance/*` - Performance analysis

## Docker

```bash
# Build
docker build -t retirement-savings-calculator .

# Run
docker run -p 5477:5477 retirement-savings-calculator
```

## Dependencies

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **psutil** - System metrics