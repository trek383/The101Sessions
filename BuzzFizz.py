#!/usr/bin/python

for i in range(1,20):
    # Do we need to print i?
    NeedToPrint = True
    # if i is divisible by 3, then print buzz
    if (i % 3 == 0):
        print "Buzz",
        NeedToPrint = False
    # if i is divisible by 5, then print buzz
    if (i % 5 == 0):
        print "Fizz",
        NeedToPrint = False
    if NeedToPrint:
        print i,
    print
    

