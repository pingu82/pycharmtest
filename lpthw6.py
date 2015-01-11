# -*- coding utf-8 -*-
x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y

print "i said: %r." % x
print "i also said: '%s'." % y
hilarious = False
joke_eval = "isn't that joke so funny?! %r"

print joke_eval % hilarious
w = "this is the left side of..."
e = "a string with a left side."
print w+e
