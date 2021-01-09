#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
OUTBREAK
You are a high ranking government official responding to an pandemic outbreak of an infectious disease that is 
affecting the world. You must travel through countries in order to find the correct combination of drugs and tools to
create a vaccine that will end the outbreak.  

In order to find the correct combination of drugs, you must travel to different countries to collect the ingredients 
and then follow the process below in order to create a vaccine. Be aware that some countries may be plagued with crime.

Steps for creating a vaccine:
1.  Generate the antigen by growing it in cells.
2.  Release the antigen from the cells and isolate it from the material used in its growth.
3.  Purify the antigens.
4.  Strengthen immune response by adding adjuvant.
5.  Distribute the vaccine across the world.

========
Commands:
  go [direction]
  get [item]
  do [steps]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in ' + currentCountry)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print the current steps you have completed to create a vaccine
    print('Steps : ' + str(vaccine))
    # print an item if there is one
    if "item" in countries[currentCountry]:
        print('You see a ' + countries[currentCountry]['item'])
    print("---------------------------")
    # print an step if there is one
    if "steps" in countries[currentCountry]:
        print('Step ' + countries[currentCountry]['steps'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a list of steps needed to create the vaccine, which is initially empty
vaccine = []

## A dictionary linking a room to other rooms
countries = {

    'China': {
        'west': 'Russia',
        'south': 'Australia',
        'steps': 'Distribute'
    },

    'Russia': {
        'east': 'China',
        'west': 'United States',
        'item': 'thimerosal',
        'steps': '3 - Purify'
    },

    'United States': {
        'east': 'Russia',
        'south': 'Brazil',
        'item': 'neomycin',
        'steps': '2 - Release'
    },

    'Brazil': {
        'north': 'United States',
        'east': 'Australia',
        'west': 'Peru',
        'item': 'egg protein',
        'steps': '1 - Generate'
    },

    'Peru': {
        'north': 'United States',
        'east': 'Brazil',
    },

    'Australia': {
        'north': 'China',
        'west': 'Brazil',
        'item': 'polysorbate',
        'steps': '4 - Strengthen'
    },

}

# start the player in the Hall
currentCountry = 'China'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in countries[currentCountry]:
            # set the current country to the new country
            currentCountry = countries[currentCountry][move[1]]
        # there is no door (link) to the new country
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the country contains an item, and the item is the one they want to get
        if "item" in countries[currentCountry] and move[1] in countries[currentCountry]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print('You got the ' + move[1])
            # delete the item from the country
            del countries[currentCountry]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'do' first
    if move[0] == 'do':
        # if the country contains a step, and the step is the one they want to do
        if "steps" in countries[currentCountry] and move[1] in countries[currentCountry]['steps']:
            # add the step to their vaccine inventory
            vaccine += [move[1]]
            # display a helpful message
            print('You completed the ' + move[1])
            # delete the step from the country
            del countries[currentCountry]['steps']
        # otherwise, if the step isn't there to do
        else:
            # tell them they can't get it
            print('Can\'t do ' + move[1] + '!')

    ## If a player enters a country riddled with crime
    if currentCountry == 'Peru':
        print('Oh no....all your inventory has been stolen... GAME OVER!')
        break

    ## Define how a player can win
    if currentCountry == 'China' and 'generate antigen' in vaccine and 'release and isolate' in vaccine and 'purify' \
            in vaccine and 'strengthen' in vaccine and 'distribute' in vaccine and 'thimerosal' in inventory and \
            'polysorbate'in inventory and 'egg protein'in inventory and 'neomycin' in inventory:
        print('You have found all the vaccine ingredients and created a cure for this pandemic. The world thanks you!!')
        break
