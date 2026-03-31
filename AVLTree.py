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





