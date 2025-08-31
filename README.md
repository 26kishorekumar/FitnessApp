# ACEest Fitness and Gym 🏋️‍♂️

This is a web-based fitness and gym tracker application, built using **Flask** and containerized with **Docker**. The project features a complete **CI/CD pipeline** using **GitHub Actions** to automate the building and testing of the application.

-----

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions CI/CD workflow
├── templates/
│   └── index.html          # HTML template for the frontend
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

First, you'll need to get the project on GitHub to use GitHub Actions.

  * **Initialize a Git repository**:

    ```bash
    git init
    git add .
    git commit -m "Initial commit: Add Flask app and project files"
    ```

  * **Create a GitHub Repository**: Go to GitHub and create a new repository. **Do not** initialize it with a README or `.gitignore` file.

  * **Link Local to Remote**: Follow the instructions provided by GitHub to link your local repository. The commands will look similar to this:

    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    git branch -M main
    git push -u origin main
    ```

Your code is now on GitHub, and the CI/CD pipeline will be active.

-----

### 2\. Running the Application Locally

For development, you can run the application directly on your machine.

  * **Set up a Virtual Environment**:

    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

  * **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

  * **Run the Flask App**:

    ```bash
    flask run
    ```

Open your web browser and go to `http://127.0.0.1:5000` to see the application.

-----

### 3\. Running Unit Tests Locally

Validate your changes before pushing them to GitHub.

```bash
pytest
```

-----

### 4\. Building and Running with Docker

This simulates the production environment and how the application will run in the CI/CD pipeline. Make sure you have Docker Desktop installed and running.

  * **Build the Docker Image**:

    ```bash
    docker build -t flask-fitness-app .
    ```

  * **Run the Docker Container**:

    ```bash
    docker run -p 5000:5000 flask-fitness-app
    ```

The application will be accessible in your browser at `http://127.0.0.1:5000`.

-----

### 5\. CI/CD Pipeline with GitHub Actions ⚙️

The automated pipeline is defined in the `.github/workflows/main.yml` file.

  * **Trigger**: The pipeline automatically runs every time you `git push` code to the **`main`** branch.
  * **Process**: It checks out your code, builds a **Docker image**, and then runs the **`pytest`** command inside the new container. This ensures that the application not only builds successfully but also works correctly within its containerized environment.
  * **Monitoring**: You can check the status and logs of each run in the **"Actions"** tab of your GitHub repository. A green checkmark means everything passed\!