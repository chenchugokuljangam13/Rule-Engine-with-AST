class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child node
        self.right = right  # Right child node (for operators)
        self.value = value  # Value for operand nodes
