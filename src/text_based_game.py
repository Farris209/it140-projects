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
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
    pass


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
        "Coach's Room": {
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
    # TODO: Set the player's starting room.

    # TODO: Create the player's inventory.

    # TODO: Call the instruction function at the appropriate time.

    # TODO: Create the gameplay loop.
    # Within the loop:
    #   - Show player status.
    #   - Prompt for the player's next command.
    #   - Handle valid movement commands.
    #   - Handle valid get-item commands.
    #   - Validate invalid commands.
    #   - Update room/inventory state when appropriate.
    #   - Detect and display the required winning outcome.
    #   - Detect and display the required losing outcome.
    #   - End the loop when the player has won or lost.
    pass


if __name__ == "__main__":
    main()
