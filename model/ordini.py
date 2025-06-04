from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ordine:
    order_date:datetime
    order_id:int
    order_status:int
    customer_id:int
    required_date:datetime
    orders:int
    shipped_date:datetime
    store_id:int
    staff_id:int

    def __hash__(self):
        return hash(self.order_id)

    def __eq__(self,other):
        return self.order_id == other.order_id