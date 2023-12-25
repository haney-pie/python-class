while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    computer_action = ("rock")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "scissors":
        print("Rock smashes scissors! You lose")
    else:
        print("Paper covers rock! you win!.")