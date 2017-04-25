# Hunt the Wumpus, by Gregory Yob. Written in 1973
# This Python port by David Miller, 2017

import random
import sys

# Define game variables. They are populated later.
neighbors = [None]*21
bat_locations = [None]*2
pit_locations = [None]*2
wumpus_location = None
location = None

# Main game loop
def main():
  maybe_print_instructions()
  setup_map()
  while True:
    place_objects()
    done = False
    while (not done):
      done = play_one_turn()

    again = get_yes_no("\nWant to play again?")
    if not again:
      sys.exit()

# Choose locations for bats, pits, Wumpus. At the beginning, no two objects are in the
# same room. As the game evolves, you and the Wumpus can move.
def place_objects():
  global location, wumpus_location, bat_locations, pit_locations
  rooms = range(1, 21)
  random.shuffle(rooms)
  location = rooms[0]
  wumpus_location = rooms[1]
  pit_locations = set([rooms[2], rooms[3]])
  bat_locations = set([rooms[4], rooms[5]])

def play_one_turn():
  print_status()
  action = get_action()
  if action == "S":
    return play_shoot()
  else:
    return play_move()

def print_status():
  print "\nYou are in room %d" % location
  near = neighbors[location]
  print "Tunnels lead to %d\t%d\t%d" % (near[0], near[1], near[2])
  if near[0] in bat_locations or near[1] in bat_locations or near[2] in bat_locations:
    print "Bats nearby!"
  if near[0] in pit_locations or near[1] in pit_locations or near[2] in pit_locations:
    print "I feel a draft."
  if wumpus_location in near:
    print "I smell a Wumpus!"

def play_move():
  destination = get_neighbor(location)
  return resolve_move(destination)
  
def resolve_move(destination):
  global location
  location = destination
  if location in bat_locations:
    return do_bats()
  if location in pit_locations:
    return do_pit()
  if location == wumpus_location:
    print "...Oops! Bumped into a Wumpus!"
    return move_wumpus()

def do_bats():
  print "ZAP -- Super Bat snatch! Elsewhereville for you!"
  return resolve_move(random.randint(1, 20))

def do_pit():
  print "YYYIIIIEEEE . . . fell in pit"
  return lose()

def move_wumpus():
  global wumpus_location
  nearby = neighbors[wumpus_location]
  wumpus_destinations = [wumpus_location, nearby[0], nearby[1], nearby[2]]
  wumpus_location = random.choice(wumpus_destinations)
  if wumpus_location == location:
    print "Tsk tsk tsk- Wumpus got you!"
    return lose()
  else:
    print "It might have run away. Can't have gone too far..."
  return False

def play_shoot():
  num_rooms = get_num_rooms()
  path = [location]
  # The limit is one more than num_rooms because we put the initial location
  # on the path.
  while len(path) < num_rooms + 1:
    room = get_room()
    # Forbid turning around and going back to the room the arrow just came from.
    if len(path) >= 2 and room == path[-2]:
      print "Arrows aren't that crooked -- try another room."
    else:
      path.append(room)
  return resolve_arrow(path)

# Returns True if an arrow in this room ends the game in any way.
def resolve_arrow(target_rooms):
  # Remove the initial room and use it at the arrow starting point.
  arrow_location = target_rooms.pop(0)
  for room in target_rooms:
    if room in neighbors[arrow_location]:
      arrow_location = room
    else:
      arrow_location = random.randint(1, 20)
    if check_for_hit(arrow_location):
      return True
  # None of the rooms had you or the Wumpus.
  print "Missed, but you woke the Wumpus!"
  return move_wumpus()

def check_for_hit(room):
  if room == wumpus_location:
    print "Aha! You got the Wumpus!"
    return win()
  elif room == location:
    print "Ouch! Arrow got you!"
    return lose()
  return False
  
def lose():
  print "Ha ha ha - you lose!"
  return True
  
def win():
  print "Hee hee hee - the Wumpus'll getcha next time!!"
  return True

