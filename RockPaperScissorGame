
import random 


print("------------------------------------")
print("Welcome to Rock Paper Scissors Game!")
print("------------------------------------")


my_list = ["Rock","Paper","Scissor"]

while True:
    choice = input("Enter your choice: ")
    computer = random.choice(my_list)
    match(choice):
        case "r":
            choice = "Rock"
            if choice == computer:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("it's a tie! both choose Rock.")
            elif "paper" == computer.lower():
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("Computer Wins! Rock covers by Paper")
            else:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("You Win! Rock crushes Scissor")
                print("-----------Exited------------")
                break
        case "p":
            choice = "Paper"
            if choice == computer:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("it's a tie both choose Paper")
            elif "rock" == computer.lower():
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("You Win! Paper covers Rock")
                break
            else:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("Computer Wins! Paper cuts by Scissor")
        case "s":
            choice = "Scissor"
            if choice == computer:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("it's a tie! both choose Scissor")
            elif "rock" == computer.lower():
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("Computer Wins! Scissor crushed by Rock")
            else:
                print(f"Your choice: {choice} \nComputer choice: {computer}")
                print("You Win! Scissor cuts Paper")
                break
