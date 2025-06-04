import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self.nodes = []
        self._idMap = {}

    def getStores(self):
        return DAO.getAllStore()

    def buildGraph(self,store,giorni):
        self.nodes = DAO.getNodes(store)
        for n in self.nodes:
            self._idMap[n.order_id]=n
        self._graph.add_nodes_from(self.nodes)

        self.edges = DAO.getEdges(store,giorni)
        for e in self.edges:
            self._graph.add_edge(self._idMap[e["o2"]],self._idMap[e["o1"]],weight=e["somma"])

        print(self._graph.number_of_nodes(), self._graph.number_of_edges())
        # arco dal più recente al più vecchio