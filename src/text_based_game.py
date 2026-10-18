"""Project Two starter for the student's text-based adventure game."""

# Patrick Farris


def show_instructions():
    """Display the game objective and available commands."""
    print("Full Court Quest")
    print("Collect all six equipment items before entering the Basketball Court.")
    print("Enter the court too early, and the Reigning Champions defeat you!")
    print("Move commands: go north, go south, go east, go west")
    print("Collect an item: get <item name>")


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])
    print("--------------------")


def main():
    """Run the main gameplay loop."""
    # TODO: Create the full room/item dictionary from your Project One map.
    rooms = {
        "Locker Room": {"west": "Training Room", "north": "Basketball Court"},
        "Training Room": {
            "east": "Locker Room",
            "north": "Equipment Room",
            "item": "Basketball"
        },
        "Equipment Room": {
            "south": "Training Room",
            "north": "Weight Room",
            "item": "Jersey"
        },
        "Weight Room": {
            "south": "Equipment Room",
            "east": "Coach's Office",
            "item": "Basketball Shoes"
        },
        "Coach's Office": {
            "west": "Weight Room",
            "east": "Medical Room",
            "item": "Playbook"
        },
        "Medical Room": {
            "west": "Coach's Office",
            "south": "Film Room",
            "item": "Ankle Brace"
        },
         "Film Room": {
            "north": "Medical Room",
            "west": "Basketball Court",
            "item": "Headband"
         },
        "Basketball Court": {
            "south": "Locker Room",
            "east": "Film Room",
         },
    }
    
    current_room = "Locker Room"
    inventory = []
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        if current_room == "Basketball Court":
            if len(inventory) == 6:
                print("You defeated the Reigning Champions!")
                print("Congratualtions! You win the Championship!")
            else:
                print("You entered the court without all six items.")
                print("The Reigning Champions defeat you. GAME OVER!")
            break
            
        command = input("Enter your move: ").strip()
        parts = command.split(maxsplit=1)

        if len(parts) != 2:
            print("Enter go <direction> or get <item name>.")
            continue

        action = parts[0].lower()
        argument = parts[1].lower()

        if action == "go":
            if argument not in ("north", "south", "east", "west"):
                print("Use north, south, east, or west.")
            elif argument in rooms[current_room]:
                current_room = rooms[current_room][argument]
            else:
                print("You cannot go that way.")

        elif action == "get":
            room_item = rooms[current_room].get("item")
            if room_item is None:
                print("There is no item to collect in this room.")
            elif argument == room_item.lower():
                inventory.append(room_item)
                del rooms[current_room]["item"]
                print(room_item, "added to inventory.")
            else:
                print("That item is not available in this room.")

        else:
            print("Unknown command. Use go <direction> or get <item name>.")
            
    print("Thanks for playing Full Court Quest!")

if __name__ == "__main__":
    main()
