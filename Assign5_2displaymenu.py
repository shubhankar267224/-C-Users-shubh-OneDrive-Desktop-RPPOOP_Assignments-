import tkinter as tk

# create the main window
root = tk.Tk()

# set the size of the window
root.geometry("500x250")

# create the menu bar
menu_bar = tk.Menu(root)

# create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# create an Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# create a Help menu with a submenu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu_sub = tk.Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Documentation")
help_menu_sub.add_command(label="About")
help_menu.add_cascade(label="Help", menu=help_menu_sub)

# add the File, Edit, and Help menus to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# display the menu bar
root.config(menu=menu_bar)

# start the main event loop
root.mainloop()
