import random
import string
import tkinter as tk 
import customtkinter
from PIL import ImageTk,Image
import pyperclip


def generator():
    passwordField.delete(0, tk.END)
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all= small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)



def on_slider_move(value):
    global x
    if value <= 33:
        x = 'Easy'
    elif 33 < value <= 66:
        x = 'Medium'
    else:
        x = 'Difficult'
    slider_label.configure(text=x)

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green")  

app = customtkinter.CTk()  
app.geometry("600x440")
app.title('Password Generator')

#background image
img1 = ImageTk.PhotoImage(Image.open("passwordgenerator/pattern.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

# mainframe
frame = customtkinter.CTkFrame(master=l1, width=420, height=580, corner_radius=15, bg_color='gray14', fg_color='gray18')
frame.place(relx=0.5, rely=0.51, anchor=tk.CENTER)

# password generator label
l2 = customtkinter.CTkLabel(master=frame, text="Password Generator", text_color='white', font=('Century Gothic', 30 ,'bold'))
l2.place(x=70, y=45)

choice = tk.IntVar()
#check buttons
weakCheckBox = customtkinter.CTkCheckBox(master=frame, text='  Include Lowercase Characters', variable=choice, onvalue=1, offvalue=0, font=('times', 13 ,'bold'),text_color='white',checkbox_height=15,checkbox_width=15)
weakCheckBox.place(x=72, y=280)
mediumCheckBox = customtkinter.CTkCheckBox (master=frame, text='  Include Uppercase Characters', variable=choice, onvalue=2, offvalue=0, font=('times', 13 ,'bold'),text_color='white',checkbox_height=15,checkbox_width=15)
mediumCheckBox.place(x=72, y=320 ) 
strongCheckBox = customtkinter.CTkCheckBox (master=frame, text='  Includes Symbols', variable=choice, onvalue=3, offvalue=0, font=('times', 13 ,'bold'),text_color='white',checkbox_height=15,checkbox_width=15)
strongCheckBox.place(x=72, y=360)

canvas = tk.Canvas(frame, width=2, height=250, bg='black')
canvas.place(x=50, y=225)
canvas.create_line(0, 0, 0, 50, fill='white', width=2)

# length spinbox
length_Box = tk.Spinbox(frame, from_=3, to_=10, width=16, font=('times', 13, 'bold'), background='gray14', fg='white',bd=2,buttonbackground='black')
length_Box.place(x=180, y=230)
length_label= customtkinter.CTkLabel(master=frame, text="Length",text_color='lightyellow2', font=('times', 16 ,'bold'))
length_label.place(x=70, y=228)

# horizantal easy,medium,difficult slider
slider = customtkinter.CTkSlider(frame, from_=0, to=100, command=on_slider_move,width= 280)
slider.place(x=70, y=450)
slider_label = customtkinter.CTkLabel(master=frame, font=('times', 12),text_color='white',text='')
slider_label.place(x=290,y=400)
# password complexity
pc_label= customtkinter.CTkLabel(master=frame, text="Password Complexity", text_color='lightyellow2',font=('times', 14 ,'bold'))
pc_label.place(x=70, y=406)

# your password label
password_label = customtkinter.CTkLabel(master=frame, text="Your Password",text_color='lightyellow2', font=('Century Gothic', 16))
password_label.place(x=20, y=115)

# generate password button
password_button = customtkinter.CTkButton(master=frame, width=180,height= 30, text="Generate",font=('Century Gothic', 15,'bold'), command=generator, corner_radius=6)
password_button.place(x=220, y=520)

# password field
passwordField=customtkinter.CTkEntry(frame,width=350,font=("Times", 26, "bold") ,height=40,border_color='seagreen3')
passwordField.place(x = 30,y = 150)

# generate password button
copy_button = customtkinter.CTkButton(master=frame, width=180,height= 30, text="Copy",font=('Century Gothic', 15,'bold'), command=copy, corner_radius=6)
copy_button.place(x=20, y=520)

app.mainloop()
