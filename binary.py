class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Let's figure out how to print the tree


# Use the insert method to add nodes
root = Node(25)
root.insert(15)
root.insert(40)
root.insert(30)
root.insert(10)
root.insert(20)

# Make sure that it prints out in the correct order which should be 10, 15, 20, 25, 30, 40
root.PrintTree()