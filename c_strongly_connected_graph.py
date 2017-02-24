def read_graph_as_lists(vertex_quantity):
    graph, reversed_graph, edge_quantity = [[] for i in range(vertex_quantity)], [[] for i in range(
        vertex_quantity)], int(input())
    for edge in range(edge_quantity):
        link1, link2 = [int(x) for x in input().split()]
        graph[link1].append(link2), reversed_graph[link2].append(link1)
    return graph, reversed_graph


def dfs(vertex, graph, used_vertexes=set(), stack=list(), stacking=True):
    used_vertexes.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used_vertexes:
            dfs(neighbour, graph, used_vertexes, stack, stacking)
    if stacking:
        stack.append(vertex)


def kosaraju(using_graphs, number_of_vertexes):
    stack, used_vertexes = [], set()
    for i in range(number_of_vertexes):
        if i not in used_vertexes:
            dfs(i, using_graphs[0], used_vertexes, stack)
    used_vertexes = set()
    dfs(stack[-1], using_graphs[1], used_vertexes, stacking=False)
    if len(used_vertexes) < number_of_vertexes:
        return 'NO'
    return 'YES'

n = int(input())
print(kosaraju(read_graph_as_lists(n), n))
