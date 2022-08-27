"""File which contains all of the required functions"""

import networkx as nx
from matplotlib import pyplot as plt


# defining function to add money owed as an attribute. Money owed is considiered -ve
# This operation is O(|E|), and |E| is upper bounded by |V|^2
def return_total_money_owed(graph):
    """
    Function that returns the total money owed by each user.
    Takes in a graph as the input and returns a graph.
    """

    # Programming defensively to protect against retard users :(
    assert isinstance(graph, nx.classes.digraph.DiGraph)

    attributes_dict = {node[0]: 0 for node in graph.nodes.data()}
    for edge in graph.edges.data():

        attributes_dict[edge[0]] -= edge[2]["weight"]
        attributes_dict[edge[1]] += edge[2]["weight"]

    nx.set_node_attributes(graph, attributes_dict, name="owed")
    return graph


def return_output_graph(graph):
    """
    Function that uses a greedy implementation of the algorithm and returns the graph.
    """
    graph = return_total_money_owed(graph)
    graph.remove_edges_from(list(graph.edges))

    # Using a greedy approach
    owes_list = []
    owed_list = []
    for node in graph.nodes.data():
        if node[1]["owed"] < 0:
            node[1]["color"] = "#FFFF00"
            owes_list.append(node)
        else:
            node[1]["color"] = "#00FFFF"
            owed_list.append(node)

    owes_list.sort(key=lambda node: node[1]["owed"])
    owed_list.sort(key=lambda node: node[1]["owed"], reverse=True)

    i = 0
    for node in owes_list:
        while abs(node[1]["owed"]) > owed_list[i][1]["owed"]:
            graph.add_edge(node[0], owed_list[i][0], weight=owed_list[i][1]["owed"])
            node[1]["owed"] += owed_list[i][1]["owed"]
            owed_list[i][1]["owed"] -= owed_list[i][1]["owed"]
            i += 1
        graph.add_edge(node[0], owed_list[i][0], weight=abs(node[1]["owed"]))
        owed_list[i][1]["owed"] += node[1]["owed"]
        node[1]["owed"] -= node[1]["owed"]

    return graph


def display_graph_and_output(graph):
    """
    Function that plots both the input graph and the output graph after the
    algorithm is implemented.
    """

    # Displaying input graph
    pos = nx.spring_layout(graph)
    plt.subplot(1, 2, 1)
    nx.draw(graph, pos, with_labels=True, arrows=True)
    print(graph.edges.data("weight"))

    # Displaying output graph
    output_graph = return_output_graph(graph)
    print(output_graph.edges.data("weight"))
    pos = nx.spring_layout(output_graph)
    plt.subplot(1, 2, 2)
    nx.draw(
        output_graph,
        pos,
        with_labels=True,
        arrows=True,
        node_color=[i[1] for i in graph.nodes.data("color")],
    )
    plt.show()
