class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    # create a new tree with a root node
    def __init__(self, _root: Node):
        self.root = _root

    # add a new node to a specific node
    # can be called recursively
    def add(self, node: Node, new_node: Node):
               
        # going left
        if new_node.data <= node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.add(node.left, new_node)

        # going right
        else:
            if node.right is None:
                node.right = new_node
            else:
                self.add(node.right, new_node)

    def print_tree(self, node:Node):
        # print main node
        print(node.data)

        # print its children
        if node.left is not None:
            self.print_tree(node.left)
        
        if node.right is not None:
            self.print_tree(node.right)


t = Tree(Node(2))
t.add(t.root, Node(1))
t.add(t.root, Node(2))
t.add(t.root, Node(3))
t.add(t.root, Node(4))
t.print_tree(t.root)
