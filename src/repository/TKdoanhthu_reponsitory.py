from util.excute import Excute


class TKdoanhthuRepository:

    def __init__(self):
        self.excute = Excute()

    def getInfo(self, start_timestamp, end_timestamp):
        query = f"select createAt, priceTicket,  priceWater, pricePopcorn from ticket where createAt between {start_timestamp} and {end_timestamp} order by createAt"
        return self.excute.getAll(query)
