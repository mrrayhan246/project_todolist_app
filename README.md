# To-Do List Application

![To-Do List](https://github.com/mrrayhan246/project_todolist_app/blob/main/to-do-lsit.png)

## Description
This is a simple To-Do List application built with Django. Users can add, complete, and delete tasks. Each task can have a title, description, due date, and priority level.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Contributing](#contributing)
5. [License](#license)
6. [Contact](#contact)

## Installation
Follow these steps to get the development environment running.

1. Clone the repository:
    ```sh
    git clone https://github.com/mrrayhan246/project_todolist_app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project_todolist_app
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Run migrations:
    ```sh
    python manage.py migrate
    ```
6. Start the development server:
    ```sh
    python manage.py runserver
    ```

## Usage
1. Navigate to `http://127.0.0.1:8000/` in your web browser.
2. You will see the To-Do List application interface.
3. Add tasks using the "Add Task" button.
4. Complete tasks by clicking the "Complete" button next to each task.
5. Delete tasks by clicking the "Delete" button next to each task.

## Features
- Add new tasks with a title, description, due date, and priority.
- Mark tasks as completed.
- Delete tasks.
- View overdue tasks.

## Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
Md. Raihanul Islam (Rayhan) - [mrrayhan246@gmail.com](mailto:mrrayhan246@gmail.com)

Project Link: [https://github.com/mrrayhan246/project_todolist_app](https://github.com/mrrayhan246/project_todolist_app)
