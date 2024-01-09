#!/usr/bin/env python3

def main():
    counter = 0
    with open('dracula.txt', 'r') as vampfile:
        with open('vampytimes.txt','w') as newfile:
            for line in vampfile:
                if 'vampire' in line.lower():
                    counter += 1
                    print(line.strip())
                    print(counter)
                    newfile.write(line)
main()
