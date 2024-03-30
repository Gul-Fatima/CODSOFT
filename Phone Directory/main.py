import tkinter as tk
import customtkinter as ct
from tkinter import messagebox

phone_directory = {}
def validate_input(new_value):
    if new_value == "" or not new_value.isdigit():
        return False
    return len(new_value) <= 11

def add_member():
    name = first_name_entry.get() + " " + last_name_entry.get()
    phone_number = phone_number_entry.get()
    phone_directory[name] = phone_number
    save_contacts()
    messagebox.showinfo("Success", f"{name.title()} is added to the phone directory.")
    
    # Clear entry boxes after adding the contact
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)  # Moved this line here
    email_entry.delete(0, tk.END)


def load_contacts():
    try:
        with open("Phone Directory/contacts.txt", "r") as file:
            for line in file:
                name, phone_number = line.strip().split(":")
                phone_directory[name] = phone_number
    except FileNotFoundError:
        pass

def save_contacts():
    with open("Phone Directory/contacts.txt", "a") as file:
        for name, phone_number in phone_directory.items():
            file.write(f"{name}:{phone_number}\n")

def delete_member():
    name = first_name_entry.get() + " " + last_name_entry.get()
    if name not in phone_directory:
        status_label.config(text="Contact not found")
    else:
        phone_directory.pop(name)
        save_contacts()
        messagebox.showinfo("Success", f"{name.title()} has been deleted from the phone directory.")

def print_directory():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Phone Directory:\n")
    for name, phone_number in phone_directory.items():
        output_text.insert(tk.END, f"{name}: {phone_number}\n")
    output_text.insert(tk.END, f"Total members: {len(phone_directory)}")

# Create Tkinter GUI
root = tk.Tk()
root.title("Phone Directory App")
root.config(background='lightsteelblue1')

option_frame = ct.CTkFrame(root, bg_color='lightsteelblue1', fg_color='white', width=800, height=700)
option_frame.place(x=90, y=80)

directory_frame = ct.CTkFrame(root, bg_color='lightsteelblue1', fg_color='white', width=500, height=700)
directory_frame.place(x=1000, y=80)

top_label = ct.CTkLabel(option_frame,text="Phone   Directory",font=('Times',80,'bold'),text_color='lightskyblue' )
top_label.place(x = 100, y= 30)

first_name_label = tk.Label(option_frame, text="First Name:",fg='lightsteelblue1',font='times 14',bg='white')
first_name_label.place(x=80, y=160)
first_name_entry = ct.CTkEntry(option_frame,width=600,height=40,fg_color='lightsteelblue1',text_color='black',font=('times ',20 ,'bold'))
first_name_entry.place(x=80, y=200)

last_name_label = tk.Label(option_frame, text="Last Name:",fg='lightsteelblue1',font='times 14',bg='white')
last_name_label.place(x=80, y=250)
last_name_entry = ct.CTkEntry(option_frame,width=600,height=40,fg_color='lightsteelblue1',text_color='black',font=('times ',20 ,'bold'))
last_name_entry.place(x=80, y=290)

phone_number_label = tk.Label(option_frame, text="Phone Number:",fg='lightsteelblue1',font='times 14',bg='white')
phone_number_label.place(x=80, y=340)
phone_number_entry = ct.CTkEntry(option_frame,width=600,height=40,fg_color='lightsteelblue1',text_color='black',font=('times ',20,'bold' ))
phone_number_entry.configure(validate="key", validatecommand=(phone_number_entry.register(validate_input), "%P"))
phone_number_entry.place(x=80, y=380)

email_label = tk.Label(option_frame, text="Email:",fg='lightsteelblue1',font='times 14',bg='white')
email_label.place(x=80, y=430)
email_entry = ct.CTkEntry(option_frame,width=600,height=40,fg_color='lightsteelblue1',text_color='black',font=('times ',20 ,'bold'))
email_entry.place(x=80, y=470)

add_button = ct.CTkButton(option_frame, text="Add", command=add_member,corner_radius=5, width=280,height=24, fg_color='lightskyblue', font=("times", 24, 'bold'),text_color='white')
add_button.place(x=400, y=550)

delete_button = ct.CTkButton(option_frame, text="Delete", command=delete_member,corner_radius=5,border_color='lightskyblue',border_width=2, width=280,height=24, fg_color='lavender', font=("times", 24, 'bold'),text_color='lightskyblue')
delete_button.place(x=80, y=550)

print_button = ct.CTkButton(directory_frame, text="Print", command=print_directory, corner_radius=5, width=205,height=24, fg_color='lightskyblue', font=("times", 24, 'bold'),text_color='white')
print_button.place(x=270, y=640)

status_label = tk.Label(directory_frame, text="")
status_label.place(x=10, y=160)

output_text = tk.Text(directory_frame, height=38, width=58,borderwidth= 2)
output_text.place(x=14, y=10)

load_contacts()  # Load contacts from file when the program starts

root.mainloop()
