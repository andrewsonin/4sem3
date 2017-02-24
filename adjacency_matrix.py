def adjacency_matrix(N, using_list):
    for i in range(N):
        for j in range(N):
            if using_list[i][j] != '0':
                print(i, j, using_list[i][j])
