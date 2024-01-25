import tkinter as tk
from tkinter import scrolledtext

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.task_list = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_display = scrolledtext.ScrolledText(master, width=50, height=10)
        self.task_display.pack()

        self.mark_completed_button = tk.Button(master, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        # Implement logic to add a task to the list and update the display
        pass

    def mark_completed(self):
        # Implement logic to mark a task as completed and update the display
        pass

    def delete_task(self):
        # Implement logic to delete a task and update the display
        pass

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
