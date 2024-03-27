from tkinter import *
import math

def click(value):
    ex = entrybox.get()
    ans = ''

    if value == 'del':
        ex = ex[:-1]  
        entrybox.delete(0, END)
        entrybox.insert(0, ex)
        return  
    elif value == '\u00F7':
        entrybox.insert(END,'/')
        return

    elif value =='C':
        entrybox.delete(0, END)
    elif value == "=":
        ans = eval(ex)
    else:
        entrybox.insert(END, value)
        return

    entrybox.delete(0, END)
    entrybox.insert(0, ans)



root = Tk()
root.geometry("345x390+200+100")
root.config(bg='teal')
root.title("Scientific Calculator")
root.resizable(0,0)

# Creating entry box
entrybox = Entry(root, font=('arial', 20, 'bold'), bg="white", fg="black", bd=10)
entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky='nsew')
# Creating buttons
button_text_list = ['C','del','\u00F7','%'
                    ,'7','8', '9', '*',
                    '4','5','6','-',
                    '1','2','3','+',
                    '0','.','=']

rowvalue = 2
columnvalue = 0

for index, i in enumerate(button_text_list):
    if index == len(button_text_list) - 1:
        columnspan_val = 2
    else:
        columnspan_val = 1

    button = Button(root, text=i, fg="teal", width=2, height=2, bd=2, bg='white', relief=RAISED, font=('arial', 12, 'bold'),
                    activebackground='teal', justify=RIGHT, command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, columnspan=columnspan_val, pady=2, padx=2, sticky='nsew')

    if columnvalue == 3:  # Check if it's the last button in the row
        rowvalue += 1
        columnvalue = 0
    else:
        columnvalue += 1

root.mainloop()
