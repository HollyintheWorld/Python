graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
} # Defining the graph to use

def BFS(graph, start_node):
    visit = list() #Defining a list to store the list of visited nodes
    queue = list() #Defining a queue to store the list of nodes to visit next
    
    queue.append(start_node) #Save the starting node to the list
    
    while queue: #Loop until there are no nodes to visit
        node = queue.pop(0) #Retrieves the first node from the list
        if node not in visit: 
            visit.append(node) #Add to visit list
            queue.extend(graph[node]) #Add child nodes of the node to the list
            
    return visit #Return visit list value

print(BFS(graph,'A'))
# Visit sequentially starting from the node added to the queue first and print
