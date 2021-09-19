class Node:
    def __init__(self, name):
        self.left = None
        self.right = None
        self.children = []
        self.name = name

    def add_child(self, node):
        self.children.append(node)
        return self
    
    def __repr__(self):
        s = str(self.name)
        s = s + "->("
        s = s + ",".join([str(child.name) for child in self.children])
        s = s + ")"
        return s



# helper just to set the problem
def connect(name1, name2, nodes):
    node1 = None
    for node in nodes:
        if node.name == name1:
            node1 = node
            break
    if node1 is None:
        raise Exception(f"Node {name1} not found")

    node2 = None
    for node in nodes:
        if node.name == name2:
            node2 = node
            break
    if node2 is None:
        raise Exception(f"Node {name1} not found")
    node1.add_child(node2)
    node2.add_child(node1)
    return 

# helper just to set the problem  
def find_vertex(name, nodes):
    node = None
    for node in nodes:
        if node.name == name:
            return node
    raise Exception(f"Node {name} not found")
    
# https://www.youtube.com/watch?v=pcKY4hjDrxk  
def helper_bfs(queue, visited_nodes_set,search_res):
        if (len(queue) == 0):
            return
        # take vertex from q and start exploring
        while len(queue) > 0:
            # explore
            node = queue.pop(0)
            children = node.children
            # explore (ie visit), and mark them in queue as well to explore further
            for child in children:
                if (not id(child) in visited_nodes_set):
                    search_res.append(child.name)
                    visited_nodes_set.add(id(child))
                    queue.insert(len(queue), child)
            for child in children:
                helper_bfs(queue, visited_nodes_set,search_res)

def BFS(nodes):
    # We can start BFS from any node
    start_from = find_vertex(1, nodes)
    visited_nodes_set=set()
    search_res = []
    queue = []
    # Init
    visited_nodes_set.add(id(start_from))
    search_res.append(start_from.name)
    queue.insert(len(queue),start_from)
    helper_bfs(queue, visited_nodes_set,search_res)
    return search_res


# -----------------------------------------------------------------------------------------
# DFS
# -----------------------------------------------------------------------------------------
def DFS(nodes):
    # We can start BFS from any node
    start_from = find_vertex(1, nodes)
    visited_nodes_set=set()
    search_res = []
    stack = []

    # Init
    stack.append(start_from)

    while len(stack) > 0:
        # explore: find first node
        peek_node = stack[len(stack)-1]
        stack.pop()
        if (not id(peek_node) in visited_nodes_set):
            visited_nodes_set.add(id(peek_node))
            search_res.append(peek_node.name)

        for child in peek_node.children:
            if (not id(child) in visited_nodes_set):
                stack.append(child)
    return  search_res

if __name__ == "__main__":

    # Set the graph problem
    nodes = []
    for i in range(1,10+1):
        nodes.append(Node(i))
    
    connect(3,10,nodes)
    connect(3,9,nodes)
    connect(3,4,nodes)
    connect(3,2,nodes)
    connect(1,4,nodes)
    connect(2,1,nodes)
    connect(2,8,nodes)
    connect(2,5,nodes)
    connect(2,7,nodes)
    connect(8,7,nodes)
    connect(7,5,nodes)
    connect(5,6,nodes)
    connect(5,8,nodes)

    bfs_result = BFS(nodes)
    print(bfs_result)
    # [1, 4, 2, 3, 5, 7, 8, 10, 9, 6]
    
    dfs_result = DFS(nodes)
    print(dfs_result)
    pass