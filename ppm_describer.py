import sys

RGB_LENGTH = 3

lines = [line.rstrip('\n') for line in open(sys.argv[1])]

image_size = tuple([int(x) for x in lines[2].split()])
width = image_size[0]
height = image_size[1]

print
print "Image info"
print "----------"
print "File: %s" % sys.argv[1]
print "Height: %s" % str(height)
print "Width: %s" % str(width)
print

rgb_lines = lines[4:]

rgb_list = [rgb_lines[x:x + RGB_LENGTH] for x in range(0, len(rgb_lines), RGB_LENGTH)]
rgb_list = [tuple(int(x[i]) for i in range(RGB_LENGTH)) for x in rgb_list]

palette = [tuple(x) for x in set(tuple(x) for x in rgb_list)]
palette = {x:0 for x in palette}

index = 0

for i in range(width):
	for j in range(height):
		palette[rgb_list[index]] = palette[rgb_list[index]] + 1
		print "(" + str(i + 1) + ", " + str(j + 1) + "): " + str(rgb_list[index])
		index = index + 1

print
print "Palette"
print "-------"
print "Total number of colors: %s" % str(len(palette))
print
for key in sorted(palette):
    print "%s: %s px  (%.2f %%)" % (key, palette[key], palette[key] / float(index) * 100)
