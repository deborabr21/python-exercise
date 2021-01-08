#!/usr/bin/env python3

# imports always go at the top of your code
import requests


def main():
    while True:
        print("""
        \nEnter your Pokemon:
        ditto
        pikachu
        bulbasaur
        venusaur
        charmander
        charizard
        blastoise
        butterfree
        beedrill
        rattata
        kakuna
        """)
        name = input(">").strip().lower()
        try:
            pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
            break
        except:
            print(f"Sorry, {name} is not a valid pokemon!")

    # Print pokemon name
    print(pokeapi["name"])

    # print all the api for the pokemon selected
    # print(pokeapi)

    # Print the URL to "front_default", which is a link to an image of your Pokemon
    print("Link to picture: ", pokeapi["sprites"]["front_default"])

    # Return a count of how many "game_indices" the selected Pokemon has been in
    indices = len(pokeapi["game_indices"])
    print(f"{name} appeared in {indices} games!")

    # Print out the "name"s of ALL the selected Pokemon's "moves".
    for x in pokeapi["moves"]:
        print(x["move"]["name"])


main()
