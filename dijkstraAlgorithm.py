INF = int(1e9) #Set 1 billion as a value that means infinity

#Receive input of number of nodes and number of edges
n,m = map(int, input("Number of nodes, and edges").split())
# Receive the starting node number
start = int(input("Please enter the starting node number"))
# Create a list containing information about the nodes connected to each node.
graph = [[] for i in range(n+1)]
#Create a list to check if you have visited
visited = [False] * (n+1)
#Initialize all shortest distance tables to infinite
distance = [INF] * (n+1)

#Enter all trunk informationEnter all trunk information
for _ in range(m):
    a,b,c = map(int, input("The cost of going from node a to node b is c.The cost of going from node a to node b is c.").split())
    graph[a].append((b,c))
    graph[b].append((a,c))

#Among unvisited nodes, returns the number of the node with the shortest distance.
def get_smallest_node():
    min_value = INF
    index = 0 # Node with shortest distance (index)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # Initialize the starting node
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # Repeat for all n - 1 nodes excluding the starting node
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        #Check other nodes connected to the current node
        for j in graph[now]:
            cost = distance[now] + j[1]
            #When the distance to travel from the current node to another node is shorter
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# Perform Dijkstra's algorithm
dijkstra(start)

#Prints the shortest distance to all nodes
for i in range(1, n+1):
    #If unreachable, output infinite (INF)
    if distance[i] == INF:
        print("INFINITY")
    #Print distance if reachable
    else:
        print("The shortest distance from",start,"to",i,"is",distance[i])
