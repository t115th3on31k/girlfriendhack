# Web App

This is a web application built using the Django framework for the backend, PostgreSQL for the database, and Next.js for the front end. Below are the instructions to set up and deploy the web application.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)
- Node.js and npm (Node package manager)
- Docker and Docker Compose (for containerization and deployment)
- PostgreSQL database server

## Local Development Setup

1. Clone the repository to your local machine.

2. Navigate to the `web_app` directory.

3. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `web_app` directory with the following content, replacing the placeholders with your actual database credentials:

   ```
   DEBUG=True
   SECRET_KEY='your_secret_key'
   DATABASE_NAME='your_database_name'
   DATABASE_USER='your_database_user'
   DATABASE_PASSWORD='your_database_password'
   DATABASE_HOST='localhost'
   DATABASE_PORT='5432'
   ```

5. Run the Django migrations to set up your database schema:

   ```
   python manage.py migrate
   ```

6. Start the Django development server:

   ```
   python manage.py runserver
   ```

7. Navigate to the `web_app/frontend` directory and install the required Node.js dependencies:

   ```
   npm install
   ```

8. Build the Next.js application:

   ```
   npm run build
   ```

9. Start the Next.js server:

   ```
   npm start
   ```

10. The web application should now be running on `http://localhost:8000` for the Django backend and `http://localhost:3000` for the Next.js frontend.

## Docker Deployment

1. Ensure Docker and Docker Compose are installed on your system.

2. Build the Docker images:

   ```
   docker-compose build
   ```

3. Start the Docker containers:

   ```
   docker-compose up -d
   ```

4. The web application should now be accessible on `http://localhost`.

## Additional Information

- Static files are located in the `web_app/app/static` directory.
- Django templates are located in the `web_app/app/templates` directory.
- Next.js pages and components are located in the `web_app/frontend/pages` and `web_app/frontend/components` directories, respectively.
- To access the Django admin interface, create a superuser with the following command and follow the prompts:

   ```
   python manage.py createsuperuser
   ```

- Access the admin interface at `http://localhost:8000/admin`.

For more detailed information about the application structure and deployment, refer to the individual README files within the `web_app` and `web_app/frontend` directories.