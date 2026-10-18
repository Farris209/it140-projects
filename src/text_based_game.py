# Author: Patrick Farris
# IT 140 Project Two - Full Court Quest


def show_instructions(required_items):
    """Display the story, objective, and supported commands."""
    print("\nFull Court Quest")
    print("It is championship night! Your equipment is scattered in the arena.")
    print(f"Collect all {required_items} items before entering the Basketball Court.")
    print("Enter too early, and the Reigning Champions will defeat you.")
    print("Move: go north, go south, go east, go west")
    print("Collect: get <item name> (for example, get Basketball Shoes)")
    print("Commands ignore capitalization and extra spaces.")


def show_status(current_room, rooms, inventory, required_items):
    """Show the player's location, inventory, available item, and exits."""
    room = rooms[current_room]
    print("\n" + "-" * 50)
    print(f"You are in the {current_room}.")
    print(f"Inventory ({len(inventory)}/{required_items}): {inventory}")
    if "item" in room:
        print(f"You see: {room['item']}")
    else:
        print("There is no equipment to collect here.")
    exits = [direction for direction in room if direction != "item"]
    print("Available moves: " + ", ".join(f"go {direction}" for direction in exits))


def move_player(current_room, direction, rooms):
    """Move only along an exit shown on the Project One map."""
    if direction not in ("north", "south", "east", "west"):
        print("Invalid direction. Use north, south, east, or west.")
    elif direction not in rooms[current_room]:
        print("You cannot go that way.")
    else:
        current_room = rooms[current_room][direction]
        print(f"You moved to the {current_room}.")
    return current_room


def get_item(current_room, requested_item, rooms, inventory):
    """Collect the matching room item once, following the get-item design."""
    room_item = rooms[current_room].get("item")
    if room_item is None:
        print("There is no equipment to collect in this room.")
    elif requested_item.casefold() != room_item.casefold():
        print(f"That item is not available here. You see: {room_item}")
    else:
        inventory.append(room_item)
        # Removing the collected item prevents duplicate inventory entries.
        del rooms[current_room]["item"]
        print(f"{room_item} added to inventory.")


def main():
    """Run the game until the player encounters the Reigning Champions."""
    # Connections and item locations match the Map tab of Project One.
    # The Locker Room and Basketball Court contain no collectible items.
    rooms = {
        "Locker Room": {
            "west": "Training Room", "north": "Basketball Court"
        },
        "Training Room": {
            "east": "Locker Room", "north": "Equipment Room",
            "item": "Basketball"
        },
        "Equipment Room": {
            "south": "Training Room", "north": "Weight Room", "item": "Jersey"
        },
        "Weight Room": {
            "south": "Equipment Room", "east": "Coach's Office",
            "item": "Basketball Shoes"
        },
        "Coach's Office": {
            "west": "Weight Room", "east": "Medical Room", "item": "Playbook"
        },
        "Medical Room": {
            "west": "Coach's Office", "south": "Film Room", "item": "Ankle Brace"
        },
        "Film Room": {
            "north": "Medical Room", "west": "Basketball Court", "item": "Headband"
        },
        "Basketball Court": {"south": "Locker Room", "east": "Film Room"}
    }
    current_room = "Locker Room"
    inventory = []
    # Calculate this before any items are removed from the room dictionary.
    required_items = sum(1 for room in rooms.values() if "item" in room)
    show_instructions(required_items)

    while True:
        show_status(current_room, rooms, inventory, required_items)

        # Entering the villain room ends the game before another command.
        if current_room == "Basketball Court":
            if len(inventory) == required_items:
                print("\nCongratulations! You collected all six items and")
                print("defeated the Reigning Champions. You win the championship!")
            else:
                missing_items = required_items - len(inventory)
                print(f"\nYou entered the court missing {missing_items} item(s).")
                print("The Reigning Champions defeat you. GAME OVER!")
            break

        try:
            # Split once so multiword item names remain a single argument.
            command = " ".join(input("Enter your move: ").split())
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted.")
            break

        parts = command.split(" ", 1)
        if len(parts) != 2:
            print("Enter go <direction> or get <item name>.")
            continue

        action, argument = parts
        action = action.casefold()
        if action == "go":
            current_room = move_player(current_room, argument.casefold(), rooms)
        elif action == "get":
            get_item(current_room, argument, rooms, inventory)
            if len(inventory) == required_items:
                print("All equipment collected! Enter the Basketball Court to compete.")
        else:
            print("Unknown command. Enter go <direction> or get <item name>.")

    print("Thanks for playing Full Court Quest!")


if __name__ == "__main__":
    main()
