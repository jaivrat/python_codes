
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data


def binary_search(node, data):
    if node is None:
        return None
    if node.data == data:
        return node
    elif data > node.data:
        return binary_search(node.right, data)
    else:
        return binary_search(node.left, data)


if __name__ == '__main__':
    n10 = Node(10)
    nm5 = Node(-5)
    nm10 = Node(-10)
    n5 = Node(5)
    n10 = Node(10)
    n25 = Node(25)
    n36 = Node(36)

    n10.left = nm5
    n10.right = n25
    nm5.left = nm10
    nm5.right = n5
    n25.right = n36
    
    node = binary_search(n10, 5)
    if node is not None:
        print("Found "+ str(node.data))
    else:
        print("Not Found 5")
    node = binary_search(n10, 100)
    if node is not None:
        print("Found "+ str(node.data))
    else:
        print("Not Found 100")
    
    print("exit")