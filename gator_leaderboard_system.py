from AVLTree import AVLTree
import os, sys

leaderboard_order = AVLTree()
player_lookup = {}
outputs = []


def initialize():
    global leaderboard_order, player_lookup
    leaderboard_order = AVLTree()
    player_lookup = {}


def insert_player(score, player_id):
    score = int(score)
    player_id = int(player_id)

    # Make sure the player id has 6 characters
    if len(str(player_id)) != 6:
        outputs.append("Player ID Must be 6 digits")
        return

    # Check if the player is already in the leaderboard
    if player_id in player_lookup:
        outputs.append("Duplicate player ID")
        return

    # Insert the player into the leaderboard and hash table
    player_lookup[player_id] = score
    leaderboard_order.insert(score, player_id)


def remove_player(player_id):
    player_id = int(player_id)

    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(f"Player {player_id} not found.")
        return

    # Get the player's score
    score = player_lookup[player_id]

    # Remove the player from the leaderboard and hash table
    leaderboard_order.delete((score, player_id))
    del player_lookup[player_id]


# Function that adds an amount to the player
def add_score(added_score, player_id):
    added_score = int(added_score)
    player_id = int(player_id)

    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(f"Player {player_id} not found.")
        return

    # Get the player's score and find the new score
    score = int(player_lookup[player_id])
    new_score = added_score + score

    # Update the hash table and leaderboard with the player's new score
    leaderboard_order.delete((score, player_id))
    leaderboard_order.insert(new_score, player_id)
    player_lookup[player_id] = new_score


def get_rank(player_id):
    player_id = int(player_id)

    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(f"Player {player_id} doesn't exist.")
        return

    score = player_lookup[player_id]
    rank = leaderboard_order.rank((score, player_id))
    outputs.append(f"get_rank() of player {player_id} is {rank}")


def get_player_with_rank(k):
    k = int(k)

    # Find the player in the leaderboard with select(k)
    player_node = leaderboard_order.select(k)

    # Check is there is a player with a rank of k
    if player_node is None:
        outputs.append(f"No player with this rank")
        return

    # Find and return the player with rank k
    score, player_id = player_node.key
    outputs.append(f"get_player_with_rank ({k}) = ({score}, {player_id})")


def print_top_k(k):
    # Make sure k is valid
    base_k = int(k)
    k = int(k)
    if k <= 0:
        outputs.append(f"Invalid k: k must be greater than 0")
        return
    else:
        # Print the header line
        outputs.append(f"print_top_k({base_k}):")
        for i in range(1, k + 1):
            player_node = leaderboard_order.select(i)
            if player_node is None:
                break
            score, player_id = player_node.key
            outputs.append(f"|-> ({player_id}, {score}), {i}")


# Command to quit the program
def quit_program():
    outputs.append(f"Program has been terminated. Go Gators!")
    return


# Function for parsing and processing the input files
def process_input(input_filename):
    with open(input_filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            # Parse the input into commands and argument text
            command = line[:line.index("(")]
            arg_text = line[line.index("(") + 1: line.index(")")]

            # Get the arguments
            args = []
            if arg_text:
                args = [arg.strip() for arg in arg_text.split(",")]

            # Call the different functions
            if command == "initialize":
                initialize()

            elif command == "insert_player":
                score, player_id = int(args[0]), int(args[1])
                insert_player(score, player_id)

            elif command == "remove_player":
                player_id = int(args[0])
                remove_player(player_id)

            elif command == "add_score":
                added_score = int(args[0])
                player_id = int(args[1])
                add_score(added_score, player_id)

            elif command == "get_rank":
                player_id = int(args[0])
                get_rank(player_id)

            elif command == "get_player_with_rank":
                rank = int(args[0])
                get_player_with_rank(rank)

            elif command == "print_top_k":
                k = int(args[0])
                print_top_k(k)

            elif command == "quit":
                quit_program()
                break


# Function to write the output to the output file
def write_to_output(input_filename):
    # Get the input file's original name
    original_name = os.path.splitext(input_filename)[0]
    # Create the required output file name
    output_filename = f"{original_name}_output_file.txt"

    # Write the outputs to the output file
    with open(output_filename, "w") as file:
        for line in outputs:
            file.write(line + "\n")


# Main block
if __name__ == "__main__":
    import sys

    input_filename = sys.argv[1]
    process_input(input_filename)
    write_to_output(input_filename)

