#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


def main():

    char_name = input('Which character do you want to know about? (Starlord, Mystique, Hulk)\n')
    char_stat = input('What statistic do you want to know about? (real name, powers, archenemy)\n')
    print(f"{char_name}'s {char_stat} is: ") 

    print(marvelchars.get(char_name).get(char_stat))



main()
