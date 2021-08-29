import random,os

def submenu():
        opt=input('1. Back to menu\n2.Exit')
        if opt=='1':
            pass
        elif opt=='2':
            status=False

dice=["┌───────┐\n│\t│\n│\t│\n│   O\t│\n│\t│\n│\t│\n└───────┘","┌───────┐\n│\t│\n│   O\t│\n│\t│\n│   O\t│\n│\t│\n└───────┘","┌───────┐\n│\t│\n│   O\t│\n│\t│\n│ O   O │\n│\t│\n└───────┘","┌───────┐\n│\t│\n│ O   O │\n│\t│\n│ O   O │\n│\t│\n└───────┘","┌───────┐\n│\t│\n│ O   O │\n│   O\t│\n│ O   O │\n│\t│\n└───────┘","┌───────┐\n│\t│\n│ O   O │\n│ O   O │\n│ O   O │\n│\t│\n└───────┘"]
status=True
os.system('cls')
while status:
    os.system('cls')
    print('This is a dice simulator.\n Select how many dices you want: \n\t1. One dice\n\t2. Two dices\n\t3. Exit')
    dices=input()
    if dices == '1':
        print(random.choice(dice),'\n')
        submenu()
    elif dices == '2':
        print(random.choice(dice), random.choice(dice),'\n')
        submenu()
    elif dices=='3':
        status=False
    else:
        os.system('cls')
        print('Incorrect number. Enter another.\n \n \n')
