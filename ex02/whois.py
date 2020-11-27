import sys
import re

if len(sys.argv) < 2:
    exit()

if len(sys.argv) > 2:
    print('ERROR')
    exit()
else:
    #if sys.argv[1].isdigit() == 0:
    # if sys.argv[1].isnumeric() == 0: # fails
    result = re.match("[-+]?\d+$", sys.argv[1])
    if result == 0:
        print('ERROR')
    elif int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
            print("I'm Even")
    elif int(sys.argv[1]) % 2 == 1:
        print("I'm Odd")
    exit()
