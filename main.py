import art
import random

# Global constants for easy and hard mode
EASY_LEVEL_LIVES =10
HARD_LEVEL_LIVES=5

def set_difficulty():
	game_mode = input("Choose a difficulty. Type 'easy' or 'hard'.").lower()
	if game_mode=="easy":
		return EASY_LEVEL_LIVES
	else:
		return HARD_LEVEL_LIVES

def check_answer(user_choice, computers_number, lives):
	if user_choice == computers_number:
		print(f"You got it! The answer was {computers_number}!")
		return 0
	elif user_choice > computers_number:
		print(f"Too high.")
		return lives - 1
	else:
		print(f"Too low.")
		return lives -1


# Creating the Guess the Number function, guess_num(). Print logo, and welcome statement.
def guess_num():
	print(art.logo)

	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")

	computers_number=random.randint(1,100)
	lives=set_difficulty()

	user_choice = 0
	while user_choice !=computers_number:
		print(f"You have {lives} attempts remaining to guess the number.")
		user_choice = int(input("Make a guess: "))

		# Track turns using our helper function
		lives = check_answer(user_choice, computers_number, lives)

		if lives == 0 and user_choice != computers_number:
			print(f"You've run out of guesses, you lose.\nThe answer was {computers_number}.")
			return
		elif user_choice != computers_number:
			print("Guess again.")


guess_num()
