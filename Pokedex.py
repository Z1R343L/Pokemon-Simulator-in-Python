# This file reads through the Pokemon spreadsheet, then creates a list of all the Pokemon names called "pokedex"
# "Pokedex" is used later to make sure user-selected Pokemon are actually in the spreadsheet

pokedex = []
with open("Kanto Pokemon Spreadsheet.csv", 'r') as fin:
    pokemonDictionary = {}

    # Creating a dictionary with each Pokemon's name as a key
    for line in fin:
        line = line.strip()
        pokeList = line.split(",")
        pokemonDictionary[pokeList[1]] = pokeList
# Taking the keys from above, turning them into a list, and sorting them
for key, value in pokemonDictionary.items():
    pokedex.append(value[1].lower())
    pokedex.sort()