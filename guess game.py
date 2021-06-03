def guess_the_number():
    y = False
    while y == False:
        x = int(input("enter a number bw 1 and 50: "))
        if x == 23:
            print("you guessed the number right!")
            y = True
        else:
            print("please try again :p ")

guess_the_number()