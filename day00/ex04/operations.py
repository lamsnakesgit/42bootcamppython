import sys
import string

def usage():
    print("Usage: python operations.py <number1> <number2>\nExample:\n" + "  python operations.py 10 3")

def operations():
    if len(sys.argv) < 3:
        print("InputError: two arguments needed") # optional
        usage()
    elif len(sys.argv) == 3:
        try:
            print(f'{"Sum:":<15}' + f'{int(sys.argv[1])+int(sys.argv[2])}')
            print(f'{"Difference:":<15}' + f'{int(sys.argv[1])-int(sys.argv[2])}')
            print(f'{"Product:":<15}' + f'{int(sys.argv[2])*int(sys.argv[1])}')
            if int(sys.argv[2]) == 0:
                print(f'{"Quotient:":<15}' + "ERROR (div by zero)")
                print(f'{"Remainder:":<15}' +"ERROR (modulo by zero)")
            else:
                print(f'{"Quotient:":<15}' + f'{int(sys.argv[1])/int(sys.argv[2])}')
                print(f'{"Remainder:":<15}' + f'{int(sys.argv[1])%int(sys.argv[2])}')
        except ValueError:
            print("InputError: only numbers\n")
            usage()
    else:
        print("InputError:too many argumnets\n")
        usage()
operations()
