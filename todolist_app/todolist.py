from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import datetime

tasks_list = []

def on_enter(event):
    """Function to handle the Enter key event."""
    quote_text = quote_entry.get()
    display_quote(quote_text)

def display_quote(quote_text):
    """Function to display the entered quote in a frame."""
    quote_label.config(text=quote_text)


def deltask():
    global tasks_list
    task = str(selected_task.get())
    if task in tasks_list:
        tasks_list.remove(task)
        with open('todo/taskfile.txt','w') as tf:
            for task in tasks_list:
                tf.write(task+"\n")

        update_radiobuttons()        

def addtask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open('todo/taskfile.txt','a') as tf:
            tf.write(f"\n{task}")
        tasks_list.append(task)
        update_radiobuttons()

def update_radiobuttons():
    for rb in radio_buttons:
        rb.destroy()

    radio_buttons.clear()

    for task in tasks_list:
        x_offset = 10
        y_offset = 10
        for task in tasks_list:
            rb = Radiobutton(main_frame, text=task, variable=selected_task, value=task, font='arial 16 bold', bg="bisque2", fg='tan4')
            rb.place(x=x_offset, y=y_offset)
            radio_buttons.append(rb)
            y_offset += 30  # Increasing y offset for next Radiobutton

def bg_img(root, image_path):
    try:
        # Opening the image file
        image = Image.open(image_path)
        tk_image = ImageTk.PhotoImage(image)
        # label for the image
        background_label = Label(root, image=tk_image)
        background_label.image = tk_image  
        background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    except Exception as e:
        print("Error loading image:", e)

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)  # Update every second

# Main tkinter window
root = Tk()
root.geometry('500x500')

#background image 
bg_img(root, "todo/Calendar.png")

# main-frame(to-do tasks frame)
style = ttk.Style()
style.configure('RoundedFrame.TFrame', borderwidth=8, relief='groove', bordercolor='brown', background='bisque2')
main_frame = ttk.Frame(root, style='RoundedFrame.TFrame', width=342, height=378 )
main_frame.place(x=163, y=200)

#calendar frame
cal_frame = Frame(root,width = 250,height =200,bg = 'white')
cal_frame.place(x = 655,y = 160)
# calendar widget
cal = Calendar(cal_frame, background='white', foreground='tomato4',width = 250,height = 500, selectbackground='burlywood', selectforeground='brown', bordercolor='white', headersbackground='white', normalbackground='wheat3', normalforeground='#8A360F', weekendbackground='wheat3', weekendforeground='#9C661F', othermonthbackground='white', othermonthforeground='wheat3', othermonthweforeground='white', othermonthwebackground='white', arrowscolor='brown')
cal.pack(expand = True,fill = 'both')

# label for time
time_label = Label(root, font=('Helvetica', 20), background='white',foreground='wheat3')
time_label.place(x = 1050,y = 597)
update_time()  # Start updating time

# Default text for the Entry widget
default_text = "Enter your task here"
# task-Entry widget
task_entry = Entry(root, width=21, relief=RIDGE, font=('Arial', 22, 'bold'), bd=2, background='bisque2', highlightthickness=2, highlightbackground="white",highlightcolor='wheat3')
task_entry.place(x=163, y=586)
task_entry.insert(0, default_text)
task_entry.config(fg='bisque3')  # Set default text color 
#  Event handling using lambda functions
task_entry.bind('<FocusIn>', lambda event: task_entry.delete(0, END) if task_entry.get() == default_text else None)
task_entry.bind('<FocusOut>', lambda event: task_entry.insert(0, default_text) if task_entry.get() == '' else None)

# quote entry box
default_q_text = "Enter quote :"
quote_entry = Entry(root, width=20, relief=RIDGE, font=('Arial', 11, 'bold'), bd=2, background='white',borderwidth=0)
quote_entry.place(x=1085, y=465)
quote_entry.insert(0, default_q_text)
quote_entry.config(fg='bisque3')  # Set default text color 
#  Event handling using lambda functions
quote_entry.bind('<FocusIn>', lambda event: quote_entry.delete(0, END) if quote_entry.get() == default_q_text else None)
quote_entry.bind('<FocusOut>', lambda event: quote_entry.insert(0, default_q_text) if quote_entry.get() == '' else None)
# Bind Enter key to the Entry widget
quote_entry.bind('<Return>', on_enter)
# label to display quote
quote_label = Label(root, text="\t", font=('Arial', 16), height=8, width=24, bg='white', anchor='nw')
quote_label.place(x=1036, y=202)

#'add-task' button
add_button = Button(root, text="A   D   D", font='arial 20 bold', width=14, bg='white', fg='black', bd=0, command=addtask)
add_button.place(x=154, y=694)

#'delete-task' button
del_button = Button(root, text="Delete", font='arial 20 bold', width=16, bg='white', fg='black', bd=0, command=deltask)
del_button.place(x=650, y=702)

#task- radiobuttons
selected_task = StringVar()
radio_buttons = []
# taskfile()
update_radiobuttons()

# Running the window
root.mainloop()
