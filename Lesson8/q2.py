import networkx as nx
from networkx import bipartite    
def replace_name(match, labels):
    sets = set()
    for i in match:
        sets.add((labels[i[0]], labels[i[1]]))
    return sets


def plotGraph(graph,ax,title):    
    pos=[(ii[1],ii[0]) for ii in graph.nodes()]
    pos_dict=dict(zip(graph.nodes(),pos))
    # labels = [labels[i] for i in pos]
    # pos = nx.spring_layout(graph)
    nx.draw(graph,pos=pos_dict,ax=ax,with_labels=True, font_size=8, node_size = 500)
    # nx.draw_networkx_labels(graph, pos, labels=labels)
    ax.set_title(title)
    return   

if __name__=='__main__':    
    #---------------Construct the graph---------------
    g=nx.Graph()
    labels={(1,0):'Allen', (1,1):'Bob', (1,2):'Chris', (1,3):'Doug', (1,4):'Eric', (1,5):'Fred', (1,6):'Gale', (1,7):'Head', (0,0):'1', (0,1):'2', (0,2):'3', (0,3):'4', (0,4): '5'}
    edges=[
        [(1,0), (0,0)],
        [(1,0), (0,1)],
        [(1,1), (0,0)],
        [(1,2), (0,0)],
        [(1,2), (0,1)],
        [(1,3), (0,2)],
        [(1,3), (0,3)],
        [(1,3), (0,4)],
        [(1,4), (0,1)],
        [(1,5), (0,0)],
        [(1,6), (0,2)],
        [(1,6), (0,3)],
        [(1,7), (0,1)],
        [(1,7), (0,2)]
        ]

    for ii in edges:
        g.add_node(ii[0],bipartite=0)
        g.add_node(ii[1],bipartite=1)

    g.add_edges_from(edges)

    #---------------Use maximal_matching---------------
    # match=nx.maximal_matching(g)   
    # # match = replace_name(match, labels) 
    # g_match=nx.Graph()
    # for ii in match:
    #     g_match.add_edge(ii[0],ii[1])

    #----------Use bipartite.maximum_matching----------
    match2=bipartite.maximum_matching(g)    
    # result = {labels[k]:labels[v] for k,v in match2.items()}
    # print(result)
    g_match2=nx.Graph()
    for kk,vv in match2.items():
        g_match2.add_edge(kk,vv)

    #-----------------------Plot-----------------------
    import matplotlib.pyplot as plt
    fig=plt.figure(figsize=(10,8))

    ax1=fig.add_subplot(1,2,1)
    plotGraph(g,ax1,'Graph')

    # ax2=fig.add_subplot(2,2,2)
    # plotGraph(g_match,ax2,'nx.maximal_matching()')

    ax3=fig.add_subplot(1,2,2)
    plotGraph(g_match2,ax3,'bipartite.maximum_matching()')

    plt.show()