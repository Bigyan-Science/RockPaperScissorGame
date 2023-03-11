import random

def ComputerRandomNumberGen():
    return random.randint(1, 3)

def displayComputerChoice(computer_choice):
    if computer_choice == 1:
        print("Computer has chosen Rock")
    elif computer_choice == 2:
        print("Computer has chosen Paper")
    else:
        print("Computer has chosen Scissors")

def displayUserChoice():
    userChoice = int(input("Enter your choice: Rock (1), Paper (2), Scissors (3)"))
    return userChoice

def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    elif user_choice == 1 and computer_choice == 3:
        return 1
    elif user_choice == 2 and computer_choice == 1:
        return 1
    elif user_choice == 3 and computer_choice == 2:
        return 1
    else:
        return -1

def display_static_Info(winner, user_choice, computer_choice):
    with open("result.txt", "w") as f:
        if winner == 1:
            print("You win!")
            f.write("You win!" + "\n")
            name = input("Enter your name: ")
            address = input("Enter your address: ")
            phone = input("Enter your phone number: ")
            with open("inputData.txt", "w") as file:
                file.write("Name: " + name + "\n")
                file.write("Address: " + address + "\n")
                file.write("Phone: " + phone + "\n")
        elif winner == -1:
            print("Computer wins!", end="\n\n")
            f.write("Computer wins!" + "\n")
        else:
            print("Draw!", end="\n\n")
            f.write("Draw!" + "\n")
        f.write("Your choice: ")
        if user_choice == 1:
            f.write("Rock" + "\n")
        elif user_choice == 2:
            f.write("Paper" + "\n")
        else:
            f.write("Scissors" + "\n")
        f.write("Computer choice: ")
        if computer_choice == 1:
            f.write("Rock" + "\n")
        elif computer_choice == 2:
            f.write("Paper" + "\n")
        else:
            f.write("Scissors" + "\n")

print("Welcome to the Rock-Paper-Scissors game!\n")

while True:
    user_choice = displayUserChoice()
    computer_choice = ComputerRandomNumberGen()
    displayComputerChoice(computer_choice)
    winner = DetermineWinnerOfRPS(user_choice, computer_choice)
    display_static_Info(winner, user_choice, computer_choice)
    if winner != 0:
        break
    print("Tie game! Play again.\n")
