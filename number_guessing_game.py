import random
top_of_range=int(input("Type a number: "))
if top_of_range <=0:
    print("Please type a number larger than 0 next time.")
    quit()

random_number= random.randint(0,top_of_range)
guesses=0
while True:
    guesses +=1
    user_guess = int(input("Make a guess: "))

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("Your guess was greater than the number.")
    else:
            print("Your guess was lesser than the number.")
print("You got in",guesses,"guesses.")