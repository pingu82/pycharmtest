# -*- coding: utf-8 -*-
from sys import argv

script, num1, num2 = argv

print script, "multipliserer to tall som gis som argumenter på kommandolinjen."
print "Bruk: python", script, "<første tall> <andre tall>\n"
print "Første tall er:", num1
print "Andre tall er:", num2
# konverterer input fra string til int.
result = int(num1) * int(num2)
print "Produktet av", num1, "og", num2, "er", result
