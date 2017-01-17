# This program gets ready to play hide and seek by counting up by fives.
# It was written as a Daily Programming Exercise.

# Use to pause between counts
import time

print "Now everybody try to find a good hiding place."
print "This ol' tree is going to be the base."
print "I'm going to close my eyes and hide my face"
print "And count to a hundred by fives."
print "Ready? Go!"
print

for i in range(5, 105, 5):
    print "%d..." % i,
    # pause between counts
    time.sleep(0.5)

print "\n"
print "Ready or not, here I come!"

