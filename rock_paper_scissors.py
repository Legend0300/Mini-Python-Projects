import   random
user_won = False
while user_won == False:
	print("Welcome Valid choices are: rock , paper and scissors")
	gesture = input("Enter your Gesture: ")
	comp_choice = random.choice(["rock" , "paper" , "scissors"])
	if gesture == "rock" and comp_choice == "rock" or gesture == "paper" and comp_choice == "paper" or gesture == "scissors" and comp_choice == "scissors":
		print('its a tie')
# win conditions
	elif gesture == "rock" and comp_choice == 'scissors' or gesture == "scissors" and comp_choice == "paper" or gesture == "paper" and comp_choice == "rock":
		print("you entered : " + gesture + " and computer entered : " + comp_choice)
		print("You win!")
		play_status = input("Want to play again? yes or no: ")
		if play_status == "yes":
			continue
		else:
			break
# losing conditions
	elif gesture == 'paper' and comp_choice == 'scissors' or gesture == 'scissors' and comp_choice == 'rock' or gesture == 'rock' and comp_choice == "paper":
		print("you entered : " + gesture + " and computer entered : " + comp_choice)
		print("Compter won :(")
	else:
		print("Please enter a valid input")