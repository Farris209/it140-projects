"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.
current_room = "Great Hall"

# TODO: Create the gameplay loop required by the milestone.
while current_room != "exit":
    print(f"You are in the {current_room}")
    command = input(" Enter your move (go north, go south, go east, go west) or exit: ")

    if command == "exit":
        current_room = "exit"
    elif command.startswith("go "):
        direction = command[3:]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You cannot go that way.")
    else:
        print("Invalid command. Please try again.")
        
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.
