import sys
import atm_fun
while 9 :
    try:
        n = int(input('enter value: '))
        match n:
            case 1:
                try:
                    atm_fun.deposit()
                except ValueError:
                    print('do not enter alphabets, special symbols')
                except TypeError:
                    print('check the type')
            case 2:
                try:
                    atm_fun.withdraw()
                except ValueError:
                    print('do not enter alphabets, special symbols')
                except TypeError:
                    print('check the type')
            case 3:
                atm_fun.balence()
            case 4:
                print('program executed')
                sys.exit()
            case _:
                print('invalid input')
    except ValueError:
        print('do not enter alphabets, special symbols')