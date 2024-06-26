import random

def decide_winner(user_choice, computer_choice):
	messages = {
		"tie": "It's a tie!",
		"won": "You won!",
		"lost": "You lost!"
	}

	print("You selected: %s" % user_choice)
	print("The computer selected: %s" % computer_choice)
	
	if user_choice == computer_choice:
		print(messages["tie"])
	elif user_choice == "ROCK":
		if computer_choice == "SCISSORS":
			print(messages["won"])
		else:
			print(messages["lost"])
	elif user_choice == "PAPER":
		if computer_choice == "ROCK":
			print(messages["won"])
		else:
			print(messages["lost"])
	elif user_choice == "SCISSORS":
		if computer_choice == "PAPER":
			print(messages["won"])
		else:
			print(messages["lost"])
	else:
		print("Invalid choice! Please choose Rock, Paper, or Scissors.")

# Example usage with random computer choice:
user_choice = input("Rock, Paper, Scissors: ").upper()
computer_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
decide_winner(user_choice, computer_choice)
