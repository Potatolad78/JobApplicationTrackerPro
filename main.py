from create_db import DB as DB
import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("Job Application Tracker")

# Create an instance of the DB class
db = DB()

# Function to open a new window to add a job application
def open_add_application_window():
    # Create a new window
    add_window = tk.Toplevel(root)
    add_window.title("Add Application")

    # Create labels and entry fields for each piece of data
    tk.Label(add_window, text="Company Name:").grid(row=0, column=0)
    company_name_entry = tk.Entry(add_window)
    company_name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Position:").grid(row=1, column=0)
    position_entry = tk.Entry(add_window)
    position_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Password:").grid(row=3, column=0)
    password_entry = tk.Entry(add_window)
    password_entry.grid(row=3, column=1)

    tk.Label(add_window, text="Interview Stage:").grid(row=4, column=0)
    interview_stage_entry = tk.Entry(add_window)
    interview_stage_entry.grid(row=4, column=1)

    tk.Label(add_window, text="Notes:").grid(row=5, column=0)
    notes_entry = tk.Entry(add_window)
    notes_entry.grid(row=5, column=1)

    # Function to handle the insertion of the application data
    def add_application():
        company_name = company_name_entry.get()
        position = position_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        interview_stage = interview_stage_entry.get()
        notes = notes_entry.get()

        db.insert_application(company_name, position, email, password, interview_stage, notes)
        add_window.destroy()  # Close the add application window after adding

        # Refresh the main window to show the new entry
        refresh_applications()

    # Create a button to submit the data
    tk.Button(add_window, text="Add Application", command=add_application).grid(row=6, column=0, columnspan=2)

# Function to display all applications in the main window
def refresh_applications():
    # Clear the current labels (if any)
    for widget in root.grid_slaves():
        widget.grid_forget()

    # Create labels for the column headers
    tk.Label(root, text="Company Name").grid(row=0, column=0)
    tk.Label(root, text="Position").grid(row=0, column=1)
    tk.Label(root, text="Email").grid(row=0, column=2)
    tk.Label(root, text="Password").grid(row=0, column=3)
    tk.Label(root, text="Interview Stage").grid(row=0, column=4)
    tk.Label(root, text="Notes").grid(row=0, column=5)

    # Fetch and display all applications
    applications = db.get_all_applications()
    for i, app in enumerate(applications, start=1):
        id, company_name, position, email, password, interview_stage, notes = app
        tk.Label(root, text=company_name).grid(row=i, column=0)
        tk.Label(root, text=position).grid(row=i, column=1)
        tk.Label(root, text=email).grid(row=i, column=2)
        tk.Label(root, text=password).grid(row=i, column=3)
        tk.Label(root, text=interview_stage).grid(row=i, column=4)
        tk.Label(root, text=notes).grid(row=i, column=5)

    # Add Application button
    tk.Button(root, text="Add Application", command=open_add_application_window).grid(row=i + 1, column=0, columnspan=6)
    #Add Manage Application Button
    tk.Button(root, text="Manage Applications", command=open_add_application_window).grid(row=i + 6, column=0, columnspan=6)

# Initial display of applications
refresh_applications()

# Start the tkinter event loop
root.mainloop()
