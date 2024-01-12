# Flask PostgreSQL Student Registration

This project is a simple Flask web application that allows users to register students with their first name, last name, and pet name into a PostgreSQL database.

## Features

- User-friendly web interface for student registration.
- Storage of student information in a PostgreSQL database.
- Validation of form inputs before submission.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.11 or higher.
- You have installed PostgreSQL on your local machine or have access to a PostgreSQL server.
- You have a PostgreSQL user with the necessary permissions to create databases and tables.

## Installation

To install the Flask PostgreSQL Student Registration project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Ollie345/Flask-postgres-connect.git
```

2. Navigate to the project directory:

```bash
cd Flask postgres
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```
4. Make sure to  download Pgadmin4
   - navigate to your pgadmin4 then input your password
   - right click on database and click on create
   - click on database option and input the name 'students' for the database

## Configuration

Configure the database connection by setting the `SQLALCHEMY_DATABASE_URI` in `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
```

Replace `username`, `password`, and `database_name` with your PostgreSQL credentials and the name of your database.

## Running the Application

To run the Flask PostgreSQL Student Registration application, execute the following command:

```bash
python app.py
```

The application will start on `http://localhost:5000/` by default.

## Usage

Navigate to `http://localhost:5000/` in your web browser to access the student registration form. Fill in the student's first name, last name, and pet name, then click the submit button to register the student.

## Contributing

To contribute to the Flask PostgreSQL Student Registration project, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).
"# Flask-postgres-connect" 
