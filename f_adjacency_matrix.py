def adjacency_matrix(N, using_list):
    for i in range(N):
        for j in range(N):
            if using_list[i][j] != '0':
                print(i, j, using_list[i][j])

N = int(input())
my_list = [input().split() for i in range(N)]
adjacency_matrix(N, my_list)
