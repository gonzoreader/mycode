#!/usr/bin/env python3
## create file object in "r"ead mode
usin = input('what file to open?')

with open(f"{usin}", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

