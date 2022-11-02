import random
random_num = random.randint(1,10)
tries = 1
username = input("Hello, What's your Username:")
print("Hello", username+",", )
question = input("Would you Like To Play A Game?[Y/N]")
if question == "n":
    print("okay")
if question == "y":
    print("I'm Thinking Of A Number Between 1 & 10")
    guess = int(input("Have a Guess :"))
    if guess>random_num:
        print("Guess Lower")
    if guess<random_num:
        print("Guess Higher")
    while guess!=random_num:
        tries+=1
        guess=int(input("Try Again: "))
        if guess<random_num:
            print("Guess Higher")
    if guess==random_num:
        print("You're Right! you win! The Number Was", random_num, "and took only", tries, "tries!")
 
