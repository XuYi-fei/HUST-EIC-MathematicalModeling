import networkx as nx
import matplotlib.pyplot as plt
from networkx import bipartite    
# , 'Bob', 'Chris', 'Doug', 'Eric', 'Fred', 'Gale', 'Head'
def plotGraph(graph,ax,title):    
    # import pdb; pdb.set_trace()
    pos=[(ii[1],ii[0]) for ii in graph.nodes()]
    labels={(1,0):'Allen', (1,1):'Bob', (1,2):'Chris', (1,3):'Doug', (1,4):'Eric', (1,5):'Fred', (1,6):'Gale', (1,7):'Head', (0,0):'1', (0,1):'2', (0,2):'3', (0,3):'4', (0,4): '5'}
    # pos = [labels[i] for i in pos]
    pos_dict=dict(zip(graph.nodes(),pos))
    # labels = [labels[i] for i in pos]
    # pos = nx.spring_layout(graph)
    nx.draw(graph,pos=pos_dict,ax=ax,with_labels=True, font_size=8, node_size = 500)
    # nx.draw_networkx_labels(graph, pos, labels=labels)
    ax.set_title(title)
    return   

if __name__=='__main__':    
    # G = nx.Graph({0: [1,2], 1: [0,2], 2: [0,1,3,4], 3: [2,4], 4:[2,3]})    
    # G = nx.Graph()
    # G.add_weighted_edges_from([('Allen', 'a', 1), ('A', 'c', 4), ('B', 'a', 2), ('B', 'b', 1), ('B', 'c', 3), ('C', 'c', 5)])
    # pos = nx.spring_layout(G)
    # print(nx.max_weight_matching(G))
    G = nx.DiGraph()
    G.add_nodes_from([0, 1, 2, 3, 'ax'])
    G.add_weighted_edges_from([(0, 3, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1), (3, 1, 1), (3, 'ax', 1)])
    print(nx.is_eulerian(G))
    nx.draw(G, with_labels=True)
    plt.show()


