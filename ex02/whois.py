import sys
import re

# isinstance might be used

if len(sys.argv) < 2:
    exit()

if len(sys.argv) > 2:
    print('ERROR')
    exit()
else:
    result = re.match("[-+]?\d+$", sys.argv[1])
    #if sys.argv[1].isdigit() == 0:
    # if sys.argv[1].isnumeric() == 0: # fails
    if result == 0:
        print('ERROR')
    #elif sys.argv
    elif int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
            print("I'm Even")
    elif int(sys.argv[1]) % 2 == 1:
        print("I'm Odd")
    exit()
