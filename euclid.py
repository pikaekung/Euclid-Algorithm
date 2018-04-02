import random

print("Euclid's Algorithm")

#       RECTANGLE
# --------Width-------
# |                  |
# Height             |
# |                  |
# --------------------

rectangle_width = random.randint(100, 1000)
rectangle_height = random.randint(100, 1000)
loop = 1

if rectangle_width < rectangle_height:
	rectangle_width, rectangle_height = rectangle_height, rectangle_width

print "Rectangle width, height", rectangle_width, rectangle_height
print "Start calculate."

while True:	
	squre_width = rectangle_height
	space_width = rectangle_width % squre_width
	print "Loop %d space width: " % loop, space_width
	if space_width == 0:
		break

	squre_width = space_width
	rectangle_width = rectangle_height
	rectangle_height = space_width
	loop = loop + 1

print "Result GCF = %d" % squre_width
print "End calculate."

