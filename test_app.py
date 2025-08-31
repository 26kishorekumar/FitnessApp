import pytest
import tkinter as tk
from app import FitnessTrackerApp

# Fixture to create a new app instance for each test function
@pytest.fixture
def app():
    """Creates a Tkinter root window and an instance of the app."""
    # We need a root window for the app to initialize, even if we don't show it.
    root = tk.Tk()
    # Withdraw the window so it doesn't appear during tests
    root.withdraw() 
    fitness_app = FitnessTrackerApp(root)
    # Yield the app instance to the test
    yield fitness_app 
    # Teardown: destroy the root window after the test is done
    root.destroy()

# --- Tests for add_workout_logic ---

def test_add_workout_success(app):
    """Test successful addition of a workout."""
    status, message = app.add_workout_logic("Running", "30")
    assert status == "success"
    assert message == "'Running' added successfully!"
    assert len(app.workouts) == 1
    assert app.workouts[0] == {"workout": "Running", "duration": 30}

def test_add_workout_no_name(app):
    """Test adding a workout with no name."""
    status, message = app.add_workout_logic("", "30")
    assert status == "error"
    assert message == "Please enter both workout and duration."
    assert len(app.workouts) == 0

def test_add_workout_no_duration(app):
    """Test adding a workout with no duration."""
    status, message = app.add_workout_logic("Weights", "")
    assert status == "error"
    assert message == "Please enter both workout and duration."
    assert len(app.workouts) == 0

def test_add_workout_invalid_duration(app):
    """Test adding a workout with a non-numeric duration."""
    status, message = app.add_workout_logic("Yoga", "abc")
    assert status == "error"
    assert message == "Duration must be a number."
    assert len(app.workouts) == 0

def test_add_workout_negative_duration(app):
    """Test adding a workout with a negative duration."""
    status, message = app.add_workout_logic("Swimming", "-10")
    assert status == "error"
    assert message == "Duration must be a positive number."
    assert len(app.workouts) == 0

# --- Tests for get_workout_summary ---

def test_view_workouts_empty(app):
    """Test viewing workouts when none have been added."""
    summary = app.get_workout_summary()
    assert summary == "No workouts logged yet."

def test_view_workouts_with_data(app):
    """Test viewing workouts after adding some."""
    app.add_workout_logic("Cycling", "45")
    app.add_workout_logic("Push-ups", "15")
    summary = app.get_workout_summary()
    expected_summary = "Logged Workouts:\n1. Cycling - 45 minutes\n2. Push-ups - 15 minutes"
    assert summary == expected_summary