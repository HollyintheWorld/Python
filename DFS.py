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
} # defining a graph to use

def DFS(graph, start_node):
    visit = list() #Defining a list to store the visited node list
    stack = list() #Defining  a list to store the list of nodes to visit next
    
    stack.append(start_node) #Saving the starting node to the list
    
    while stack: #Loop until there are no nodes to visit
        node = stack.pop() #Retrieves the last node from the list
        if node not in visit: #If the node is not yet on the visit list
            visit.append(node) #Add to visit list
            stack.extend(graph[node]) #Add child nodes of the node to the list
    
    return visit #Return visit list value
