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
    *   **Real-time Clock**: Displays current date and time.
    *   **Reminders & Notifications**: Get timely browser notifications and audible alerts for overdue tasks.
*   **GUI Interface Highlights**:
    *   Simple and intuitive desktop application for quick task management.
*   **CLI Interface Highlights**:
    *   Fast and efficient task management directly from your terminal.

## Installation:

To get Py-Todo up and running on your system, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone <https://github.com/yourusername/Py-Todo.git> # Replace with your actual repository URL
    cd Py-Todo
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    The web interface requires Flask. Tkinter is usually included with Python.
    ```bash
    pip install Flask
    ```

## Usage:

All interfaces operate on the same `data.json` file, meaning tasks created or modified in one interface will be reflected in the others.

### 1. Command-Line Interface (CLI)

For quick task management in your terminal:

```bash
python cli.py
```
Follow the interactive menu to add, view, mark tasks as done, or delete them.

### 2. Graphical User Interface (GUI)

For a desktop application experience:

```bash
python gui.py
```
A Tkinter window will open, providing a visual way to manage your to-do list.

### 3. Web Interface

To access your tasks through a web browser:

```bash
python web.py
```
Once the server starts, open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure:

*   `tasks.py`: The core module containing functions for loading, saving, adding, updating, and deleting tasks. It manages the `data.json` file.
*   `cli.py`: The script for the command-line interface.
*   `gui.py`: The script for the Tkinter-based graphical user interface.
*   `web.py`: The Flask application that serves the web interface.
*   `data.json`: (Automatically created) The JSON file where all your tasks are stored.
*   `templates/`: Directory containing Jinja2 HTML templates for the web interface (e.g., `index.html`).
*   `static/`: Directory for static web assets.
    *   `static/style.css`: Stylesheets for the web interface.
    *   `static/script.js`: JavaScript for client-side interactivity, including AJAX, theme toggling, clock, and task reminders.

## Technologies Used:

*   **Python 3**: Core programming language.
*   **Flask**: Web framework for the web interface.
*   **Tkinter**: Standard Python GUI toolkit for the desktop application.
*   **HTML5, CSS3, JavaScript**: Frontend technologies for the web interface.
*   **JSON**: Data storage format.

## Contributing:

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to fork the repository and submit a pull request.

## License:

This project is open-source and distributed under the MIT License. See the `LICENSE` file (if present) for more details.
