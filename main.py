import customtkinter as ctk

app = ctk.CTk()
app.geometry('500x500')

tabview = ctk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

# Adding tabs
Notes = tabview.add("Notes")
TODO = tabview.add("TODO")
Reminders = tabview.add("Reminders")

# Notes tab
label_1 = ctk.CTkLabel(master=tabview.tab("Notes"), text="Write your notes here.")
label_1.pack(padx=20, pady=20)

textbox_notes = ctk.CTkTextbox(master=tabview.tab("Notes"), activate_scrollbars=True, height=10)
textbox_notes.pack(padx=20, pady=20, fill='both', expand=True)

# To Do tab
label_2 = ctk.CTkLabel(master=tabview.tab("TODO"), text="Your To Do's:")
label_2.pack(padx=20, pady=5)

listbox_todo = ctk.CTkTextbox(master=tabview.tab("TODO"), activate_scrollbars=True, height=10, state="disabled")
listbox_todo.pack(padx=20, pady=10, fill='both', expand=True)


def add_todo():
    def save_todo():
        todo_item = entry.get()
        listbox_todo.configure(state="normal")
        listbox_todo.insert(ctk.END, todo_item + "\n")
        listbox_todo.configure(state="disabled")
        new_window.destroy()

    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x100")
    label = ctk.CTkLabel(new_window, text="Enter a new To Do:")
    label.pack()
    entry = ctk.CTkEntry(new_window)
    entry.pack()
    save_button = ctk.CTkButton(new_window, text="Save To Do", command=save_todo)
    save_button.pack()

button = ctk.CTkButton(master=tabview.tab("TODO"), text="Add To Do", command=add_todo)
button.pack(padx=20, pady=20)

# Reminders tab
label_3 = ctk.CTkLabel(master=tabview.tab("Reminders"), text="Your Reminders:")
label_3.pack(padx=20, pady=5)

listbox_reminders = ctk.CTkTextbox(master=tabview.tab("Reminders"), activate_scrollbars=True, height=10, state="disabled")
listbox_reminders.pack(padx=20, pady=10, fill='both', expand=True)

def add_reminder():
    def save_reminder():
        reminder_item = entry.get()
        listbox_reminders.configure(state="normal")
        listbox_reminders.insert(ctk.END, reminder_item + "\n")
        listbox_reminders.configure(state="disabled")
        new_window.destroy()

    new_window = ctk.CTkToplevel(app)
    new_window.geometry("300x100")
    label = ctk.CTkLabel(new_window, text="Enter a new Reminder:")
    label.pack()
    entry = ctk.CTkEntry(new_window)
    entry.pack()
    save_button = ctk.CTkButton(new_window, text="Save Reminder", command=save_reminder)
    save_button.pack()

button = ctk.CTkButton(master=tabview.tab("Reminders"), text="Add Reminder", command=add_reminder)
button.pack(padx=20, pady=20)

app.mainloop()
