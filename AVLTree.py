# This file defines the AVL Tree data structure

class Node:
    # Node constructor
    def __init__(self, score, player_id):
        self.key = (score, player_id)
        self.left = None
        self.right = None
        self.height = 0
        self.size = 1




class AVLTree:
    # Empty tree constructor
    def __init__(self):
        self.root = None

    # Inserts a player into the tree
    def insert(self, score, player_id):
        # 1. If tree is empty → create root
        # 2. Otherwise, → call recursive insert
        pass

    # Helper for inserting player
    def _insert(self, node, score, player_id):
        pass
        # 1. If node is None → create new Node
        # 2. Compare (score, player_id) with node.key
        #    - if higher rank → go left
        #    - else → go right
        # 3. Update height
        # 4. Update size
        # 5. Check balance
        # 6. Perform rotations if needed

    def delete(self, player_id):
        # 1. If player_id not in the tree, output "Player <player_id> not found
        # 2. Find score from the hash table
        # 3. Delete(score, player_id) from the tree and hash table, no output required
        pass

    def _delete(self, node, score, player_id):
        # 1. If node is None
        # 2. Compare key with node.key
        #   - If target should be left, recurse left
        #   - If target should be right, recurse right
        #   - else, found the node to delete
        # 3. Once found, handle the 3 BST delete cases:
        #   - no children
        #   - one child
        #   - two children
        # 4. After deletion:
        #   - update heigh, size, compute balance, rebalance with rotations if necessary
        pass







