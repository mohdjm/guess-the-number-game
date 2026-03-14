import art
import random

# Creating the Guess the Number function, guess_num(). Print logo, and welcome statement.
def guess_num():
	print(art.logo)

	is_game_over = False

	user_choice=[]
	computers_number=[]

	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	computers_number=random.randint(1,100)

	game_mode=input("Choose a difficulty. Type 'easy' or 'hard'.").lower()

	if game_mode == "easy":
		lives=10
		print(f"You have {lives} attempts remaining to guess the number.")

		while not is_game_over:
			user_choice = int(input("Make a guess: "))
			if user_choice == computers_number:
				print(f"You got it! The answer was {computers_number}!")
			elif user_choice > computers_number:
				lives -= 1
				print(f"Too high.\n Guess again.")
			elif user_choice< computers_number:
				lives-=1
				print(f"Too low.\n Guess again.")

	else:
		lives=5
		print(f"You have {lives} attempts remaining to guess the number.")

		while not is_game_over:
			user_choice = int(input("Make a guess: "))
			if user_choice == computers_number:
				print(f"You got it! The answer was {computers_number}!")
			elif user_choice > computers_number:
				lives -= 1
				print(f"Too high.\n Guess again.")
			elif user_choice< computers_number:
				lives-=1
				print(f"Too low.\n Guess again.")


guess_num()
