import tkinter as tk
from tkinter import simpledialog


class ToDoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('To Do App')
        self.window.geometry('300x450')

        # Create frames for each category view
        self.todo_frame = self.create_frame('To Do')
        self.reminder_frame = self.create_frame('Reminders')
        self.note_frame = self.create_frame('Notes')

        # Create buttons to navigate between frames
        self.create_nav_button('To Do', self.todo_frame)
        self.create_nav_button('Reminders', self.reminder_frame)
        self.create_nav_button('Notes', self.note_frame)

        # Show initial frame
        self.show_frame(self.todo_frame)

    def create_frame(self, title):
        frame = tk.Frame(self.window)
        tk.Label(frame, text=title).pack()
        text_area = tk.Text(frame, height=10, width=15)
        text_area.pack()
        button = tk.Button(frame, text=f'Add {title}', command=lambda: self.add_item(text_area))
        button.pack()

        return frame

    def create_nav_button(self, text, frame):
        button = tk.Button(self.window, text=text, command=lambda: self.show_frame(frame))
        button.pack(side='left')

    def show_frame(self, frame):
        # Hide all frames
        self.todo_frame.pack_forget()
        self.reminder_frame.pack_forget()
        self.note_frame.pack_forget()
        # Show the target frame
        frame.pack()

    def add_item(self, text_area):
        item = simpledialog.askstring('New Item', 'Enter the item:')
        if item:
            text_area.insert(tk.END, f'\n{item}')

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    app = ToDoApp()
    app.run()