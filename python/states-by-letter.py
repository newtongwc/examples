# A solution to a Daily Programming Exercise:
#
states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut', 'Delaware',
        'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
        'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri', 'Mississippi', 'Montana',
        'North Carolina', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'New Mexico', 'Nevada',
        'New York', 'Ohio', 'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
        'Tennessee', 'Texas', 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming'
]

user_letter = ""
while len(user_letter) != 1:
    user_letter = raw_input('Enter a single letter: ').lower()

print "These states start with %c:" % user_letter
for state in states:
    if state.lower().startswith(user_letter):
        print state

print
print "These states contain the letter %c:" % user_letter
for state in states:
    if user_letter in state.lower():
        print state
