import sys
from queue import PriorityQueue


def create_graph(filename):  # Parses through the input file and creates a dictionary
    graph = {}
    file = open(filename, 'r')
    num_lines = file.readlines()
    file.close()
    for line in num_lines[:-1]:
        data = line.split()
        if data == 'END OF INPUT':
            return graph
        else:
            if data[0] in graph:
                graph[data[0]][data[1]] = (data[2])
            else:
                graph[data[0]] = {data[1]: (data[2])}
            if data[1] in graph:
                graph[data[1]][data[0]] = (data[2])
            else:
                graph[data[1]] = {data[0]: (data[2])}
    return graph


def heuristic_input(filename):  # Parses through the heuristic file and creates a dictionary
    vals = {}
    file = open(filename, 'r')
    num_lines = file.readlines()
    file.close()
    for line in num_lines[:-1]:
        data = line.split()
        if data == 'END OF INPUT':
            return vals
        else:
            vals[data[0]] = data[1]
    return vals


def uninformed_search(node, graphnode, graph):  # Implements a graph based uniform cost search
    popped = 0
    generated = 0
    fringe = PriorityQueue()
    fringe.put((0, node))
    visited = {}
    visited[node] = ("", 0)
    parsed = []
    max_node = 0
    while not fringe.empty():
        if len(fringe.queue) > max_node:
            max_node = len(fringe.queue)
        _, node_count = fringe.get()
        popped += 1
        if node_count == graphnode:
            break
        if node_count in parsed:
            continue
        parsed.append(node_count)
        for i in graph[node_count]:
            generated += 1
            fringe.put((graph[node_count][i]+str(visited[node_count][1]), i))
            if i not in visited:
                visited[i] = (node_count, graph[node_count][i]+str(visited[node_count][1]))
    route = []
    distance = "infinity"
    if graphnode in visited:
        distance = 0.0
        node_count = graphnode
        while node_count != node:
            distance += float(graph[visited[node_count][0]][node_count])
            route.append(node_count)
            node_count = visited[node_count][0]
    return route, popped, generated, distance, len(parsed)


def informed_search(inode, inf_graph_node, graph, data):  # Implements A* search
    inf_generated = 0
    inf_popped = 0
    fringe = PriorityQueue()
    fringe.put((0, inode))
    inf_visited = {}
    inf_visited[inode] = ("", 0)
    inf_explored = []
    inf_node = 0
    while not fringe.empty():
        if len(fringe.queue) > inf_node:
            inf_node = len(fringe.queue)
        _, inf_count_node = fringe.get()
        inf_popped += 1
        if inf_count_node == inf_graph_node:
            break
        if inf_count_node in inf_explored:
            continue
        inf_explored.append(inf_count_node)
        for i in graph[inf_count_node]:
            inf_generated += 1
            if i not in inf_visited:
                inf_visited[i] = (inf_count_node, graph[inf_count_node][i] + str(inf_visited[inf_count_node][1]))
            fringe.put((graph[inf_count_node][i] + str(inf_visited[inf_count_node][1]) + data[i], i))
    route = []
    dist = "infinity"
    if inf_graph_node in inf_visited:
        dist = 0.0
        inf_count_node = inf_graph_node
        while inf_count_node != inode:
            dist += float(graph[inf_visited[inf_count_node][0]][inf_count_node])
            route.append(inf_count_node)
            inf_count_node = inf_visited[inf_count_node][0]
    return route, inf_popped, inf_generated, dist, inf_node


# Formatting output
if len(sys.argv) == 4:
    file_name = sys.argv[1]
    src = sys.argv[2]
    destination = sys.argv[3]
    graph = create_graph(file_name)
    route, popped, generated, distance, expanded = uninformed_search(src, destination, graph)
    print("Nodes Popped: {}".format(popped))
    print("Nodes Expanded: {}".format(expanded))
    print("Nodes Generated: {}".format(generated+1))
    if format(distance) == "infinity":
      print("Distance: {} ".format(distance))
    else:
      print("Distance: {} km".format(distance))
    print("Route:")
    node_count = src
    if len(route) == 0:
        print("None")
    else:
        for path in route[::-1]:
            print("{} to {}, {} km".format(node_count, path, float(graph[node_count][path])))
            node_count = path

elif len(sys.argv) == 5:
    file_name = sys.argv[1]
    src = sys.argv[2]
    destination = sys.argv[3]
    fname_h = sys.argv[4]
    graph = create_graph(file_name)
    val = heuristic_input(fname_h)
    route, popped, generated, distance, max_node = informed_search(src, destination, graph, val)
    print("Nodes Popped: {}".format(popped))
    print("Nodes Expanded: {}".format(len(route)))
    print("Nodes Generated: {}".format(generated+1))
    if format(distance) == "infinity":
      print("Distance: {} ".format(distance))
    else:
      print("Distance: {} km".format(distance))
    print("Route:")
    node_count = src
    if len(route) == 0:
        print("None")
    else:
        for path in route[::-1]:
            print("{} to {}, {} km".format(node_count, path, float(graph[node_count][path])))
            node_count = path
