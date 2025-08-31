# ACEest Fitness and Gym 🏋️‍♂️

This is a web-based fitness and gym tracker application, built using **Flask** and containerized with **Docker**. The project features a complete **CI/CD pipeline** using **GitHub Actions** to automate the building and testing of the application.

-----

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD workflow
├── app.py                  # Core Flask application logic
├── test_app.py             # Pytest unit tests
├── Dockerfile              # Docker container definition
├── requirements.txt        # Python dependencies
└── README.md               # This setup guide
```

-----

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

### 1\. Version Control Setup (Git & GitHub)

First, you need to track your project files with Git and host them on GitHub.

Initialize Git: Open a terminal in your project folder (where app.py is located) and run:

git init
git branch -M main

Add and Commit Files: Add all the files we created to Git.

git add app.py test_app.py Dockerfile requirements.txt README.md
git commit -m "Initial commit: Add application, tests, and Docker config"

Create a GitHub Repository:

Go to GitHub and create a new repository. Do not initialize it with a README or .gitignore.

Copy the commands under "...or push an existing repository from the command line."

Push to GitHub: In your terminal, run the commands you copied. They will look like this:

git remote add origin [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)
git push -u origin main

Your code is now on GitHub!

### 2\. Understanding the Unit Tests (Pytest)

The file test_app.py contains unit tests for the application's logic. 

test_add_workout_success: Checks if a valid workout is added correctly.

test_add_workout_invalid_duration: Ensures the app rejects non-numeric duration values.

test_view_workouts_empty: Verifies the correct message is returned when no workouts are logged.

You can run these tests locally by running pytest in your terminal.

### 3\. Understanding Containerization (Docker)

The Dockerfile is a blueprint for creating a portable environment for our application.

FROM python:3.9-slim: Starts with a lightweight Python image.

RUN apt-get update && apt-get install -y tk-dev xvfb: Installs system packages. tk-dev is for Tkinter, and xvfb is a "virtual display" that lets us run GUI tests in a command-line environment.

COPY and RUN commands: These copy our code into the image and install the Python dependencies (pytest) listed in requirements.txt.

### 4\. Setting up the CI/CD Pipeline (GitHub Actions)

This is the automation step.

Create the Workflow Directory: In your project folder, create the necessary directories:

mkdir -p .github/workflows

Add the Workflow File: Move the main.yml file you downloaded into the .github/workflows/ directory.

Commit and Push the Workflow:

git add .github/workflows/main.yml
git commit -m "feat: Add CI/CD workflow for automated testing"
git push origin main

See it in Action:

Go to your repository on GitHub and click on the "Actions" tab.

You will see your workflow running. It is triggered automatically by the git push you just did.

The workflow will:

Check out your code.

Build the Docker image according to your Dockerfile.

Run the pytest command inside the container using xvfb-run to handle the GUI components.

CI/CD pipeline is implemented successfully