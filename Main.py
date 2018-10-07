def choose(choice):
    while True:
        if choice.find(".") >= 0 or choice.find("-") >= 0:
            choice = input("You didn't type in a positive integer. Please try again: ")
        else:
            try:
                choice = int(choice)
                dummyNum = 2/choice
                if choice == 1 or choice == 2 or choice == 3:
                    break
                else:
                    choice = input("You didn't type a valid choice. Please try again: ")
            except ValueError:
                choice = input("You didn't type in a positive integer. Please try again: ")
            except ArithmeticError:
                choice = input("You didn't type in a positive integer. Please try again: ")
    print("")
    return choice

def main():
    hasNotQuit = True
    while hasNotQuit:
        choice = input("What would you like to do? Please select an option below:\n1. Encrypt a text file\n2. Encrypt an image\n3. Quit\n\nEnter your choice: ")
        choice = choose(choice)
        if choice == 1:
            choice = input("Would you like to encrypt a text file into Morse code or pig Latin?\n1. Morse code\n2.Pig Latin")
            choice = choose(choice)
            if choice == 1:
                import morse
            else:
                import piglatin
        elif choice == 2:
            import EncryptImage
        else:
            hasNotQuit = False
            print("Exiting the program...")

main()