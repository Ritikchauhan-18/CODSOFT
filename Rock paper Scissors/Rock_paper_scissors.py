import tkinter as tk
import random
from tkinter import messagebox
from tkinter import PhotoImage

# Initialize game variables
user_score = 0
computer_score = 0
rounds_played = 0

# Choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score, rounds_played
    rounds_played += 1

    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "Win"
    else:
        computer_score += 1
        return "Lose"

# Function to play a round of the game
def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer's Choice: {computer_choice}")

    # Animate the computer choice
    animate_computer_choice(computer_choice)
    
    # Check the result and show a pop-up message
    if result == "Win":
        messagebox.showinfo("Result", "You Win!")
    elif result == "Lose":
        messagebox.showinfo("Result", "You Lose!")
    else:
        messagebox.showinfo("Result", "It's a Tie!")

    # Update the labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")
    rounds_label.config(text=f"Rounds Played: {rounds_played}")

# Function to animate computer choice
def animate_computer_choice(choice):
    delay = 100  # Delay in milliseconds for animation
    for _ in range(10):
        result_label.config(text=f"{random.choice(choices)}")
        root.update()
        root.after(delay)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# User's choice buttons
user_choice_frame = tk.Frame(root)
user_choice_frame.pack(side=tk.LEFT, padx=10)
user_choice_label = tk.Label(user_choice_frame, text="Your Choice", font=("Helvetica", 34))
user_choice_label.pack()
user_choices = ["Rock", "Paper", "Scissors"]
for choice in user_choices:
    choice_button = tk.Button(user_choice_frame, text=choice, command=lambda c=choice.lower(): play_game(c))
    choice_button.pack(padx=10)


# Create a label widget to display the text
text_label = tk.Label(root, text="Rock-Paper-Scissors\nGame\n\n", font=("Helvetica",56))

# Use the pack geometry manager to center the label at the top
text_label.pack(side="top", pady=10)

# Computer's choice labels
computer_choice_frame = tk.Frame(root)
computer_choice_frame.pack(side=tk.RIGHT, padx=10)
computer_choice_label = tk.Label(computer_choice_frame, text="Computer's Choice", font=("Helvetica", 25))
computer_choice_label.pack()
result_label = tk.Label(computer_choice_frame, text="", font=("Helvetica", 25))
result_label.pack()

# Score labels
user_score_label = tk.Label(root, text=f"User Score: {user_score}", font=("Helvetica", 25))
user_score_label.pack()
computer_score_label = tk.Label(root, text=f"Computer Score: {computer_score}", font=("Helvetica", 25))
computer_score_label.pack()

# Rounds label
rounds_label = tk.Label(root, text=f"Rounds Played: {rounds_played}", font=("Helvetica", 25))
rounds_label.pack()


# Start the GUI main loop
root.mainloop()