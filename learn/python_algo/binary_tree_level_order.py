class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data

class Queue:
    def __init__(self):
        self.elements = []
    
    def enqueue(self, data):
        self.elements.append(data)
        return data

    def dequeue(self):
        return self.elements.pop(0)

    # Look at last element
    def rear(self):
        return self.elements[-1]
    
    # Look at front element
    def front(self):
        return self.elements[0]

    def is_empty(self):
        return len(self.elements) == 0


def level_first_traverse(node):
    q = Queue()
    q.enqueue(node)
    while (not q.is_empty()):
        node_loc = q.dequeue()
        if node_loc.left is not None:
            q.enqueue(node_loc.left)
        if node_loc.right is not None:
            q.enqueue(node_loc.right)
        print(node_loc.data)


if __name__ == '__main__':
    n10 = Node(10)
    n9 = Node(9)
    nm10 = Node(-10)
    n11 = Node(11)
    n15 = Node(15)
    n16  = Node(16)
    n21 = Node(21)
    n18 = Node(18)
    n19 = Node(19)

    n10.left = n9
    n10.right = nm10
    n9.left = n11
    n11.right = n15
    nm10.left = n16
    nm10.right = n21
    n21.right = n19
    n16.right = n18

    level_first_traverse(n10)
