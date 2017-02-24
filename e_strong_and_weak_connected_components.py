def read_graph_as_lists(vertex_quantity):
    graphs, edge_quantity = [[[] for i in range(vertex_quantity)] for j in range(3)], int(input())
    for edge in range(edge_quantity):
        a, b = [int(x) for x in input().split()]
        graphs[0][a].append(b), graphs[1][b].append(a), graphs[2][a].append(b), graphs[2][b].append(a)
    return graphs


def dfs(vertex, graph, used_vertexes=set(), stack=list(), stacking=True):
    used_vertexes.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used_vertexes:
            dfs(neighbour, graph, used_vertexes, stack, stacking)
    if stacking:
        stack.append(vertex)


def kosaraju(graph, reversed_graph, number_of_vertexes):
    stack, used_vertexes = [], set()
    for i in range(number_of_vertexes):
        if i not in used_vertexes:
            dfs(i, graph, used_vertexes, stack)
    used_vertexes, number_of_connected_components = set(), 0
    for i in range(-1, -number_of_vertexes - 1, -1):
        if stack[i] not in used_vertexes:
            dfs(stack[i], reversed_graph, used_vertexes, stacking=False)
            number_of_connected_components += 1
    return number_of_connected_components


def weak_components(graph, number_of_vertexes):
    using_set, number_of_connected_components = set(), 0
    for using_vertex in range(number_of_vertexes):
        if using_vertex not in using_set:
            dfs(using_vertex, graph, using_set, stacking=False)
            number_of_connected_components += 1
    return number_of_connected_components

n = int(input())
my_graph = read_graph_as_lists(n)
print(weak_components(my_graph[2], n), kosaraju(my_graph[0], my_graph[1], n))
