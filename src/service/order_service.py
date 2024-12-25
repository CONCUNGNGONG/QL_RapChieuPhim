from model.ticket import Ticket
from repository.ticket_repository import TicketRepository
from repository.seat_repository import SeatRepository
from util.genarate import gen_time
from util.response import Res


class OrderService:
    def __init__(self):
        self.ticketRepository = TicketRepository()
        self.seatRepository = SeatRepository()

    def order(self, ticket: Ticket, chairs: list, idStaff: str) -> Res:
        if ticket is None:
            return Res(False, "Không có thông tin")

        if ticket.authen != "OK":
            return Res(False, "Lỗi xác thực")

        if str(idStaff).strip() == "":
            return Res(False, "Nhân viên không tồn tại")
        ticket.setCreateAt(gen_time.getNowTimestamp())
        insertTicket = self.ticketRepository.orderTicket(ticket, idStaff)
        if insertTicket == None or insertTicket == 0:
            return Res(False, "Lỗi đặt vé")

        dataSeat = [(ticket.id, ticket.calendar, c) for c in chairs]
        insertSeat = self.seatRepository.orderSeat(dataSeat)
        if insertSeat == None or insertSeat == 0:
            return Res(False, "Lỗi đặt ghế")

        return Res(True)
