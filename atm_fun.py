import sys
try:
    bal_amount = 500
    def deposit():
        global bal_amount
        d_money = float(input('enter deposit money: '))
        bal_amount += d_money
        print('balence = ',bal_amount)
        print('{} have deposited to your account'.format(d_money))
    def withdraw():
        global bal_amount
        w_money = float(input('enter withdraw money: '))
        if w_money > bal_amount-500 or w_money <= 500:
            print('insufficient fund')
            sys.exit()
        bal_amount -= w_money
        print('balence = ',bal_amount)
        print('{} have withdrawn'.format(w_money))
    def balence():
        global bal_amount
        print('bal amount = ', bal_amount)
except ValueError:
    print('do not enter alphabets, special symbols')
except TypeError:
    print('check the type')

