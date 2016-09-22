import random
secret = random.randint(1, 10)
limit = 5
guess = 0

print "I am thinking of a number between 1 and 10."
print "What's my number? "

while (guess != secret) and (limit > 0):
    guess = int(raw_input("Your guess? "))
    limit -= 1
    if guess > secret:
        print "Nope, not it. Guess lower!"
    elif guess < secret:
        print "Nope, not it. Guess higher!"
    else:
        print "You guessed it!"
        break
if (limit == 0) and (guess != secret):
    print "You ran out of guesses!"
