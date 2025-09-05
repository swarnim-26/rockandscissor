import tkinter as tk
from tkinter import Button, TOP, Label
from PIL import Image, ImageTk
import random

# Window setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("700x500")
root.config(bg="lightblue")

# Choices
choices = ["rock", "paper", "scissors"]

# Load images
rock_img = ImageTk.PhotoImage(Image.open("C:/Users/Welcome/Downloads/rock.webp").resize((120, 120)))
paper_img = ImageTk.PhotoImage(Image.open("C:/Users/Welcome/Downloads/paper.webp").resize((120, 120)))
scissors_img = ImageTk.PhotoImage(Image.open("C:/Users/Welcome/Downloads/scissors.webp").resize((120, 120)))

# Mapping choices to images
image_dict = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

# Labels
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="lightblue")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=20)

# User side
user_label = tk.Label(frame, text="You", font=("Arial", 16), bg="lightblue")
user_label.grid(row=0, column=0, pady=10)
user_img_label = tk.Label(frame, bg="lightblue")
user_img_label.grid(row=1, column=0)

# VS label
vs_label = tk.Label(frame, text="VS", font=("Arial", 20, "bold"), bg="lightblue")
vs_label.grid(row=1, column=1, padx=40)

# Computer side
comp_label = tk.Label(frame, text="Computer", font=("Arial", 16), bg="lightblue")
comp_label.grid(row=0, column=2, pady=10)
comp_img_label = tk.Label(frame, bg="lightblue")
comp_img_label.grid(row=1, column=2)

# Result text
result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="lightblue")
result_label.pack(pady=20)

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    # Show images
    user_img_label.config(image=image_dict[user_choice])
    comp_img_label.config(image=image_dict[computer_choice])

    # Decide winner
    if user_choice == computer_choice:
        result = "🤝 It's a Draw!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "🎉 You Win!"
    else:
        result = "😢 You Lose!"

    result_label.config(text=result)
def reset():
    user_img_label.config(image="")
    comp_img_label.config(image="")
    result_label.config(text="")
    
# Buttons for choices
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=30)

rock_btn = tk.Button(button_frame, image=rock_img, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=20)

paper_btn = tk.Button(button_frame, image=paper_img, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=20)

scissors_btn = tk.Button(button_frame, image=scissors_img, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=20)

reset_button = Button(text="Restart", font=("consolas", 20), command=lambda: reset())
reset_button.pack(side=TOP)

root.mainloop()