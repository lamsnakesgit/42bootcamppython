import string

def operations():
    nums = [int(num) for num in input().split()]
    if len(nums) == 2:
        print(f'{"+Sum:":<15}' + f'{nums[0]+nums[1]}')
        print(f'{"-Difference:":<15}' + f'{nums[0]-nums[1]}')
        print(f'{"*Product:":<15}' + f'{nums[0]*nums[1]}')
        print(f'{"*Quotient:":<15}' + f'{nums[0]/nums[1]}')
        print(f'{"%Remainder:":<15}' + f'{nums[0]%nums[1]}')
    else:
        print("InputError:too many argumnets")
operations()
