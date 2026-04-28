# Py-Todo: A Multi-Interface To-Do Application

Py-Todo is a versatile to-do list application that demonstrates a clean separation of concerns with a shared backend logic and multiple user interfaces:

1.  **Web Interface (Flask)**: A modern, responsive, and feature-rich web app.
2.  **Desktop GUI (Tkinter)**: A simple and functional native desktop application.
3.  **Command-Line Interface (CLI)**: A straightforward interface for terminal users.

## ✨ Features

### Web Interface
-   **Modern UI/UX**: Clean and intuitive design.
-   **AJAX-Powered**: Add, complete, and delete tasks without page reloads for a smooth experience.
-   **Animations**: Subtle animations for deleting and completing tasks.
-   **Light/Dark Theme**: Toggle between themes with local storage persistence.
-   **Real-time Clock**: Displays the current date and time.
-   **Task Metadata**: Add tasks with priority, due date, and due time.
-   **Smart Sorting**: Tasks are automatically sorted by completion status, overdue status, and priority.
-   **Browser Notifications & Reminders**: Get modal popups and browser notifications for due tasks.

### Core
-   **JSON Backend**: Tasks are stored in a simple `data.json` file.
-   **Unique IDs**: Each task is assigned a unique ID for robust management.
-   **Atomic Writes**: Ensures data integrity when saving tasks.

## 🚀 How to Run

### Prerequisites
-   Python 3.x
-   Flask (`pip install Flask`)

### 1. Running the Web Application

To start the web server, run the following command in your terminal:

```bash
python web.py
```

Then, open your web browser and navigate to `http://localhost:5000`.

### 2. Running the Desktop GUI

To launch the Tkinter-based desktop application, run:

```bash
python gui.py
```

### 3. Using the Command-Line Interface

To use the CLI version, run:

```bash
python cli.py
```

Follow the on-screen prompts to manage your tasks.
