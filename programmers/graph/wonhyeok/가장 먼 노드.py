def solution(n, edge):
    #�ʺ� �켱 Ž��
    graph = {k:[] for k in range(1,n+1)}
    
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    queue = [(0, graph.pop(1))]
    max_range = 0
    answer_count = 0
    
    while len(queue) > 0:
        node_range, connect_list = queue.pop(0) #��ť�� �ٲٱ�
        
        is_node_end = True
        for connect_node_num in connect_list:
            if connect_node_num in graph:
                is_node_end = False
                queue.append((node_range+1, graph.pop(connect_node_num)))
        
        if is_node_end:
            if max_range < node_range:
                max_range = node_range
                answer_count = 1
            elif max_range == node_range:
                answer_count += 1
    
    return answer_count