# This file defines the AVL Tree data structure

class Node:
    # Node constructor
    def __init__(self, score, player_id):
        self.key = (score, player_id)
        self.left = None
        self.right = None
        self.height = 0
        self.size = 1


# Helper function that returns True if two keys are equal
def compare_keys(key1, key2):
    if key1[0] == key2[0] and key1[1] == key2[1]:
        return True
    else:
        return False

# Helper method to return the node height
def _get_height(node):
    if node is None:
        return -1
    else:
        return node.height

# Helper method to return node size
def _get_size(node):
    if node is None:
        size = 0
        return size
    else:
        return node.size

# Helper method to calculate a node's balance
def balance(node):
    if node is None:
        return 0
    return _get_height(node.left) - _get_height(node.right)

# Helper method to update a node's height and size after its children have been modified
def _update_node(node):
    node.height = 1 + max(_get_height(node.left), _get_height(node.right))
    node.size = 1 + _get_size(node.left) + _get_size(node.right)

# Helper method for comparing two nodes to avoid repeating score and id logic
def comes_before(node, new_score, new_player_id):
    if (new_score > node.key[0]) or (new_score == node.key[0] and new_player_id < node.key[1]):
        return True
    else:
        return False

# Method for a right rotation on a node
def _rotate_right(node):
    left_child = node.left
    t2 = left_child.right

    left_child.right = node
    node.left = t2

    _update_node(node)
    _update_node(left_child)

    return left_child

# Method for left rotation on a node
def _rotate_left(node):

    right_child = node.right
    t2 = right_child.left

    right_child.left = node
    node.right = t2

    _update_node(node)
    _update_node(right_child)

    return right_child

def pre_order(node):
    if node:
        print(node.key[0], end=" ")
        pre_order(node.left)
        pre_order(node.right)

# Helper method for comparing two tuple keys directly
def _comes_before_key(key1, key2):
    return (key1[0] > key2[0]) or (key1[0] == key2[0] and key1[1] < key2[1])



# THIS IS WHERE THE AVL TREE CLASS BEGINS
class AVLTree:

    # Empty tree constructor
    def __init__(self):
        self.root = None


    # Inserts a player into the tree
    def insert(self, score, player_id):
        self.root = self._insert(self.root, score, player_id)


    # Helper for inserting player
    def _insert(self, node, score, player_id):
        # Base case
        if node is None:
            node = Node(score, player_id)
            return node

        # Recursion
        if comes_before(node, score, player_id):
            node.left = self._insert(node.left, score, player_id)
        else:
            node.right = self._insert(node.right, score, player_id)

        # Update the node's height and size
        _update_node(node)

        # Calculate the node's balance factor
        bf = balance(node)

        # RR case -> left rotate on the current node
        if bf < -1 and comes_before(node.right, score, player_id) == False:
            return _rotate_left(node)

        ## LL case -> right rotate on the current node
        if bf > 1 and comes_before(node.left, score, player_id):
            return _rotate_right(node)

        # RL Case -> right rotate on the right child, left rotate on the current node
        if bf < -1 and comes_before(node.right, score, player_id):
            node.right = _rotate_right(node.right)
            return _rotate_left(node)

        # LR case -> left rotate on left child, right rotate on the current node
        if bf > 1 and comes_before(node.left, score, player_id) == False:
            node.left = _rotate_left(node.left)
            return _rotate_right(node)

        return node


    # Removes a player from the tree using the node's key
    def delete(self,key):
        self.root = self._delete(self.root, key)


    # Delete helper to find the successor when a deleted node has two children
    def _get_min_node(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr


    # Delete helper method
    def _delete(self, node, key):
        # Base case
        if node is None:
            return None

        # Recursion
        if _comes_before_key(key, node.key):
            node.left = self._delete(node.left, key)
        elif _comes_before_key(node.key, key):
            node.right = self._delete(node.right, key)
        else:
            # Case 1 - Node is a leaf
            if node.left is None and node.right is None:
                return None

            # Case 2 - Node has one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3 - Node has two children
            else:
                # Find the successor with our helper class
                successor = self._get_min_node(node.right)
                # Copy the successor to the node
                node.key = successor.key
                # Delete the successor from its subtree
                node.right = self._delete(node.right, successor.key)

        # If the subtree became empty we can return the node now
        if node is None:
            return node

        # Update the node's height and size
        _update_node(node)

        # Calculate balance
        bf = balance(node)

        # Rebalance the different cases
        if bf > 1:
            if balance(node.left) >= 0:
                return _rotate_right(node)
            else:
                node.left = _rotate_left(node.left)
                return _rotate_right(node)

        if bf < -1:
            if balance(node.right) <= 0:
                return _rotate_left(node)
            else:
                node.right = _rotate_right(node.right)
                return _rotate_left(node)

        return node


    # Function for returning a node's rank
    def rank(self, key):
        return self._rank(self.root, key)


    # Helper for determining a node's rank
    def _rank(self, node, key):
        # Return none if the node is not found
        if node is None:
            return None

        # If the key is greater than the current node's key recurse left
        if _comes_before_key(key, node.key):
            return self._rank(node.left, key)

        # if the current node's key is greater than the key recurse right
        elif _comes_before_key(node.key, key):
            # Find the node's rank in the right subtree
            right_rank = self._rank(node.right, key)
            # Handle if the node does not exist in the right subtree
            if right_rank is None:
                return None
            # Add the size of the left tree to the node's rank in the right subtree
            return _get_size(node.left) + 1 + right_rank

        # The current node is the target node
        else:
            return _get_size(node.left) + 1


    # Method for returning the player with rank k
    def select(self, k):
        # Check for invalid rank arguments (k < 1 or k > the entire tree size
        if k <= 0 or k > _get_size(self.root):
            return None
        # Otherwise, call the _select helper
        return self._select(self.root, k)


    # Helper method for select
    def _select(self, node, k):
        if node is None:
            return None

        left_size = _get_size(node.left)

        if k == left_size + 1:
            return node
        elif k <= left_size:
            return self._select(node.left, k)
        else:
            return self._select(node.right, k - left_size - 1)

    # Method that searches a node by its key
    def search_by_key(self, key):
        return self._search_by_key(self.root, key)

    # Helper method for search by key
    def _search_by_key(self, node, key):

        # Return false if the searched key does not exist
        if node is None:
            return False

        # If the current node comes before the node we are searching for, recurse right
        if _comes_before_key(node.key, key):
            return self._search_by_key(node.right, key)
        # If the target key comes before the current node, recurse left
        elif _comes_before_key(key, node.key):
            return self._search_by_key(node.left, key)
        # The nodes are equal, return true
        else:
            return True


