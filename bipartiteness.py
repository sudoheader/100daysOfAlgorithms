import networkx as nx
import matplotlib.pyplot as plt

%matplotlib inline
# algorithm
def test_bipartiteness(graph):
    partition = {}
    nodes = [(i, None) for i in graph]

    while nodes:
        node, color = nodes.pop()

        # assign default color
        if color is None:
            color = partition.get(node, 0)

        # test bipartiteness
        if node in partition:
            if partition[node] != color:
                raise ValueError('graph is not bipartite')
            continue

        # assign partition, DFS
        partition[node] = color
        nodes.extend((i, 1 - color) for i in graph[node])

    return partition

# graph #1
graph = nx.complete_multipartite_graph(5, 5)
partition = test_bipartiteness(graph)
partition

plt.figure(figsize=(10, 8))
plt.axis('off')

colors = ['steelblue', 'red']
node_color = [colors[partition[i]] for i in graph]
pos = nx.circular_layout(graph)

nx.draw_networkx(graph, pos=pos, node_color=node_color)

# graph #2
graph = nx.circulant_graph(10, [1])
partition = test_bipartiteness(graph)
partition

plt.figure(figsize=(10, 8))
plt.axis('off')

colors = ['steelblue', 'red']
node_color = [colors[partition[i]] for i in graph]
pos = nx.circular_layout(graph)

nx.draw_networkx(graph, pos=pos, node_color=node_color)

# graph #3
try:
    graph = nx.complete_multipartite_graph(2, 2, 2)
    test_bipartiteness(graph)
except ValueError as e:
    print(e)

plt.figure(figsize=(10, 8))
plt.axis('off')

nx.draw_networkx(graph, pos=nx.circular_layout(graph))
