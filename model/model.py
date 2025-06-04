from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getStores(self):
        return DAO.getAllStore()

    def buildGraph(self,store):
        DAO.getNodes(store)