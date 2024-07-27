  Features
The computer generates a random target number between 1 and 100.
The player inputs their guess in a text field.
The game provides feedback on whether the guess is too high, too low, or correct.
The number of attempts is tracked and displayed once the player guesses correctly.
The game resets after a correct guess, allowing for a new round.
Requirements
Python 3.x
Tkinter (usually included with Python installations)
 Installation
Clone the Repository:


git clone https://github.com/your-username/number-guessing-game.git
Navigate to the Project Directory:


cd number-guessing-game
Usage
Run the Application:


python number_guessing_game.py
Play the Game:

Enter a number between 1 and 100 in the input field.
Click the "Submit Guess" button.
Receive feedback on whether your guess is too high, too low, or correct.
If you guess correctly, the number of attempts is displayed, and the game resets for a new round.
Code Overview
NumberGuessingGame Class
__init__(self, root):

Initializes the game with a random target number and zero attempts.
Creates the GUI components including a label, entry box, submit button, and result label.
check_guess(self):

Handles the user's guess, provides feedback, and checks if the guess is correct.
Updates the result label with appropriate messages.
reset_game(self):

Resets the game state after a correct guess by generating a new target number and resetting the attempt count.
GUI Layout
Label: Displays instructions for the player.
Entry Box: Where the player inputs their guess.
Submit Button: Submits the guess and triggers the check.
Result Label: Displays feedback on the player's guess.
Example Code
Here is the main code for the game:

python
Copy code
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

 Create the main window
root = tk.Tk()
app = NumberGuessingGame(root)

 Run the application
root.mainloop()
  License
This project is licensed under the MIT License - see the LICENSE file for details.

  Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.
