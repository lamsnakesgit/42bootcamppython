import sys
import string

def operations():
    if len(sys.argv) < 3:
        print("InputError: two arguments needed")
    elif len(sys.argv) == 3:
        try:
            print(f'{"Sum:":<15}' + f'{int(sys.argv[1])+int(sys.argv[2])}')
            print(f'{"Difference:":<15}' + f'{int(sys.argv[1])-int(sys.argv[2])}')
            print(f'{"Product:":<15}' + f'{int(sys.argv[2])*int(sys.argv[1])}')
            print(f'{"Quotient:":<15}' + f'{int(sys.argv[1])/int(sys.argv[2])}')
            print(f'{"Remainder:":<15}' + f'{int(sys.argv[1])%int(sys.argv[2])}')
        except ValueError:
            print("InputError: only numbers")
    else:
        print("InputError:too many argumnets")
operations()
