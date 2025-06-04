import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self.nodes = []

    def getStores(self):
        return DAO.getAllStore()

    def buildGraph(self,store,giorni):
        self.nodes = DAO.getNodes(store)
        self._graph.add_nodes_from(self.nodes)
        self.edges = DAO.getEdges(store,giorni)
        # arco dal più recente al più vecchio