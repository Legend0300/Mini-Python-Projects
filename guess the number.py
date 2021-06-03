def guess_the_number():
    number_guessed = False
    while number_guessed == False:
        number = int(input("enter a number: "))
        if number == 23:
            print("you guessed the number!")
            number_guessed = True
        else:
            print("Thats the wrong number try again")
            continue
guess_the_number()
