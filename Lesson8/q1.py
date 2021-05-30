import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

oo = float('inf')
def getShortest(G):
    print("The shortest path with odd nodes:")
    print('k','h',nx.dijkstra_path_length(G, 'k','h'))
    print('k','i',nx.dijkstra_path_length(G, 'k','i'))
    print('k','m',nx.dijkstra_path_length(G, 'k','m'))
    print('k','c',nx.dijkstra_path_length(G, 'k','c'))
    print('k','d',nx.dijkstra_path_length(G, 'k','d'))
    print('h','i',nx.dijkstra_path_length(G, 'h','i'))
    print('h','m',nx.dijkstra_path_length(G, 'h','m'))
    print('h','c',nx.dijkstra_path_length(G, 'h','c'))
    print('h','d',nx.dijkstra_path_length(G, 'h','d'))
    print('i','m',nx.dijkstra_path_length(G, 'i','m'))
    print('i','c',nx.dijkstra_path_length(G, 'i','c'))
    print('i','d',nx.dijkstra_path_length(G, 'i','d'))
    print('m','c',nx.dijkstra_path_length(G, 'm','c'))
    print('m','d',nx.dijkstra_path_length(G, 'm','d'))
    print('c','d',nx.dijkstra_path_length(G, 'c','d'))
    
    return

if __name__ == '__main__':
    
    # 作图，无向图
    G = nx.Graph()
    G.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm'])

    G.add_weighted_edges_from([('a', 'd', 1),  ('a', 'e', 1), ('a', 'c', 3), ('a', 'b', 4), 
                            ('b', 'c', 5), ('b', 'd', 4), ('b', 'f', 3), ('c', 'g', 1), ('d', 'f', 2), ('e', 'f', 4), ('e', 'k', 6),('e', 'h', 3), ('f', 'l', 3), ('f', 'g', 3), ('f', 'i', 4), ('g', 'j', 4), ('g', 'm', 1), ('h', 'k', 3), ('h', 'l', 1), ('i', 'l', 1), ('i', 'j', 6), ('j', 'l', 4), ('j', 'm', 2), ('k', 'l', 3), ('l', 'm', 5), ('k', 'i', 3), ('d', 'h', 6), ('c', 'm', 2)])
    getShortest(G)
    pos = nx.spring_layout(G)
    # 是否是欧拉图
    print(nx.is_eulerian(G))
    # 获得欧拉路径
    euler = list(nx.eulerian_circuit(G, 'f'))
    # 记录
    path_length = 0
    cnt = 0
    for i in euler:
        cnt += 1
        path_length += G._adj[i[0]][i[1]]['weight']
    print("最短路径为:", euler)
    print("最短路径长度为:", path_length)
    print("共经过路径数目:",cnt)
    
    nx.draw(G, pos, with_labels=True)
    plt.show()