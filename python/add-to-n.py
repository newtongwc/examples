n = input("I can add up all the numbers from 1 to any number you like. Enter a number -->")

# Start the total at 1 and the range at 2 so our output looks nice without boring 0+0=0, 0+1=1
# End the range at n+1 so we include n in the total
total = 1
for number in range(2, n+1):
    print "%d+%d=%d" % (total, number, number + total)
    total += number
print "The answer is %d" % total
