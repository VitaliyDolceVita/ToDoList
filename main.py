# Importing Tkinter for GUI
import tkinter as tk
from tkinter import messagebox


class ToDoList:
    def __init__(self):
        """Initialize the to-do list with an empty list of tasks."""
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append(task)

    def delete_task(self, index):
        """
        Delete a task from the to-do list by its index.
        Index is assumed to be 1-based for user friendliness.
        """
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            raise IndexError("Task index out of range")

class ToDoListUI:
    def __init__(self, todo_list):
        self.todo_list = todo_list
        self.root = tk.Tk()
        self.root.title("To Do List")

        # Task List Display
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        # Input Field for New Task
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(fill=tk.X)

        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(fill=tk.X)

        # Delete Task Button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(fill=tk.X)

        # Load existing tasks
        self.load_tasks()

    def load_tasks(self):
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.todo_list.delete_task(task_index + 1)
        except IndexError:
            messagebox.showerror("Error", "No task selected")

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    todo_list = ToDoList()
    ui = ToDoListUI(todo_list)
    ui.run()
