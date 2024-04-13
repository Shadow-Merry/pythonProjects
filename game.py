import random
import os
def guessNumber():
    os.system('cls')
    print('****************************')
    print('Guess The Number Game')
    print('Range 1 to 50')
    print('****************************')
    x = random.randint(1,50)
    c = 1
    num = int(input('Guess the number: '))

    while (num != x):
        if x > num:
            print('To Low')
        else:
            print('To High')
        num = int(input('Guess the number: '))
        c += 1
    print('Congra You Guessed It Right')
    print(f'You Guessed {c} Times')
    print()
    print('To Play Again Press 1')
    print('To Exit Press 3')

def rockPaperRule(firstValue,secondValue):
    if firstValue == 'R' and secondValue =='S':
        win = True
    elif firstValue == 'R' and secondValue == 'P':
        win = False
    elif firstValue == 'S' and secondValue == 'P':
        win = True
    elif firstValue == 'S' and secondValue == 'R':
        win = False
    elif firstValue == 'P' and secondValue == 'R':
        win = True
    elif firstValue == 'P' and secondValue == 'S':
        win = False
    elif firstValue == secondValue:
        win = None
    return win

def rockPaper():
    os.system('cls')
    hand = ('R','P','S')
    computerCount = 0
    userCount = 0
    while (computerCount != 5 or userCount != 5):
        otherHand = input('Rock[r] Paper[p] Scissor[s]: ').upper()
        computerHand = random.choice(hand)
        print(computerHand)
        if otherHand not in hand:
            print('only r for Rock')
            print('only  p for Paper')
            print('only s for Scissor')
        else:
            if rockPaperRule(otherHand,computerHand) == True:
                userCount = userCount + 1
                print('User Wins')
                print (f'computer {computerCount} user {userCount}')
            elif rockPaperRule(otherHand,computerHand) == None:
                print('Stalemates')
            else:
                computerCount = computerCount + 1
                print('Computer Wins')
                print (f'computer {computerCount} user {userCount}')
        if computerCount == 5:
            os.system('cls')
            print("Computer Win")
            print('Good Luck Next Time')
            break
        if userCount == 5:
            os.system('cls')
            print("User Win")
            print('Nice Game')
            break
    print()
    print('To Play Again Press 2')
    print('To Exit Press 3')




os.system('cls')
print('Hello')
print('List of Games')
print('1. Guess Game')
print('2. Rock Paper Scissor')
print('3. Exit')
choose = 0
while (choose != 3):
    try:
        choose = int(input('>: '))
        if choose == 1:
            guessNumber()
        elif choose == 2:
            rockPaper()
        elif choose == 3:
            print('Bye Bye')
            print()
            print()
            print()
            break
        else:
            print('Please only Select the Number from the List')
    except ValueError:
        print('Please only Input Numbers Not Strings')