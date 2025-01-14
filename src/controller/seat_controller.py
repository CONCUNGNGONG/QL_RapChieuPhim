from service.seat_service import SeatService
from util.response import Res


class SeatController:
    def __init__(self):
        self.seatService = SeatService()

    def getAllChairSelected(self, idCalendar) -> Res:
        return self.seatService.getAllSeatOfCalendar(idCalendar)
