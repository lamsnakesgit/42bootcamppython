import sys

if len(sys.argv) < 2:
	exit()

def reversecase(s):
	return s[::-1].swapcase()

n = len(sys.argv) - 1
args = [reversecase(sys.argv[n])]
while n > 0:
	s = sys.argv[n]
	s = reversecase(s)
	prev = s
	# print(s, end="--\n")
	if n != 1:# and n != len(sys.argv) - 1:
		#print(s, end=' ')
		args.append(prev)#s = ' '.join(s, "")
	n -= 1
#print(s)
print(' '.join(args))
