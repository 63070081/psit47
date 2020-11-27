""" Booking Tickets """


def main():
    """ Welcome stage before start"""
    welcome1 = str(input(
        "Welcome to Movie Booking Tickets system [Press 'Y' to start or Press 'N' to cancel.] Ans:"))
    if welcome1 == 'Y' or welcome1 == 'y':
        print("Okay")
        func1('1.Alive', '2.Frozen 2', '3.Iron Mask')
    elif welcome1 == 'N' or welcome1 == 'n':
        print("Thank you for using. See you next time ! ;D")
    else:
        print("!!!!!!!!!!!!")
        print("Try Again!!")
        print("!!!!!!!!!!!!")
        main()


def func1(mov1, mov2, mov3, inf1=0, inf2=0, inf3=0, num1=1):
    """ Let's get started """
    inf1 = ("Alive is a good movie created by...")
    inf2 = ("Frozen by Disney")
    inf3 = ("Iron mask super hero")
    print("Today we have a movies for you !")
    print("Here a list of movies we have today :D")
    print(mov1, mov2, mov3, sep="\n")
    num1 = str(
        input("Which one do you like? [Press 1, 2, 3 to select or 'N' to exit]  Ans:"))
    if num1 == 'N' or num1 == 'n':
        print("Thank you for using. See you next time ! ;D")
    elif num1 == '1':
        func2(mov1, mov2, mov3, inf1, inf2, inf3, 1)
    elif num1 == '2':
        func2(mov1, mov2, mov3, inf1, inf2, inf3, 2)
    elif num1 == '3':
        func2(mov1, mov2, mov3, inf1, inf2, inf3, 3)
    else:
        print("!!!!!!!!!!!!")
        print("Try again!")
        print("!!!!!!!!!!!!")
        func1(mov1, mov2, mov3)


def func2(mov1, mov2, mov3, inf1, inf2, inf3, num1=1):
    if num1 == 1:
        print("Okay you choose [%s]" % mov1)
        strcor1 = str(
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf1)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
            elif strcor2 == 'N' or strcor2 == 'n':
                print("---------------------------------")
                print("Change? No problem :D")
                print("Let me repeat")
                print("---------------------------------")
                func1(mov1, mov2, mov3)
        elif strcor1 == 'N' or strcor1 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func1(mov1, mov2, mov3)
    elif num1 == 2:
        print("Okay you choose [%s]" % mov1)
        strcor1 = str(
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf2)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
            elif strcor2 == 'N' or strcor2 == 'n':
                print("---------------------------------")
                print("Change? No problem :D")
                print("Let me repeat")
                print("---------------------------------")
                func1(mov1, mov2, mov3)
        elif strcor1 == 'N' or strcor1 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func1(mov1, mov2, mov3)
    elif num1 == 3:
        print("Okay you choose [%s]" % mov3)
        strcor1 = str(
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf3)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
            elif strcor2 == 'N' or strcor2 == 'n':
                print("---------------------------------")
                print("Change? No problem :D")
                print("Let me repeat")
                print("---------------------------------")
                func1(mov1, mov2, mov3)
        elif strcor1 == 'N' or strcor1 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func1(mov1, mov2, mov3)


main()
