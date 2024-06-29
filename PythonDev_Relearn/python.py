import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("300x200")

        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Choose:").pack()
        tk.Radiobutton(self.window, text="Rock", variable=self.user_choice, value="rock").pack()
        tk.Radiobutton(self.window, text="Paper", variable=self.user_choice, value="paper").pack()
        tk.Radiobutton(self.window, text="Scissors", variable=self.user_choice, value="scissors").pack()

        tk.Button(self.window, text="Play", command=self.play_game).pack()

        tk.Label(self.window, text="Computer chose:").pack()
        tk.Label(self.window, textvariable=self.computer_choice).pack()

        tk.Label(self.window, text="Result:").pack()
        tk.Label(self.window, textvariable=self.result).pack()

    def play_game(self):
        user_choice = self.user_choice.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        self.computer_choice.set(computer_choice)

        if user_choice == computer_choice:
            self.result.set("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.result.set("You win!")
        else:
            self.result.set("Computer wins!")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()