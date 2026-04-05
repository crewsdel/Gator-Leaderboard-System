from AVLTree import AVLTree

leaderboard_order = AVLTree()
player_lookup = {}
outputs = []

def initialize():
    global leaderboard_order, player_lookup, outputs
    leaderboard_order = AVLTree()
    player_lookup = {}
    outputs = []

def insert_player(score, player_id):

    # Make sure the player id has 6 characters
    if len(str(player_id)) != 6:
        return print("Player ID Must be 6 digits")

    # Check if the player is already in the leaderboard
    if leaderboard_order.search_by_key((score, player_id)):
        return print("Duplicate player ID")

    # Insert the player into the leaderboard and hash table
    leaderboard_order.insert(score, player_id)
    player_lookup.update({player_id: score})
    return None

def remove_player(player_id):
    # Check if the player is in the hash table
    if player_id not in player_lookup:
        outputs.append(print(f"Player {player_id} not found."))
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
        outputs.append(f"Player {player_id} not found.")
        return

    # Get the player's score and find the new score
    score = player_lookup.get(player_id)
    new_score = added_score + score

    # Update the hash table and leaderboard with the player's new score
    player_lookup[player_id] = new_score
    leaderboard_order.delete((score, player_id))
    leaderboard_order.insert(new_score, player_id)

def get_rank(player_id):
    if player_id not in player_lookup:
        return outputs.append(f"Player {player_id} doesn't exist.")


    score = player_lookup.get(player_id)
    rank = leaderboard_order.rank((score, player_id))
    return outputs.append(f"get_rank() of player {player_id} is {rank}")



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
            outputs.append(f"get_player_with_rank({k}) = ({score}, {player_id})")








