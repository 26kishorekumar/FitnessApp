import pytest
import tkinter as tk
from app import FitnessTrackerApp

# Fixture to create a new app instance for each test function
# This ensures each test runs in a clean, isolated environment.
@pytest.fixture
def app():
    """
    Creates a Tkinter root window and a FitnessTrackerApp instance for testing.
    The window is withdrawn to prevent it from appearing during the test run.
    """
    root = tk.Tk()
    root.withdraw() 
    fitness_app = FitnessTrackerApp(root)
    # Yield the app instance to the test function
    yield fitness_app 
    # Teardown: destroy the root window after the test is done
    root.destroy()

# --- Tests for the core logic of adding a workout ---

def test_add_workout_success(app):
    """Tests that a valid workout is added successfully."""
    status, message = app.add_workout_logic("Running", "30")
    assert status == "success"
    assert message == "'Running' added successfully!"
    assert len(app.workouts) == 1
    assert app.workouts[0] == {"workout": "Running", "duration": 30}

# Use pytest.mark.parametrize to test all error cases with a single function.
@pytest.mark.parametrize("workout, duration, expected_message", [
    ("", "30", "Please enter both workout and duration."),
    ("Weights", "", "Please enter both workout and duration."),
    ("Yoga", "abc", "Duration must be a number."),
    ("Swimming", "-10", "Duration must be a positive number.")
])
def test_add_workout_error_cases(app, workout, duration, expected_message):
    """Tests various invalid inputs for adding a workout."""
    status, message = app.add_workout_logic(workout, duration)
    assert status == "error"
    assert message == expected_message
    # Ensure no workouts were added to the list in any of the error cases.
    assert len(app.workouts) == 0

# --- Tests for the workout summary functionality ---

def test_view_workouts_empty(app):
    """Tests that the correct message is returned when no workouts are logged."""
    summary = app.get_workout_summary()
    assert summary == "No workouts logged yet."

def test_view_workouts_with_data(app):
    """Tests that a correctly formatted summary is returned after adding workouts."""
    app.add_workout_logic("Cycling", "45")
    app.add_workout_logic("Push-ups", "15")
    summary = app.get_workout_summary()
    expected_summary = "Logged Workouts:\n1. Cycling - 45 minutes\n2. Push-ups - 15 minutes"
    assert summary == expected_summary
