secret = 5

print "I am thinking of a number between 1 and 10."
print "What's my number?"
guess = int(raw_input("Your guess? "))

while (guess != secret):
    if guess < secret:
        print "Nope, not it! Guess higher!"
        guess = int(raw_input("Your guess? "))
    else:
        print "Nope, not it! Guess lower!"
        guess = int(raw_input("Your guess? "))

print "You got it!"
