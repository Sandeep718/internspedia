print("You are standing outside of your house and you see a man running towards youand asking for urgent shelter.")
print("Will you provide shelter?(y/n)")
a1 = input("")
if a1=="y":
    print("Police came to your house, and ask you that whether the thief is in your house or not.")
    print("Will you say (y/n)")
    a2 = input("")
    if a2=="y":
        print("You are an honest person. He was a thief & You won the Game\n")
    elif a2=="n":
        print("You helped a thief. Now, go to Jail.GAME OVER\n")
    else:
        print("wrong input.")
elif a1=="n":
    print("Now, he is trying to kill you. Will, you knock him down?(y/n)")
    a3 = input("")
    if a3=="y":
        print("Congrats! He was a thief and You helped the police to catch him.\n")
    elif a3=="n":
        print("Sorry! You are dead.He was a thief and killed you.GAME OVER\n")
    else:
        print("wrong input.")
else:
    print("wrong input.")
