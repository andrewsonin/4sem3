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


def assert_even_of_vertexes(graph):
    for vertex in graph:
        if len(vertex) % 2 != 0:
            return False
    return True


def assert_connected_graph(graph, number_of_vertexes):
    stack_set, number_of_connected_components = set(), 0
    for vertex in range(number_of_vertexes):
        if vertex not in stack_set:
            dfs(vertex, graph, stack_set)
            number_of_connected_components += 1
            if number_of_connected_components > 1:
                return False
    return True


def euler(graph, number_of_vertexes):
    if not assert_even_of_vertexes(graph) or not assert_connected_graph(graph, number_of_vertexes):
        return 'NO'
    return 'YES'

n = int(input())
print(euler(read_graph_as_lists(n), n))
