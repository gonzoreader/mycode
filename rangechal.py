#!/usr/bin/env python3


def main():
    usin = int(input('How many bottles of beer should we start counting from?'))
    for x in range(usin, 0, -1):
        print(f'{x} bottles of beer on the wall!')
        print(f'{x} bottles of beer on the wall! {x} bottles of beer! You take one down, pass it around!')
main()
