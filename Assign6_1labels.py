import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("400x200")

# Create the first label with a red background and larger font size
label1 = tk.Label(root, text="Label 1", bg="red", fg="blue", font=("Arial", 20))
label1.pack()

# Create the second label with a blue background and larger font size
label2 = tk.Label(root, text="Label 2", bg="blue", fg="red", font=("Arial", 20))
label2.pack()

# Start the Tkinter event loop
root.mainloop()