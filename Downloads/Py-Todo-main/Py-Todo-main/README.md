# Py-Todo

Professional-looking task manager built with Flask and a modern frontend (HTML/CSS/JS). Stores tasks in `data.json`.

## Features
- Add tasks with name, due date, due time, and priority (Low/Medium/High)
- Mark tasks as completed
- Delete tasks
- Overdue highlighting
- Live date & time display
- Priority-colored badges
- Dark / Light theme with localStorage
- Smooth animations and responsive design

## Files
- `web.py` — Flask backend
- `templates/index.html` — main HTML template
- `static/style.css` — styling and themes
- `static/script.js` — JS for theme, clock, and UX
- `data.json` — JSON task storage
- `requirements.txt` — Python deps

## Install & Run

1) Install dependencies (use a virtualenv):

```bash
python -m pip install -r requirements.txt
```

2) Run the app (development):

```bash
python web.py
```

Open `http://127.0.0.1:5000` in your browser. To view on mobile, run the app with `host='0.0.0.0'` (already set) and open `http://<PC_IP>:5000` on your phone.

## Notes for GitHub
- The UI is responsive and uses CSS variables for theme and color management.
- Storage is a simple `data.json` file with atomic writes.
- For production consider using a real database and serving static files via a web server.

Enjoy — feel free to fork and style further for your portfolio.

## Screenshots

You can include screenshots in this repository and show them in the README. Recommended path: create an `assets/` folder at the project root and place your images there.

Example steps (run in the project folder):

```bash
# create folder and copy your screenshot(s) into it (from your local machine)
mkdir -p assets
# e.g. copy Screenshot.png from your desktop to the repo
# (on Windows PowerShell)
copy C:\Users\You\Desktop\Screenshot.png .\assets\screenshot1.png

# add and commit
git add assets/screenshot1.png README.md
git commit -m "Add screenshot to README"

# push to GitHub (ensure remote 'origin' exists)
git push origin main
```

Add the following markdown into the README where you want the image to appear:

```markdown
## App Preview

![App screenshot](assets/screenshot1.png)

```

Notes
- If you already initialized the repo and set the remote (for example `https://github.com/Pal5060/Py-Todo.git`), pushing will upload the image file as part of the commit.
- Ensure your `.gitignore` does not exclude the `assets/` folder or image files.
- If you prefer uploading screenshots via GitHub's web UI, you can drag-and-drop images into the README editor; GitHub will upload them into the repo and give you an image URL to paste into the README.

If you want, I can:
- Add placeholder image files into `assets/` and update the README to reference them (you'll need to replace them with your real screenshots), or
- Provide the exact `git` commands adapted to your environment (PowerShell, Bash).