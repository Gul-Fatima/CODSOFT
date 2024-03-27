from tkinter import *
import customtkinter as ct
import math

# Function to handle button clicks
def click(value):
    ex = entrybox.get()  # Get the current content of the entry box
    ans = ''  # Initialize the variable to store the result

    if value == 'del':
        ex = ex[:-1]  # Delete the last character from the entry
        entrybox.delete(0, END)  # Clear the entry box
        entrybox.insert(0, ex)  # Insert the modified string back into the entry box
        return
    elif value == '\u00F7':
        entrybox.insert(END, '/')  # Insert division symbol
        return
    elif value == 'C':
        entrybox.delete(0, END)  # Clear the entry box
    elif value == "=":
        ans = eval(ex)  # Evaluate the expression
    else:
        entrybox.insert(END, value)  # Insert the clicked button's value into the entry box
        return

    entrybox.delete(0, END)  # Clear the entry box
    entrybox.insert(0, ans)  # Insert the result into the entry box

# Create the main window
root = Tk()
root.geometry("345x320+200+100")
root.config(bg='teal')
root.title("Scientific Calculator")
root.resizable(0, 0)

# Creating entry box
entrybox = ct.CTkEntry(root,font=('arial', 20, 'bold'),width=325,bg_color='teal',height=40,fg_color='white',corner_radius=10)
entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')

# Button labels
button_text_list = ['C', 'del', '\u00F7', '%',
                    '7', '8', '9', '*',
                    '4', '5', '6', '-',
                    '1', '2', '3', '+',
                    '0', '.', '=']

# Initialize row and column values
rowvalue = 2
columnvalue = 0

# Create buttons
for index, i in enumerate(button_text_list):
    if index == len(button_text_list) - 1:
        columnspan_val = 2
    else:
        columnspan_val = 1

    # Create button with specified properties
    button = ct.CTkButton(root, text=i, fg_color="white", width=2, height=40, bg_color='teal',
                    font=('arial', 20, 'bold'), text_color='teal',
                    command=lambda button=i: click(button))
    
    # Position button in the grid
    button.grid(row=rowvalue, column=columnvalue, columnspan=columnspan_val, pady=2, padx=2, sticky='nsew')

    if columnvalue == 3:  # Check if it's the last button in the row
        rowvalue += 1
        columnvalue = 0
    else:
        columnvalue += 1

root.mainloop()  # Run the GUI
