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

    # Make sure the player id has 6 characters
    if len(str(player_id)) != 6:
        return print("Player ID Must be 6 digits")

    # Check if the player is already in the leaderboard
    if player_id in player_lookup:
        return print("Duplicate player ID")

    # Insert the player into the leaderboard and hash table
    leaderboard_order.insert(score, player_id)
    player_lookup.update({player_id: score})
    return None

def remove_player(player_id):
    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(print(f"Player {player_id} not found REMOVE PLAYER"))
        return

    # Get the player's score
    score = player_lookup.get(player_id)

    # Remove the player from the leaderboard and hash table
    leaderboard_order.delete((score, player_id))
    del player_lookup[player_id]

# Function that adds an amount to the player
def add_score(added_score, player_id):
    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(f"Player {player_id} not found ADD SCORE")
        return

    # Get the player's score and find the new score
    score = player_lookup.get(player_id)
    new_score = added_score + score

    # Update the hash table and leaderboard with the player's new score
    player_lookup[player_id] = new_score
    leaderboard_order.delete((score, player_id))
    leaderboard_order.insert(new_score, player_id)

def get_rank(player_id):
    print(player_lookup.get(player_id))
    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(f"Player {player_id} doesn't exist.")
        return

    score = player_lookup[player_id]
    print(score)
    rank = leaderboard_order.rank((score, player_id))
    print(rank)
    outputs.append(f"get_rank() of player {player_id} is {rank}")
    print(outputs)


def get_player_with_rank(k):
    # Find the player in the leaderboard with select(k)
    player_node = leaderboard_order.select(k)
    if player_node is None:
        outputs.append(f"No player with this rank")
        return


    score, player_id = player_node.key
    outputs.append(f"get_player_with_rank({k}) = ({score}, {player_id})")


def print_top_k(k):
    # Make sure k is valid
    if k <= 0:
        outputs.append(f"Invalid k: k must be greater than 0")
        return
    else:
        # Print the header line
        outputs.append(f"print_top_k({k}):")
        for i in range(1, k + 1):
            player_node = leaderboard_order.select(i)
            if player_node is None:
                break
            score, player_id = player_node.key
            rank = leaderboard_order.rank((score, player_id))
            outputs.append(f"-> ({player_id}, {score}), {rank}")

# Command to quit the program
def quit_program():
    outputs.append(f"Program has been terminated. Go Gators!")
    exit(0)


def process_input(input_filename):
    with open(input_filename, "r") as file:
        for line in file:
            line = line.strip()


            if not line:
                continue

            command = line[:line.index("(")]
            arg_text = line[line.index("(") + 1: line.index(")")]

            args = []
            if arg_text:
                args = [arg.strip() for arg in arg_text.split(",")]

            if command == "initialize":
                initialize()

            elif command == "insert_player":
                score, player_id = args[0], args[1]
                insert_player(score, player_id)

            elif command == "remove_player":
                player_id = args[0]
                remove_player(player_id)

            elif command == "add_score":
                added_score = args[0]
                player_id = args[1]
                add_score(added_score, player_id)

            elif command == "get_rank":
                player_id = args[0]
                get_rank(player_id)

            elif command == "get_player_with_rank":
                rank = args[0]
                get_player_with_rank(rank)

            elif command == "print_top_k":
                k = args[0]
                print_top_k(k)

            elif command == "quit":
                quit_program()
                break


def write_to_output(input_filename):
    original_name = os.path.splitext(input_filename)[0]
    output_filename = f"{original_name}_output_file.txt"
    with open(output_filename, "w") as file:

        for line in outputs:
            print(line)
            file.write(line + "\n")