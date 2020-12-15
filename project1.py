""" Booking Tickets """


def main():
    """ Welcome stage before start"""
    welcome1 = str(input(
        "Welcome to Movie Booking Tickets system (IDLE Version) [Press 'Y' to start or Press 'N' to cancel.]  Ans:"))
    if welcome1 == 'Y' or welcome1 == 'y':
        print("Okay")
        func1('1.Alive', '2.Frozen 2', '3.Iron Mask') #edit movies name here
    elif welcome1 == 'N' or welcome1 == 'n':
        print("Thank you for using. See you next time ! ;D")
    else:
        print("!!!!!!!!!!!!")
        print("Try Again!!")
        print("!!!!!!!!!!!!")
        main()


def func1(mov1, mov2, mov3, inf1=0, inf2=0, inf3=0, num1=1):
    """ Let's get started """
    inf1 = ("Alive is a 2020 South Korean zombie film directed by Cho Il-hyung.") #edit here
    inf2 = ("Frozen is a 2013 American 3D computer-animated musical fantasy film produced by Walt Disney Animation Studios and released by Walt Disney Pictures") #edit here
    inf3 = ("Iron Mask, an action-fantasy epic starring Jackie Chan and Arnold Schwarzenegger") #edit here
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
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]  Ans:"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
            func3(mov1, mov2, mov3, 1)
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf1)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]  Ans:"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
                func3(mov1, mov2, mov3, 1)
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
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func2(mov1, mov2, mov3, inf1, inf2, inf3, 1)
    elif num1 == 2:
        print("Okay you choose [%s]" % mov2)
        strcor1 = str(
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]  Ans:"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
            func3(mov1, mov2, mov3, 2)
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf2)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]  Ans:"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
                func3(mov1, mov2, mov3, 2)
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
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func2(mov1, mov2, mov3, inf1, inf2, inf3, 2)
    elif num1 == 3:
        print("Okay you choose [%s]" % mov3)
        strcor1 = str(
            input("Right? [Press 'Y' to confirm, 'I' to see detail or 'N' to change]  Ans:"))
        if strcor1 == 'Y' or strcor1 == 'y':
            print("Okay Let's go to next step")
            func3(mov1, mov2, mov3, 3)
        elif strcor1 == 'I' or strcor1 == 'i':
            print(inf3)
            strcor2 = str(
                input("Select This? [Press 'Y' to confirm or 'N' to change]  Ans:"))
            if strcor2 == 'Y' or strcor2 == 'y':
                print("Okay Let's go to next step")
                func3(mov1, mov2, mov3, 3)
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
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func2(mov1, mov2, mov3, inf1, inf2, inf3, 3)

def func3(mov1, mov2, mov3, num1=1):
    if num1 == 1:
        print("Time to choose seat for [%s]" %mov1)
        print("--------------- Screen ---------------")
        print("[A1] [A2] [A3] [A4] [A5] [A6]")
        print("[B1] [B2] [B3] [B4] [B5] [B6]")
        print("[C1] [C2] [C3] [C4] [C5] [C6]")
        print("[D1] [D2] [D3] [D4] [D5] [D6]")
        print("[E1] [E2] [E3] [E4] [E5] [E6]")
        strseat1 = input("Input the number you want:..")
        strseat10 = strseat1.upper()
        strseat11 = strseat10.split()
        strseat2 = input("Okay Your Seat(s) is.. %s Right? [Press 'Y' to confirm or 'N' to change]  Ans:" %strseat11)
        if strseat2 == 'Y' or strseat2 == 'y':
            print("Okay Your Movie [%s] with seat(s) : %s" %(mov1, strseat11))
            print("~~~~~ Print your e-ticket receipt ~~~~~") #False
            print("Enjoy your movie !!")
        elif strseat2 == 'N' or strseat2 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func3(mov1, mov2, mov3, 1)
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func3(mov1, mov2, mov3, 1)
    elif num1 == 2:
        print("Time to choose seat for [%s]" %mov2)
        print("----------- Screen -----------")
        print("[A1] [A2] [A3] [A4] [A5] [A6]")
        print("[B1] [B2] [B3] [B4] [B5] [B6]")
        print("[C1] [C2] [C3] [C4] [C5] [C6]")
        print("[D1] [D2] [D3] [D4] [D5] [D6]")
        print("[E1] [E2] [E3] [E4] [E5] [E6]")
        strseat1 = input("Input the number you want:..")
        strseat10 = strseat1.upper()
        strseat11 = strseat10.split()
        strseat2 = input("Okay Your Seat(s) is.. %s Right? [Press 'Y' to confirm or 'N' to change]  Ans:" %strseat11)
        if strseat2 == 'Y' or strseat2 == 'y':
            print("Okay Your Movie [%s] with seat(s) : %s" %(mov2, strseat11))
            print("~~~~~ Print your e-ticket receipt ~~~~~") #False
            print("Enjoy your movie !!")
        elif strseat2 == 'N' or strseat2 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func3(mov1, mov2, mov3, 2)
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func3(mov1, mov2, mov3, 2)
    elif num1 == 3:
        print("Time to choose seat for [%s]" %mov3)
        print("----------- Screen -----------")
        print("[A1] [A2] [A3] [A4] [A5] [A6]")
        print("[B1] [B2] [B3] [B4] [B5] [B6]")
        print("[C1] [C2] [C3] [C4] [C5] [C6]")
        print("[D1] [D2] [D3] [D4] [D5] [D6]")
        print("[E1] [E2] [E3] [E4] [E5] [E6]")
        strseat1 = input("Input the number you want:..")
        strseat10 = strseat1.upper()
        strseat11 = strseat10.split()
        strseat2 = input("Okay Your Seat(s) is.. %s Right? [Press 'Y' to confirm or 'N' to change]  Ans:" %strseat11)
        if strseat2 == 'Y' or strseat2 == 'y':
            print("Okay Your Movie [%s] with seat(s) : %s" %(mov3, strseat11))
            print("~~~~~ Print your e-ticket receipt ~~~~~") #False
            print("Enjoy your movie !!")
        elif strseat2 == 'N' or strseat2 == 'n':
            print("---------------------------------")
            print("Change? No problem :D")
            print("Let me repeat")
            print("---------------------------------")
            func3(mov1, mov2, mov3, 3)
        else:
            print("!!!!!!!!!!!!")
            print("Try again!")
            print("!!!!!!!!!!!!")
            func3(mov1, mov2, mov3, 3)

main()
