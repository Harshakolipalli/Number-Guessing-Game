import tkinter as tk
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        # Initialize game variables
        self.target_number = random.randint(1, 100)
        self.attempts = 0

        # Create GUI components
        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < self.target_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.target_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
app = NumberGuessingGame(root)

# Run the application
root.mainloop()
