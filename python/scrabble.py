# A daily programming exercise for Newton Girls Who Code Club
value_of_tile = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2,
                 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1,
                 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
                 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

print "Enter a word and I'll compute the value in Scrabble."
while True:
    word = raw_input("Enter a word: ")
    total = 0
    print
    for letter in word.upper():
        value = value_of_tile[letter]
        print "%s is worth %d" % (letter, value)
        total = total + value
    print
    print "The total is %d" % total
