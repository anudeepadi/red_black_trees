# Implementation of red-black trees

class Node:
    def __init__(self, key, color, left, right):
        self.key = key
        self.color = color
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def insert_node(self, node, key):
        if node is None:
            return Node(key, 'red', None, None)

        if key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def is_red(self, node):
        if node is None:
            return False
        return node.color == 'red'

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'red'
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'red'
        return x

    def flip_colors(self, node):
        node.color = 'red'
        node.left.color = 'black'
        node.right.color = 'black'

    def print_tree(self):
        self.print_node(self.root)

    def print_node(self, node):
        if node is None:
            return

        self.print_node(node.left)
        print(node.key)
        self.print_node(node.right)

if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.print_tree()