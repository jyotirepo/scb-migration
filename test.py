from idlelib import rstrip

#bp = open('blue.txt', 'r')

#[line.rstrip() for line in open('filename.txt')]
lines = [line.rstrip() for line in open('blue.txt')]

#bp.readlines()
print (lines)
x = lines[0]
y = lines[1]
z = lines[2]
print (x)
print (y)
print (z)
#bp.close()
