from database.DB_connect import DBConnect
from model.ordini import Ordine


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

        query = """select *
from orders o 
where o.store_id = %s"""
        cursor.execute(query, (id,))
        for row in cursor:
            result.append(Ordine(**row))
        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getEdges(id,giorni):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select distinct  o.order_id as o1, o2.order_id as o2, o.order_date as data1,o2.order_date as data2, oi.quantity + oi2.quantity as somma
from orders o , orders o2 ,order_items oi , order_items oi2 
where o2.order_id = oi2.order_id and 
o.order_id = oi.order_id
and o.store_id = o2.store_id and 
o2.store_id = %s 
and oi.item_id != oi2.item_id 
and o.order_id != o2.order_id 
and o.order_id < o2.order_id 
and datediff(o.order_date,o2.order_date) <= %s
and datediff(o2.order_date,o.order_date) <= %s
group by o.order_id, o2.order_id,o.order_date,o2.order_date"""
        cursor.execute(query, (id,giorni,giorni))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()

        return result