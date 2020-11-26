import sys
# get in cycle argv[i] process each str
if len(sys.argv) < 2:
	exit()

def reversecase(s):
	return s[::-1].swapcase()

n = len(sys.argv) - 1
# s = sys.argv[n]#input()
# output = 
while n > 1:
	s = s[::-1]
	# print(s, end="--\n")
	if n != 1:
		print(s, end=' ')
	n -= 1
print()
