import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

while True:
    print("Comp's Turn: Rock(r) or Paper(p) or Scissor(s)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        comp = 'r'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 's'

    you = input("Your Turn : Rock(r) or Paper(p) or Scissor(s)?").lower()

    if you not in ('r', 'p', 's'):
        print("Invalid input. Please choose 'r', 'p', or 's'.")

        continue

    result = gameWin(comp, you)

    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    if result == None:
        print("The Game is a tie!")
    elif result:
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break