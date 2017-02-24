def dfs(vertex, graph, used_vertexes=set()):
    used_vertexes.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used_vertexes:
            dfs(neighbour, graph, used_vertexes)


def read_graph_as_lists(vertex_quantity):
    graph, edge_quantity = [[] for i in range(vertex_quantity)], int(input())
    for edge in range(edge_quantity):
        link1, link2 = [int(x) for x in input().split()]
        graph[link2].append(link1), graph[link1].append(link2)
    return graph

n = int(input())
using_graph, using_set, number_of_connected_components = read_graph_as_lists(n), set(), 0
for using_vertex in range(n):
    if using_vertex not in using_set:
        dfs(using_vertex, using_graph, using_set)
        number_of_connected_components += 1
if number_of_connected_components > 1:
    print('NO')
else:
    print('YES')
