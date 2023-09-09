# Django Project Setup

This guide outlines the steps to set up a basic Django project. Follow these instructions to create a virtual environment, set up PostgreSQL using Docker, and run the Django server.

## Prerequisites

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/) (3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Getting Started

1. Clone the project repository:

   ```bash
   git clone <repository-url>
   cd <project-directory>
2. Create a virtual environment (optional but recommended):

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Setting up PostgreSQL with Docker
  
4. Create and start PostgreSQL containers using Docker Compose:

    ```bash
    docker-compose up -d
   ```
    This command will start PostgreSQL in a Docker container. Make sure to configure your Django project's settings to use the PostgreSQL database. Update the DATABASES settings in your Django project's settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ditto',
        'USER': 'ditto',
        'PASSWORD': 'ditto',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
5. Apply Django migrations to create the database tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a superuser to access the Django admin panel:`

    ```bash
    python manage.py createsuperuser
    ```
## Running the Django Server
7. Start the Django development server:

    ```bash
    python manage.py runserver
    ```
    The development server will be accessible at http://localhost:8000/.

8. Access the Django admin panel:

    1. Open a web browser and go to http://localhost:8000/admin/.
    2. Log in using the superuser credentials created earlier.
## Project Structure
1. The project code is organized in the standard Django structure.
2. Custom apps and views can be added as needed for your specific project requirements.