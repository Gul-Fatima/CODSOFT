import random as rd
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import customtkinter as ct

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # self.player_choices = []


        load = Image.open("rps/bg.png")
        # Resize the image to fit the window
        resized_image = load.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        # Create a label widget to display the resized image
        label = tk.Label(self, image=tk_image)
        label.pack(fill=tk.BOTH, expand=True)  # Fill the entire frame with the image
        label.image = tk_image  # Store a reference to the image to prevent garbage collection

        # Create a lets play button
        b = ct.CTkButton(self, corner_radius=2, text="L e t s   P l a y!", border_color='#8B008B', fg_color='pink',
                         bg_color='mediumorchid', text_color='mediumorchid1', height=50, font=("times", 25, 'bold'),
                         width=470, command=self.lets_play)
        b.place(x=987, y=664)

    def lets_play(self):
        self.controller.show_frame(SecondPage)
class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Devin = 0
        you = 0
        
        
        # bg image
        load = Image.open("rockpaper/Rock.png")
        # Resize the image to fit the window
        resized_image = load.resize((parent.winfo_screenwidth(), parent.winfo_screenheight()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        # Create a label widget to display the resized image
        label = tk.Label(self, image=tk_image)
        label.pack(fill=tk.BOTH, expand=True)  # Fill the entire frame with the image
        label.image = tk_image  # Store a reference to the image to prevent garbage collection

        # first main frame
        frame1 = tk.Frame(self, bg='pink')
        frame1.place(x=50, y=50, width=450, height=750)
        
        # Second main frame
        frame2 = tk.Frame(self, bg='pink')
        frame2.place(x=570, y=50, width=970, height=750)

        # User Score Frame
        user_frame = ct.CTkFrame(frame2, width=400, height=120, fg_color='cadetblue', corner_radius=15, bg_color='pink')
        user_frame.place(x=50, y=50)
        
        # Computer Score Frame
        comp_frame = ct.CTkFrame(frame2, width=400, height=120, fg_color='cadetblue', corner_radius=15, bg_color='pink')
        comp_frame.place(x=50, y=210)
        
        # Buttons
        self.rock_button = self.create_image_button('Helene.png', lambda: self.on_button_click("rock"),frame2)
        self.rock_button.place(x=80, y=450)
        self.paper_button = self.create_image_button('rps/paper.png',lambda: self.on_button_click("paper"), frame2)
        self.paper_button.place(x=380, y=450)
        self.scissor_button = self.create_image_button('rps/scissor.png', lambda: self.on_button_click("scissor"), frame2)
        self.scissor_button.place(x=680, y=450)
        
        #gamae plan label:
        self.game_plan_label = tk.Label(frame1, text="G a m e   P l a n ", background='pink',fg='cadetblue', font='times 40 bold')
        self.game_plan_label.place(x=30, y=80)
        
        # Input for number of turns
        self.turn_label = tk.Label(frame1, text="Enter number of turns:", fg='gray',background='pink', font='times 12')
        self.turn_label.place(x=50, y=400)
        self.turn_entry = ct.CTkEntry(frame1,width=350,font=('times',12))
        self.turn_entry.place(x=50, y=430)
        self.set_turns_button = ct.CTkButton(frame1, text="Set Turns", command=self.set_total_turns,fg_color='cadetblue',bg_color='pink',corner_radius=15)
        self.set_turns_button.place(x=250, y=470)
        
       
        # Play again button
        self.play_again_button = ct.CTkButton(frame1, text="Play again",font=('times',30,'bold'),height=35,width=350,corner_radius=135, fg_color='cadetblue',command=self.play_again)
        self.play_again_button.place(x=50, y=550)

        #username and computer entry boxes
        self.username_label = tk.Label(frame1, text="Username:", fg='gray',background='pink', font='times 12')
        self.username_label.place(x=50, y=300-100)
        self.username_entry = ct.CTkEntry(frame1,width=350,font=('times',24))
        self.username_entry.place(x=50, y=330-100)

        self.compname_label = tk.Label(frame1, text="Opponent's name", fg='gray',background='pink', font='times 12')
        self.compname_label.place(x=50, y=380-100)
        self.compname_entry = ct.CTkEntry(frame1,width=350,font=('times',24))
        self.compname_entry.place(x=50, y=410-100)
        
        #Scoreboard
        self.gsb_frame = ct.CTkFrame(frame2, width=400, height=280, fg_color='cadetblue', corner_radius=15, bg_color='pink')
        self.gsb_frame.place(x=500, y=50)
        self.wsb_frame = ct.CTkFrame(self.gsb_frame, width=380, height=260, fg_color='white', corner_radius=15, bg_color='cadetblue')
        self.wsb_frame.place(x=10, y=10)
                
        self.myname_label = tk.Label(user_frame, text="Username", fg='white',background='cadetblue', font='times 34')
        self.myname_label.place(x=15, y=20)
        self.username_entry.bind("<Return>", lambda event: self.myname_label.config(text=self.username_entry.get()))
        self.myscore_label = tk.Label(user_frame, text="Score : 0", fg='white',background='cadetblue', font='times 20')
        self.myscore_label.place(x=270, y=70)
        
        self.cname_label = tk.Label(comp_frame, text="Opponent", fg='white',background='cadetblue', font='times 34')
        self.cname_label.place(x=15, y=20)
        self.compname_entry.bind("<Return>", lambda event: self.cname_label.config(text=self.compname_entry.get()))
        self.pcscore_label = tk.Label(comp_frame, text="Score : 0", fg='white',background='cadetblue', font='times 20')
        self.pcscore_label.place(x=270, y=70)
        
        #wsb_frame scores label
        self.result_label = tk.Label(self.wsb_frame, text="Winner : ", fg='cadetblue4',background='white', font='times 26')
        self.result_label.place(x=15, y=180)
         
        #wsb_frame scores label
        self.computer_choice_label = tk.Label(self.wsb_frame, text="Computer chose : ", fg='cadetblue4',background='white', font='times 18')
        self.computer_choice_label.place(x=25, y=80)
        self.my_choice_label = tk.Label(self.wsb_frame, text="You chose : ", fg='cadetblue4',background='white', font='times 18')
        self.my_choice_label.place(x=25, y=120)
        
        self.length_Box = tk.Label(self.wsb_frame, text="Turns : 0/0", background='white',fg='cadetblue4', font='times 20')
        self.length_Box.place(x=220, y=30)
       
    def create_image_button(self, image_path, command_func, parent_frame):
        img = Image.open(image_path)
        resized_image = img.resize((300, 300), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)
        button = tk.Button(parent_frame, image=tk_image, highlightthickness=0, command=command_func, bd=0, width=200, height=200, borderwidth=0, background='red', border=0)
        button.img = tk_image  # To prevent garbage collection
        return button
    
    def play_again(self):
        # Clear the entry and update label
        self.turn_entry.delete(0, tk.END)
        self.length_Box.config(text="Turns : 0/0")
        self.set_total_turns()
        self.lets_play()

    def set_total_turns(self):
        global total_turns, current_turn, Devin, you
        total_turns = int(self.turn_entry.get())
        current_turn = 0
        Devin = 0
        you = 0
        # Update label with the number of turns
        self.length_Box.config(text=f"Turn: {current_turn}/{total_turns}")  
        self.play_again_button.config(state=tk.DISABLED)
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)

    
    def rock_paper_scissors(self, player_choice):
        global you, Devin  # Define global scores
    
        # Generate a random choice for the computer
        choices = ['rock', 'paper', 'scissors']
        computer_choice = rd.choice(choices)

        # Determine the winner based on choices
        if player_choice == computer_choice:
            return "It's a tie!", computer_choice
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'scissors' and computer_choice == 'paper') or \
            (player_choice == 'paper' and computer_choice == 'rock'):
            # Increment user score
            you += 1
            return "You win!", computer_choice
        else:
            # Increment opponent score
            Devin += 1
            return "Computer wins!", computer_choice

    def on_button_click(self, choice):
        global current_turn, you, Devin
        if current_turn < total_turns:
            result, computer_choice = self.rock_paper_scissors(choice)
            self.result_label.config(text=f"Winner : {result}")
            self.computer_choice_label.config(text=f"Computer chose: {computer_choice}")
            self.my_choice_label.config(text=f"You chose: {choice}")
            
            # Update the scores
            self.myscore_label.config(text=f"Score: {you}")
            self.pcscore_label.config(text=f"Score: {Devin}")

            current_turn += 1
            self.length_Box.config(text=f"Turn: {current_turn}/{total_turns}")
        else:
            messagebox.showinfo("Game Over", "Maximum number of turns reached!")

    
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window_frame = tk.Frame(self)
        window_frame.pack()
        
        window_frame.grid_rowconfigure(0, minsize = 500)
        window_frame.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, SecondPage):
            frame = F(window_frame, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")

app = Application()
# app.maxsize(800,500)
app.mainloop()
