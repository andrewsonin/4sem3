from adjacency_matrix import adjacency_matrix
from time_module import Profiler

using_list = open('output.txt', 'r', encoding='utf8').read().split()
using_list = [[using_list[i * 1000 + j] for j in range(1000)] for i in range(1000)]

with Profiler():
    for i in range(10):
        adjacency_matrix(1000, using_list)