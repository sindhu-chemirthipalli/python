def game(p1,p2):
    if(p1==p2):
        print("its a tie")
    elif(p1 == "rock")and(p2 =="paper"):
        print("congrats p2")
    elif (p1 == "rock") and (p2 == "paper"):
        print("congrats p2")
    elif (p1 == "paper") and (p2 == "scissor"):
        print("congrats p2")
    elif (p1 == "scissor") and (p2 == "rock"):
        print("congrats p2")
    elif (p1 == "paper") and (p2 == "rock"):
        print("congrats p1")
    elif (p1 == "scissor") and (p2 == "paper"):
        print("congrats p1")
    elif(p1 =="rock") and (p2 =="scissor"):
        print("congrats p1")
    else:
        print("invalid input")
    return()