# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

### Prerequisites

- Python 3.8 or newer
- `pip` package manager

### Installation

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Start the FastAPI server:
   ```sh
   uvicorn src.app:app --reload
   ```

3. Open your browser and navigate to:
   - Web app: http://localhost:8000/static/index.html
   - API docs: http://localhost:8000/docs

The app will reload automatically on code changes when using `--reload`.

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.
