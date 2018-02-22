import random

def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def prim(graph, root):
    pred = {} # pair {vertex: predecesor in MST}
    key = {}  # keep track of minimum weight for each vertex
    pqueue = {} # priority queue implemented as dictionary
    #print("graph when calling prim's: ", graph)
    for v in graph:
        pred[v] = -1
        key[v] = 1000
    key[root] = 0
    for v in graph:
        pqueue[v] = key[v]
     
    while pqueue:
        u = popmin(pqueue)
        for v in graph[u]: # all neighbors of v
            if v in pqueue and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return pred

def MST_weight(mst):
	weight = 0
	for n in mst:
		if mst[n] != -1:
			weight += graph[n][mst[n]]
	return weight

def createGraph(n):
	#random generated edge eights
	graph = {}
	for node in range(n):
		graph[node] = {}
	return graph

def createCon(graph):
	#creating the connections for random weight graph
	i = 0
	while(i < len(graph)):
		j = i + 1
		while j < len(graph):
			weight = random.random()
			graph[i][j] = weight
			graph[j][i] = weight
			j += 1
		i += 1
	return graph

graph = createCon(createGraph(8192))
#print(graph)
x = prim(graph, 0)
#print(graph)
print(MST_weight(x))