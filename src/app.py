"""
High School Management System API

A simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.

## Features

- View available extracurricular activities
- Sign up for activities
- Serve static frontend files
- Example endpoint for listing cities by country

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
   - Web app: [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

The app will reload automatically on code changes when using `--reload`.

## Project Structure

```
src/
  app.py           # Main FastAPI application
  static/
    index.html     # Frontend HTML
    app.js         # Frontend JavaScript
    styles.css     # Frontend CSS
requirements.txt   # Python dependencies
```

## Example API Endpoints

- `GET /activities` - List all activities
- `POST /activities/{activity_name}/signup?email=student@school.edu` - Sign up for an activity
- `GET /countries/{country}/cities` - List cities for a given country

---

This project is ready to run in a dev container with Python, Node.js, and Git
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

@app.get("/countries/{country}/cities")
def get_cities(country: str):
        """Return a list of cities for a given country/region"""
        country_cities = {
            "USA": ["New York", "Los Angeles", "Chicago", "Houston"],
            "UK": ["London", "Manchester", "Birmingham", "Liverpool"],
            "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary"],
            "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
            "Spain": ["Madrid", "Barcelona", "Valencia", "Seville"]
        }
        if country not in country_cities:
            raise HTTPException(status_code=404, detail="Country/region not found")
        return {"country": country, "cities": country_cities[country]}