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

def MST_weight(graph, mst):
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

def createGraphPlane(n):
	graph = {}
	for node in range(n):
		x_point = random.random()
		y_point = random.random()
		graph[node] = {}
		graph[node]['x_point'] = x_point
		graph[node]['y_point'] = y_point
	return graph

def createConPlane(graph):
	i = 0
	while(i < len(graph)):
		j = i + 1
		x_i = graph[i].pop('x_point')
		y_i = graph[i].pop('y_point')
		while j < len(graph):
			x_j = graph[j]['x_point']
			y_j = graph[j]['y_point']
			x_dis = abs(x_i - x_j)**2
			y_dis = abs(y_i - y_j)**2
			distance = (x_dis + y_dis)**(0.5)
			graph[i][j] = distance
			graph[j][i] = distance
			j += 1
		i += 1
	return graph



def avg_for_16(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(16)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(16)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_32(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(32)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(32)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_64(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(64)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(64)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_128(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(128)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(128)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_256(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(256)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(256)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_512(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(512)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(512)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_1024(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(1024)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(1024)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_2048(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(2048)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(2048)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_4096(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(4096)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(4096)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5

def avg_for_8192(is_Plane):
	#graphs for part 1
	if(is_Plane != True):
		total_mst_weights = 0
		graph = createGraph(8192)
		for x in range(5):
			new_graphs = createCon(graph)
			mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
			total_mst_weights += mst_weight
		return total_mst_weights/5

	#graphs for part 2
	total_mst_weights = 0
	for x in range(5):
		graph = createGraphPlane(8192)
		new_graphs = createConPlane(graph)
		mst_weight = MST_weight(new_graphs, prim(new_graphs, 0))
		total_mst_weights += mst_weight
	return total_mst_weights/5


def main():
	a = avg_for_16(False)
	b = avg_for_32(False)
	c = avg_for_64(False)
	d = avg_for_128(False)
	e = avg_for_256(False)
	f = avg_for_512(False)
	g = avg_for_1024(False)
	h = avg_for_2048(False)
	i = avg_for_4096(False)
	j = avg_for_8192(False)

	lst_of_rand_num_averages = [a,b,c,d,e,f,g,h,i,j]

	a = avg_for_16(True)
	b = avg_for_32(True)
	c = avg_for_64(True)
	d = avg_for_128(True)
	e = avg_for_256(True)
	f = avg_for_512(True)
	g = avg_for_1024(True)
	h = avg_for_2048(True)
	i = avg_for_4096(True)
	j = avg_for_8192(True)

	lst_of_plot_averages = [a,b,c,d,e,f,g,h,i,j]

	print('lst_of_rand_num_averages: ', lst_of_rand_num_averages)
	print('lst_of_plot_averages: ', lst_of_plot_averages)

main()