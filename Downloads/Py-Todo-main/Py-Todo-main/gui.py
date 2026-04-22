import tkinter as tk
from tkinter import messagebox
from tasks import load_tasks, add_task, delete_task, mark_done


class TodoGUI:
    def __init__(self, root):
        self.root = root
        root.title('To-Do Manager')
        root.geometry('400x450')

        self.frame = tk.Frame(root, padx=12, pady=12)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.frame, font=('Arial', 12))
        self.entry.pack(fill=tk.X, pady=(0, 8))

        btn_frame = tk.Frame(self.frame)
        btn_frame.pack(fill=tk.X, pady=(0, 8))

        self.add_btn = tk.Button(btn_frame, text='Add Task', command=self.add_task, bg='#4CAF50', fg='white')
        self.add_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 4))

        self.mark_btn = tk.Button(btn_frame, text='Mark as Done', command=self.mark_task, bg='#2196F3', fg='white')
        self.mark_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=4)

        self.del_btn = tk.Button(btn_frame, text='Delete Task', command=self.delete_task, bg='#f44336', fg='white')
        self.del_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(4, 0))

        self.listbox = tk.Listbox(self.frame, font=('Arial', 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for t in load_tasks():
            mark = '✔ ' if t.get('done') else ''
            self.listbox.insert(tk.END, f"{mark}{t.get('name')}")

    def add_task(self):
        name = self.entry.get().strip()
        if not name:
            messagebox.showinfo('Info', 'Please enter a task name')
            return
        add_task(name)
        self.entry.delete(0, tk.END)
        self.refresh()

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo('Info', 'Select a task to delete')
            return
        index = sel[0]
        delete_task(index)
        self.refresh()

    def mark_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo('Info', 'Select a task to mark')
            return
        index = sel[0]
        mark_done(index)
        self.refresh()


if __name__ == '__main__':
    root = tk.Tk()
    app = TodoGUI(root)
    root.mainloop()
