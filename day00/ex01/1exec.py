import sys

if len(sys.argv) < 2:
	exit()

def reversecase(s):
	return s[::-1].swapcase()

n = len(sys.argv) - 1
while n > 0:
	s = sys.argv[n]
	s = reversecase(s)
	# print(s, end="--\n")
	if n != 1:
		print(s, end=' ')
	n -= 1
print(s)
