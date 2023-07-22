
from colorama import Fore, Back, Style
def returnNumber():
    inputNumber = input('Enter first number: ')
    secondNumber = input('Enter second number: ')


    try:
        print(Fore.GREEN + inputNumber+' divided by '+ secondNumber + ' is: \n')
        print(Style.BRIGHT + str(int(inputNumber)/int(secondNumber)))
    except ZeroDivisionError:
        print(Fore.RED + 'Divide by zero')
    else:
        print(Style.NORMAL +Fore.GREEN + 'execute when no exceptin occur')

    finally:
        print(Style.NORMAL+Fore.GREEN + 'Finally code is always executing...')



returnNumber()

