def Dijkstra(distance_matrix, start):                            #输入为距离矩阵与初始点
    Inf = 9e+100
    node = [start]                                               # 目前最近节点的点
    distance = [Inf for i in range(len(distance_matrix))]        # 目前最短距离
    distance[start] = 0
    way = [[] for i in range(len(distance_matrix))]              # 初始点到其他节点的最短距离
    way[start] = [start]
    while len(node) < len(distance_matrix):     
        min_distance = Inf
        col = 999                                   # 表示无联通路径
        row = 999                                   # 表示无联通路径
        for n in node:                              # 以当前最短路径节点出发
            for i in [x for x in range(len(distance_matrix)) if x not in node]:   
                if distance_matrix[n][i] + distance[n] < min_distance:     # 小于路径最小值时进入循环
                    min_distance = distance_matrix[n][i] + distance[n]     # 合并路径距离
                    row = n         
                    col = i
        if col == 999 or row == 999:                   # 无联通路径
            break
        node.append(col)                             # 添加节点
        distance[col] = min_distance                 # 最短距离
        way[col] = way[row][:]         
        way[col].append(col)                
    return node, distance, way

