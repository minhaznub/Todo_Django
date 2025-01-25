# To-Do Application

This is a simple To-Do application built with Django. It allows users to add tasks to a list and displays the list below the form. The application also shows the name of the virtual machine where it is running.

## Features

- Add new tasks
- Display a list of tasks
- Show the virtual machine name

## Project Structure

```
todo_app/
├── manage.py
├── todo_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── tasks/
│       ├── task_list.html
│       └── task_form.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd todo_app
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your web browser and go to `http://127.0.0.1:8000/` to view the application.

## Usage

- Use the form to add new tasks.
- The list of tasks will be displayed below the form.
- The virtual machine name will be shown on the page.

## License

This project is licensed under the MIT License.