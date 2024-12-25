from model.ticket import Ticket
from service.order_service import OrderService
from util.response import Res


class OrderController:
    def __init__(self):
        self.orderService = OrderService()

    def orderTicket(self, ticket: Ticket, chairs: list, idStaff: str) -> Res:
        return self.orderService.order(ticket, chairs, idStaff)
