import networkx as nx
from networkx import Graph
import matplotlib as plt


class Roadmap(Graph):

    def __init__(self):
        roadmap = nx.complete_graph(10)

    def show_map(self):
        nx.draw(self.map)
        plt.show()


