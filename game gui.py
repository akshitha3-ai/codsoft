import tkinter as tk
import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"You: {user_score}  |  Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose rock, paper, or scissors:", font=("Arial", 14)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), pady=10)
result_label.pack()

score_label = tk.Label(root, text="You: 0  |  Computer: 0", font=("Arial", 12))
score_label.pack()

tk.Button(root, text="Quit", command=root.quit, width=10).pack(pady=10)

root.mainloop()
