import string

def operations():
    nums = [int(num) for num in input().split()]
    if len(nums) == 2:
        print('Sum:' '%9s' % f"{nums[0]+nums[1]}")
        print('Difference:' '%2s' % f"{nums[0]-nums[1]}")
        print('Product:' '%8s' % f"{nums[0]*nums[1]}")
        print('Product:'.ljust(12 + 2) + f'{nums[0]*nums[1]}')
        #print('Quotient:ii' '{:<15}'.format("quot:")  f'{nums[0]+nums[1]}')
        print(f'{"Quotient:":<15}' + f'{nums[0]/nums[1]}')
        print('Remainder:'.ljust(len("difference") + 2) + f'{nums[0]%nums[1]}')
        print("randstr".ljust(4,'p'))
        print(len("difference") + 2)
    else:
        print("InputError:too many argumnets")
operations()
