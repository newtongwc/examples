import random

targets = ["apple", "banana", "orange", "pear"]
for target in targets:
    entry = None
    while entry != target:
        entry = raw_input("Type \"%s\":\n----> " % target)
    print "You got it! Now try another.\n"
