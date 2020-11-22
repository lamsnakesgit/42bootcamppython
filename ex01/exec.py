import sys
# get in cycle argv[i] process each str
s = sys.argv[1]#input()
i = len(s) - 1
while i >= 0:
	if s[i].islower() == 1:#int(s[i]) >= 65 and int(s[i]) <= 90:
		print(s[i].upper(), end='')#(int(s[i]) + 32)
	else:
		print(s[i].lower(), end='')
	i -= 1
print()
