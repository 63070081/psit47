""" Booking Tickets """
def main():
    """ Welcome stage before start"""
    welcome1 = str(input("Welcome to Movie Booking Tickets system [Press 'Y' to start or Press 'N' to cancel.] Ans:"))
    if welcome1 == 'Y' or welcome1 == 'y':
        print("Okay")
        func1('1.Alive', '2.Frozen 2', '3.Iron Mask')
    elif welcome1 == 'N' or welcome1 == 'n':
        print("Thank you for using. See you next time ! ;D")
    else:
        print("Try Again!!")
        main()
    
def func1(mov1,mov2,mov3):
    """ Let's get started """
    print("Today we have a movies for you !")
    print("Here a list of movies we have today :D")
    print(mov1, mov2, mov3, sep="\n")
    num1 = int(input("Which one do you like? [Press 1, 2, 3 to select]  Ans:"))

main()
