# Author: Aaron Frazier Jr

def show_instructions():
    """ Display the game instructions to the player. """
    print("Adventure Game")
    print("Collect all items to win the game, or be defeated by the villain.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

def show_status(current_room, inventory, rooms):
    """ Display the player's current status. """
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("----------------------")

def main():
    """ Main function containing the game loop. """
    # Initialize the player's starting status
    current_room = 'Great Hall'
    inventory = []

    # Define the rooms and their connections
    rooms = {
        'Great Hall': {'South': 'Bedroom', 'North': 'Dungeon', 'East': 'Kitchen', 'West': 'Library'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar', 'item': 'Armor'},
        'Cellar': {'West': 'Bedroom', 'item': 'Helmet'},
        'Dining Room': {'South': 'Kitchen', 'item': 'Dragon'},  # Villain
        'Dungeon': {'South': 'Great Hall', 'item': 'Sword'},
        'Library': {'East': 'Great Hall', 'item': 'Shield'},
        'Kitchen': {'West': 'Great Hall', 'North': 'Dining Room', 'item': 'Potion'}
    }

    # Number of items to win the game
    required_items = 5

    show_instructions()

    # Main game loop
    while True:
        show_status(current_room, inventory, rooms)

        # Get the player's next move
        move = input("Enter your move: ").strip()

        if move.startswith('go '):
            direction = move.split()[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")
        elif move.startswith('get '):
            item = move.split(' ', 1)[1]
            if 'item' in rooms[current_room] and item == rooms[current_room]['item']:
                inventory.append(item)
                del rooms[current_room]['item']
                print(f"{item} has been added to your inventory.")
            else:
                print("There's no such item here!")
        else:
            print("Invalid move!")

        # Check for game win condition
        if len(inventory) == required_items:
            print("Congratulations! You have collected all items and won the game!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

        # Check for game lose condition
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'Dragon':
            print("NOM NOM...GAME OVER!")
            print("Thanks for playing the game. Hope you enjoyed it.")
            break

if __name__ == "__main__":
    main()