def get_action():
  choice = None
  while choice not in ["S", "M"]:
    choice = raw_input("Shoot or move (S/M)? ").upper()
  return choice

def get_num_rooms():
  choice = None
  while choice not in [1, 2, 3, 4, 5]:
    choice = safe_string_to_int(input("Number of rooms (1-5)? "))
  return choice
  
def get_room():
  choice = None
  valid = range(1, 21)
  while choice not in valid:
    choice = safe_string_to_int(raw_input("Room #: "))
    if choice not in valid:
      print "Not a valid choice. Try again."
  return choice

def get_neighbor(location):
  choice = None
  valid = neighbors[location]
  while choice not in valid:
    choice = safe_string_to_int(raw_input("Where to? "))
    if choice not in valid:
      print "Not possible. Try again."
  return choice

def get_yes_no(message):
  choice = None
  valid = ["Y", "N"]
  while choice not in valid:
    choice = raw_input("%s (Y-N)" % message).upper()
  return choice == "Y"

# Normally python would crash the program if we tried to convert
# a string that doesn't represent an int (like "hello") to an int.
# This returns 0 instead. 0 is not a valid option anywhere we call
# safe_string_to_int (it's not a room or a number of rooms you can
# shoot an arrow), so we'll end up asking the user to try again if
# they enter anything that is not a number.
def safe_string_to_int(s):
  try: 
    value = int(s)
    return value
  except ValueError:
    return 0

# The rooms lie on the vertices of a dodecahedron.
def setup_map():
  neighbors[1] = [2,5,8]
  neighbors[2] = [1,3,10]
  neighbors[3] = [2,4,12]
  neighbors[4] = [3,5,14]
  neighbors[5] = [1,4,6]
  neighbors[6] = [5,7,15]
  neighbors[7] = [6,8,17]
  neighbors[8] = [1,7,9]
  neighbors[9] = [8,10,18]
  neighbors[10] = [2,9,11]
  neighbors[11] = [10,12,19]
  neighbors[12] = [3,11,13]
  neighbors[13] = [12,14,20]
  neighbors[14] = [4,13,15]
  neighbors[15] = [6,14,16]
  neighbors[16] = [15,17,20]
  neighbors[17] = [7,16,18]
  neighbors[18] = [9,17,19]
  neighbors[19] = [11,18,20]
  neighbors[20] = [13,16,19]
  # Room 0 isn't a real room, we just have it so we can use rooms #1-20
  # as the real rooms.
  neighbors[0] = None

def maybe_print_instructions():
  wanted = get_yes_no("Instructions?")
  if (wanted):
    print """
Welcome to Hunt the Wumpus!

The Wumpus lives in a cave of 20 rooms. Each room has 3 tunnels leading to
other rooms. (Look at a dodecahedron to see how this works-if you don't
know what a dodecahedron is, ask someone).

HAZARDS:

Bottomless pits - two rooms have bottomless pits in them. If you go there,
  you fall into the pit (& lose!)

Super bats - two other rooms have super bats. If you go there, a bat grabs
  you and takes you to some other room at random (which might be
  troublesome).
    
WUMPUS:

The Wumpus is not bothered by the hazards (it has sucker feet and is too
big for a bat to lift). Usually it is asleep. Two things wake it up: your
entering its room or your shooting an arrow. If the wumpus wakes, it moves
one room or stays still. After that, if it is where you are, it eats you up
(& you lose!) 

YOU:

Each turn you may move or shoot a "crooked arrow".
  Moving: You can go one room (through one tunnel).

Arrows: You have 5 arrows. You lose when you run out. Each arrow can go
  from 1 to 5 rooms. You aim by telling the computer the room numbers you
  want the arrow to go to. If the arrow can't go that way (ie no tunnel) it
  moves at ramdom to the next room.  
  
  If the arrow hits the wumpus, you win.
  If the arrow hits you, you lose.

WARNINGS:
    When you are one room away from wumpus or hazard, the computer says:

  Wumpus- 'I smell a wumpus'
  Bat - 'Bats nearby'
  Pit - 'I feel a draft'
"""

# Start the actual program
main()
