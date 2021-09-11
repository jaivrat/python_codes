

class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

# V-L-R
def pre_order(node):
    if node is not None:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)

# L-V-R
def in_order(node):
    if node is not None:
        pre_order(node.left)
        print(node.data)
        pre_order(node.right)  

if __name__ == '__main__':
    n10 = Node(10)
    n2 = Node(2)
    n6 = Node(6)
    n5 = Node(5)
    n8 = Node(8)
    n3 = Node(3)
    n10.left = n2
    n2.left = n6
    n10.right =n5
    n5.left = n8
    n5.right = n3
    print("Pre Order:")
    pre_order(n10)
    print("In Order:")
    in_order(n10)
    print("exit")