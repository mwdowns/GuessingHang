word = "YESTERDAY"
guess = 0
count = 0
solved = "N"
body = "o|--<"


print "The word is %r letters long." % str(len(word))
print "You are of sound mind and body! %r " % body
solution = list(word)
print solution

while (solved == "N") or (count < 6):
    guess = str.upper(raw_input("What letter do you guess? "))
    if guess in solution:
        print "You got one!"
        #this tells the player if the letter shows up in the word and how many times
        print "%r shows up %r times in the word" % (guess, solution.count(guess))
        #this tells the player where the letter shows up in the word
        for i, j in enumerate(solution):
            if j == guess:
                print "%r shows up at postion %r." % (guess, i)
    else:
        count += 1
        body = body[:-1]
        print "Boo! Boo! %r doesn't show up in the word." % guess
        print "You've lost a body part!"
        print body
