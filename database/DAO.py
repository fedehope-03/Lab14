from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllStore():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select s.store_id 
from stores s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["store_id"])
        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getNodes(id):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """"""
        cursor.execute(query)
        for row in cursor:
            result.append()
        cursor.close()
        conn.close()

        return result