import random

class Question:
  def __init__(self, query, top, bottom):
      self.query = query
      self.top = top
      self.bottom = bottom

questions = [
  Question("is there a law against", "cannibalism","flag burning"),
  Question("the beatles are", "still alive", "dead")]

print "Let's play Google Feud!"
while True:
  question = random.choice(questions)  
  print "Guess the more likely completion.\n"
  print "query: %s __________" % question.query
  if random.choice([True, False]):
    answerA = question.top
    answerB = question.bottom
    correct = "A"
  else:
    answerA = question.bottom
    answerB = question.top
    correct = "B"

  print "(A) %s" % answerA
  print "(B) %s" % answerB
  response = raw_input("\n--->")
  if response != "A" and response != "B":
    print "\nYou must choose A or B. Try again with this question."
    continue
  
  if response == correct:
    result = "Correct!"
  else:
    result = "Wrong!"

  print "%s! It's (%s) %s." % (result, correct, question.top)
