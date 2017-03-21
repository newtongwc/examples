import random

print "Welcome to Word Scramble!\n\n"
print "Try unscrambling these letters to make an english word.\n"

words = ["apple", "banana", "pear", "apricot"]

while True:
  word = random.choice(words)
  letters = list(word)
  random.shuffle(letters)
  scramble = ''.join(letters)
  
  print "Scrambled: %s" % scramble
  guess = raw_input("What word is this? ")
  if guess == word:
    print "\nThat's right!\n"
  else:
    print "\nNo, the word was %s\n" % word
  
