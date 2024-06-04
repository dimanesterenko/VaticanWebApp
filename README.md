# VaticanWebApp

A brief description of what your project does.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [API Documentation](#api-documentation)
- [Running Tests](#running-tests)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Feature 1
- Feature 2
- Feature 3

## Prerequisites

- Python 3.8+
- Django 4.0+
- PostgreSQL 

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dimanesterenko/VaticanWebApp.git
    cd Back
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    Edit the `DATABASES` setting in `Back/settings.py` to match your database configuration.

    Apply the migrations:

    ```sh
    python manage.py migrate
    ```

5. **Create a `.env` file for environment variables:**

    ```sh
    cp .env.example .env
    ```

    Edit the `.env` file to include your settings (e.g., `SECRET_KEY`, `DATABASE_URL`).

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

## Running the Project

1. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/`.


python manage.py test
