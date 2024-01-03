#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]



def chmain():

    #eyes
    v1 = challenge[2][1]
    #goggles
    v2 = challenge[2][0]
    #nothing
    v3 = challenge[3]

    print(f"My {v1}! The {v2} do {v3}!")

chmain()

def trmain():

    #eyes
    v4 = trial[2].get("goggles")
    #goggles
    v5 = trial[2].get("eyes")
    #nothing
    v6 = trial[3]

    print(f"My {v4}! The {v5} do {v6}!")

trmain()

def nimain():

    #eyes
    v7 = nightmare[0].get("user").get("name").get("first")
    #goggles
    v8 = nightmare[0].get("kumquat")
    #nothing
    v9 = nightmare[0].get("d")

    print(f"My {v7}! The {v8} do {v9}!")

nimain()
