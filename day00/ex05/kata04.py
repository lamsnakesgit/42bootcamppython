import sys

t = ( 0, 4, 132.42222, 10000, 12345.67)

print("day_0" + str(t[0]) + ", ex_0" + str(t[1]) + " : ", end="")
print("%.2f" % t[2], end=" ")
# print("%.2e" % t[3], t[4]) # only 1st arg formatted
print("%.2e %.2e" % (t[3], t[4]))

# print(" , " + "{.2f}".format(t[2]))
# sys.stdout.write(" , " + format(t[3], ".2e"))# + "\n")
