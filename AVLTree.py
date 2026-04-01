# This file defines the AVL Tree data structure

class Node:
    # Node constructor
    def __init__(self, score, player_id):
        self.key = (score, player_id)
        self.left = None
        self.right = None
        self.height = 0
        self.size = 1

# Helper method to return the node height
def height(node):
    if node is None:
        height = -1
        return height
    else:
        height = node.height
    return height

# Helper method to return node size
def size(node):
    if node is None:
        size = 0
        return size
    else:
        size = node.size
        return size

# Helper method to calculate a node's balance
def balance(node):
    balance = height(node.left) - height(node.right)
    return balance

# Helper method to update a node's height and size after its children have been modified
def update_node(node):
    node.height = 1 + max(height(node.left), height(node.right))
    node.size = 1 + size(node.left) + size(node.right)


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
        # Base case
        if node is None:
            node = Node(score, player_id)

        if score > node.key:
            node.left = self._insert(node.left, score, player_id)
        elif score == node.key and player_id < node.key:
            node.left = self._insert(node.left, score, player_id)
        else:
            node.right = self._insert(node.right, score, player_id)

        return node
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







