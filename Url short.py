import pyshorteners
from tkinter import *

# Create the main window
win = Tk()
win.geometry("400x270")
win.configure(bg="White")
win.title("URL Shortener")

# Function to shorten the URL
def short():
    url = entry1.get()
    try:
        # Create a Shortener instance and shorten the URL
        s = pyshorteners.Shortener().tinyurl.short(url)
        # Clear the output field and insert the shortened URL
        entry2.delete(0, END)
        entry2.insert(END, s)
    except Exception as e:
        # Handle exceptions (e.g., invalid URL) by showing an error message
        entry2.delete(0, END)
        entry2.insert(END, "Error: Invalid URL")

# Label for user instruction
Label(win, text="Enter Your URL Link", font="Impact 17", bg="Black", fg="White").pack(fill=X, pady=10)

# Entry box for the long URL
entry1 = Entry(win, font=10, bd=3, width=40)
entry1.pack(pady=20)

# Button to trigger URL shortening
Button(win, text="Shorten URL", font="Impact 12", bg="Black", fg="White", width=14, command=short).pack(pady=10)

# Entry box to display the shortened URL
entry2 = Entry(win, font="Impact 16", width=35, bd=3)
entry2.pack(pady=30)

# Run the main event loop
win.mainloop()
