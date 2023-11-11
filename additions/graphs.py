from math import inf

graph = ((0, 3, 1, 3, 0, 0),
        (3, 0, 4, 0, 0, 0),
        (3, 0, 0, 0, 0, 2),
        (0, 0, 7, 0, 0, 4),
        (0, 0, 5, 2, 4, 0))

nodes_len = len(graph) #число вершин графа
result_row = [inf]*nodes_len #определяют последнюю строку таблицы, заполняя бесконечностями

start_node = 0 #стартовая вершина
processed = {start_node} #просмотренные вершины
result_row[start_node] = 0 #нулевой вес для стартовой вершины

def get_neighbours(node, graph):
    for i, weight in enumerate(graph[node]):
        if weight > 0:
            yield i

def min_node(result_row, processed):
    min_arg = -1
    max_value = max(result_row)
    for i, t in enumerate(result_row):
        if t < max_value and i not in processed:
            max_value = t
            min_arg = i
    return min_arg

while start_node != -1:
    for j in get_neighbours(start_node, graph): # перебор всех соседей вершины start_node
        if j not in processed:
            weight = result_row[start_node] + graph[start_node][j]
            if weight < result_row[j]:
                result_row[j] = weight

    next_node = min_node(result_row, processed) #выбираем след. вершину с минимальным весов
    if next_node > 0:
        processed.add(next_node)

print(result_row)