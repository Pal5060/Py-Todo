# Py-Todo: A Versatile To-Do Manager

Py-Todo is a simple yet powerful To-Do list application designed to help you manage your tasks efficiently. It offers multiple interfaces to suit your workflow: a Command-Line Interface (CLI), a Graphical User Interface (GUI) built with Tkinter, and a modern Web Interface powered by Flask. All interfaces share the same underlying data, ensuring a consistent task list across platforms.

## Key Features:

*   **Multi-Platform Access**: Manage your tasks via CLI, a desktop GUI, or a web browser.
*   **Persistent Storage**: Tasks are automatically saved to `data.json`, so your data is safe and available across sessions.
*   **Comprehensive Task Details**: Each task can have a name, due date, due time, and a priority level (High, Medium, Low).
*   **Web Interface Highlights**:
    *   **Dynamic Updates**: Add, mark as done, and delete tasks seamlessly with AJAX.
    *   **Smart Sorting**: Tasks are intelligently sorted by completion status, overdue status, and priority.
    *   **Theme Toggle**: Switch between light and dark themes for comfortable viewing.
    *   **Like Feature**: Users can "like" tasks, with the count persisting across sessions.
    *   **Real-time Clock**: Displays current date and time.
    *   **Reminders & Notifications**: Get timely browser notifications and audible alerts for overdue tasks.
*   **GUI Interface Highlights**:
    *   Simple and intuitive desktop application for quick task management.
*   **CLI Interface Highlights**:
    *   Fast and efficient task management directly from your terminal.

## Setup and Installation

To get the Py-Todo application running on your local machine, follow these steps:

1.  **Prerequisites**:
    *   Ensure you have Python (version 3.6 or higher recommended) installed. You can download it from [python.org](https://www.python.org/downloads/).
    *   `pip` (Python's package installer) should be included with your Python installation.

2.  **Clone the Repository (if you haven't already):**
    ```bash
    git clone https://github.com/your-username/Py-Todo.git
    cd Py-Todo
    ```
    (Replace `your-username` with your GitHub username if you're cloning your own repo).

3.  **Install Dependencies**:
    The web interface requires Flask. Install it using pip:
    ```bash
    pip install Flask
    ```
    Tkinter, used for the GUI, is typically included with standard Python installations.

## How to Run the Application

All three interfaces (CLI, GUI, Web) share the same backend logic (`tasks.py`) and data storage (`data.json`). Any changes made in one interface will be reflected in the others.

### 1. Command-Line Interface (CLI)

To run the CLI version:
```bash
python cli.py
```
Follow the on-screen menu to interact with your tasks.

### 2. Graphical User Interface (GUI)

To run the GUI version:
```bash
python gui.py
```
A desktop window will appear, allowing you to manage tasks.

### 3. Web Interface

To run the web application:
```bash
python web.py
```
The terminal will display a URL (e.g., `http://127.0.0.1:5000/`). Open this URL in your web browser to access the web interface.

### Data Storage

Your tasks are stored persistently in a file named `data.json` in the project's root directory. If this file doesn't exist, it will be created automatically when you add your first task. You can inspect this file to see the raw task data.
