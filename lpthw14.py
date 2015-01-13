from sys import argv

script, user_name = argv
prompt = "Answer me, human! -  "

print "Hi, %s. I'm the %s script" % (user_name, script)
print "I would like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
So you say %s about liking me,
You live in %s. You have a %s computer. Good for you.
"""  % (likes, lives, computer)
