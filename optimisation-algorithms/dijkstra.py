inf = float("inf") # python actually has infinity

# adjacency matrix for a 10x10 graph
graph = [ # A, B, C, D, E, F, G, H, I, J
[0, inf, inf, 7, 13, inf, 5, inf, inf, 6], # A
[inf, 0, 10, inf, inf, inf, 1, inf, 18, 5], # B
[inf, 10, 0, inf, 6, inf, 4, 20, 1, 4], # C
[7, inf, inf, 0, inf, 7, 7, 17, 11, 2], # D
[13, inf, 6, inf, 0, 9, 12, 17, inf, 15], # E
[inf, inf, inf, 7, 9, 0, inf, inf, 11, inf], # F
[5, 1, 4, 7, 12, inf, 0, 16, 15, 10], # G
[inf, inf, 20, 17, 17, inf, 16, 0, inf, 14], # H
[inf, 18, 1, 11, inf, 11, 15, inf, 0, inf], # I
[6, 5, 4, 2, 15, inf, 10, 14, inf, 0]] # J

vertices = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def dijkstra(graph, vertices):
    processed_vertices = set()
    shortest_distances = [inf for i in range(len(vertices))]
    predecessors = [-1 for i in range(len(vertices))]
    shortest_distances[0] = 0
    predecessors[0] = 0

    #main loop
    for _ in range(len(vertices)):
        # add the shortest unexplored vertex to processed_vertices
        min_distance_vertex = -1
        min_val = inf
        for vertex in range(len(vertices)):
            if vertex not in processed_vertices and shortest_distances[vertex]<min_val:
                min_val = shortest_distances[vertex]
                min_distance_vertex = vertex
        if min_distance_vertex == -1:
            break # break once all reachable verticies explored
        processed_vertices.add(min_distance_vertex)

        # update the matrices with the new shortest path
        for vertex in vertices:
            if vertex not in processed_vertices:
                shortest_distances[vertex] = min(shortest_distances[vertex], shortest_distances[min_distance_vertex]+graph[min_distance_vertex][vertex])
                if shortest_distances[min_distance_vertex]+graph[min_distance_vertex][vertex] < shortest_distances[vertex]:
                    predecessors[vertex] = min_distance_vertex
        
    return shortest_distances

print(dijkstra(graph,vertices))