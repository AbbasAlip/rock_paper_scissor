import random
options = ["rock" , "paper" , "scissor"]
user_wins = 0
computer_wins = 0
while True:
    user_pick = input("Choosse any one Rock/paper/scissor or Q to quit: ").lower()
    if user_pick == "q":
        quit()
    if user_pick not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked" , computer_pick)
    if user_pick == "scissor" and computer_pick == "paper":
        print("You Won!...")
        user_wins+=1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You Won!...")
        user_wins+=1
    elif user_pick == "rock" and computer_pick == "scissor":
        print("You Won!...")
        user_wins += 1
    else:
        print("Computer Won!....")
        computer_wins+=1
    print("You Won",user_wins,"times")
    print("The computer won", computer_wins,"times")
    print("Good Bye!")