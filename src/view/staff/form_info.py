# Form implementation generated from reading ui file 'form_info.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt6 import QtCore, QtGui, QtWidgets

from model.staff_current import StaffCurrent
from controller.calendar_controller import CalendarController
from controller.movie_controller import MovieController
from controller.seat_controller import SeatController
from controller.total_controller import TotalController
from controller.ticket_controller import TicketController
from controller.order_controller import OrderController
from util import toast, time
from util.genarate import gen_time
from model.ticket import Ticket
from view.staff.frame_calendar import Ui_SelectCalendar
from view.staff.frame_payment import Ui_Payment


class Ui_FormInfo(object):
    def __init__(self, frameWorking, staffCurrent: StaffCurrent):
        self.frameWorking = frameWorking
        self.calendarController = CalendarController()
        self.movieController = MovieController()
        self.seatController = SeatController()
        self.totalController = TotalController()
        self.ticketController = TicketController()
        self.orderController = OrderController()
        self.staffCurrent = staffCurrent
        self.listIdMovie = []
        self.listMovie = []
        self.listIdCalendar = []
        self.listCalendar = []
        self.selecting = []
        self.priceMovie = None
        self.totalTicket = 0
        self.totalWater = 0
        self.totalPopcorn = 0
        self.ticketAuthened: Ticket = None

    def setupUi(self, FormInfo):
        FormInfo.setObjectName("FormInfo")
        FormInfo.resize(381, 701)
        FormInfo.setStyleSheet(
            "QSpinBox,QComboBox,QLineEdit,QPushButton,QLabel{font-size: 15px} QSpinBox,QComboBox,QLineEdit, QPushButton{border-radius: 10px; padding: 5px 8px}"
        )

        self.box = QtWidgets.QGroupBox(parent=FormInfo)
        self.box.setGeometry(QtCore.QRect(0, 0, 381, 701))
        self.box.setStyleSheet("background: rgba(235, 235, 235, 0.8); border: none")
        self.box.setTitle("")
        self.box.setObjectName("box")
        self.label_9 = QtWidgets.QLabel(parent=self.box)
        self.label_9.setGeometry(QtCore.QRect(30, 510, 71, 21))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(parent=self.box)
        self.label_6.setGeometry(QtCore.QRect(130, 390, 91, 31))
        self.label_6.setStyleSheet("font-size: 22px")
        self.label_6.setObjectName("label_6")
        self.email = QtWidgets.QLineEdit(parent=self.box)
        self.email.setGeometry(QtCore.QRect(80, 340, 211, 31))
        self.email.setStyleSheet("background: white")
        self.email.setObjectName("email")
        self.total_popcorn = QtWidgets.QLabel(parent=self.box)
        self.total_popcorn.setGeometry(QtCore.QRect(230, 500, 101, 31))
        self.total_popcorn.setObjectName("total_popcorn")
        self.clean = QtWidgets.QPushButton(parent=self.box)
        self.clean.setGeometry(QtCore.QRect(240, 630, 111, 41))
        self.clean.setStyleSheet("background-color: yellow; font-size: 16px")
        self.clean.setObjectName("clean")
        self.total_ticket = QtWidgets.QLabel(parent=self.box)
        self.total_ticket.setGeometry(QtCore.QRect(260, 430, 101, 31))
        self.total_ticket.setObjectName("total_ticket")
        self.total_water = QtWidgets.QLabel(parent=self.box)
        self.total_water.setGeometry(QtCore.QRect(230, 550, 101, 31))
        self.total_water.setObjectName("total_water")
        self.payment = QtWidgets.QPushButton(parent=self.box)
        self.payment.setGeometry(QtCore.QRect(30, 630, 201, 41))
        self.payment.setStyleSheet("background-color: #3dd5f3; font-size: 16px")
        self.payment.setObjectName("payment")
        self.groupBox = QtWidgets.QGroupBox(parent=self.box)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 341, 231))
        self.groupBox.setStyleSheet("QGroupBox{border: 1px solid #adb5bd}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 10, 131, 31))
        self.label.setStyleSheet("font-size: 22px")
        self.label.setObjectName("label")
        self.image = QtWidgets.QLabel(parent=self.groupBox)
        self.image.setGeometry(QtCore.QRect(230, 50, 101, 141))
        self.image.setStyleSheet("border: 1px solid #adb5bd; padding: 1px")
        self.image.setText("")
        self.image.setObjectName("image")
        self.nameMovie = QtWidgets.QComboBox(parent=self.groupBox)
        self.nameMovie.setGeometry(QtCore.QRect(10, 100, 211, 31))
        self.nameMovie.setStyleSheet("font-size: 15px; background: #ffffff")
        self.nameMovie.setObjectName("nameMovie")
        self.nameMovie.addItem("")
        self.selectDay = QtWidgets.QLineEdit(parent=self.groupBox)
        self.selectDay.setGeometry(QtCore.QRect(10, 50, 211, 31))
        self.selectDay.setStyleSheet("background: white")
        self.selectDay.setReadOnly(True)
        self.selectDay.setObjectName("selectDay")
        self.calender = QtWidgets.QComboBox(parent=self.groupBox)
        self.calender.setGeometry(QtCore.QRect(10, 150, 211, 31))
        self.calender.setStyleSheet("font-size: 15px; background: #ffffff")
        self.calender.setObjectName("calender")
        self.calender.addItem("")
        self.btnSelectChair = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnSelectChair.setGeometry(QtCore.QRect(10, 190, 101, 31))
        self.btnSelectChair.setStyleSheet("font-size: 15px; background: #fd9843")
        self.btnSelectChair.setObjectName("btnSelectChair")
        self.timeRemaing = QtWidgets.QLabel(parent=self.groupBox)
        self.timeRemaing.setGeometry(QtCore.QRect(130, 200, 191, 20))
        self.timeRemaing.setStyleSheet("color: rgb(255, 75, 84)")
        self.timeRemaing.setText("")
        self.timeRemaing.setObjectName("timeRemaing")
        self.num_popcorn = QtWidgets.QSpinBox(parent=self.box)
        self.num_popcorn.setGeometry(QtCore.QRect(110, 500, 91, 31))
        self.num_popcorn.setStyleSheet("background: white")
        self.num_popcorn.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(parent=self.box)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 111, 31))
        self.label_3.setObjectName("label_3")
        self.listChair = QtWidgets.QTextEdit(parent=self.box)
        self.listChair.setGeometry(QtCore.QRect(30, 430, 211, 31))
        self.listChair.setStyleSheet(
            "font-size: 15px;     background: transparent; border: none"
        )
        self.listChair.setReadOnly(True)
        self.listChair.setObjectName("listChair")
        self.nameCustomer = QtWidgets.QLineEdit(parent=self.box)
        self.nameCustomer.setGeometry(QtCore.QRect(150, 290, 191, 31))
        self.nameCustomer.setStyleSheet("background: white")
        self.nameCustomer.setObjectName("nameCustomer")
        self.label_8 = QtWidgets.QLabel(parent=self.box)
        self.label_8.setGeometry(QtCore.QRect(120, 460, 131, 31))
        self.label_8.setStyleSheet("font-size: 22px")
        self.label_8.setObjectName("label_8")
        self.num_water = QtWidgets.QSpinBox(parent=self.box)
        self.num_water.setGeometry(QtCore.QRect(110, 550, 91, 31))
        self.num_water.setStyleSheet("background: white")
        self.num_water.setObjectName("spinBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.box)
        self.label_4.setGeometry(QtCore.QRect(20, 340, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.box)
        self.label_5.setGeometry(QtCore.QRect(120, 250, 131, 31))
        self.label_5.setStyleSheet("font-size: 22px")
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(parent=self.box)
        self.label_10.setGeometry(QtCore.QRect(20, 560, 71, 21))
        self.label_10.setObjectName("label_10")
        self.retranslateUi(FormInfo)
        QtCore.QMetaObject.connectSlotsByName(FormInfo)

    def retranslateUi(self, FormInfo):
        _translate = QtCore.QCoreApplication.translate
        FormInfo.setWindowTitle(_translate("FormInfo", "Form Info"))
        self.label_3.setText(_translate("FormInfo", "Tên khách hàng"))
        self.label_4.setText(_translate("FormInfo", "Email"))
        self.label_5.setText(_translate("FormInfo", "Khách hàng"))
        self.label_6.setText(_translate("FormInfo", "Chỗ ngồi"))
        self.label.setText(_translate("FormInfo", "Tra cứu phim"))
        self.nameMovie.setItemText(0, _translate("FormInfo", "Chọn bộ phim"))
        self.calender.setItemText(0, _translate("FormInfo", "Chọn lịch chiếu"))
        self.btnSelectChair.setText(_translate("FormInfo", "Chọn ghế"))
        self.label_8.setText(_translate("FormInfo", "Dịch vụ khác"))
        self.label_9.setText(_translate("FormInfo", "Bỏng ngô"))
        self.label_10.setText(_translate("FormInfo", "Nước ngọt"))
        self.total_popcorn.setText(_translate("FormInfo", "0 đ"))
        self.total_water.setText(_translate("FormInfo", "0 đ"))
        self.total_ticket.setText(_translate("FormInfo", "0 đ"))
        self.payment.setText(_translate("FormInfo", "Thanh toán"))
        self.clean.setText(_translate("FormInfo", "Làm mới"))
        self.listChair.setHtml(
            _translate(
                "FormInfo",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:15px; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.setMovieToday()
        self.setEvents()

    def setEvents(self):
        self.selectDay.textChanged.connect(self.changeDay)
        self.selectDay.mousePressEvent = self.showFrameSelectCalendar
        self.nameMovie.currentIndexChanged.connect(self.changeMovie)
        self.calender.currentIndexChanged.connect(self.changeCalendar)
        self.btnSelectChair.clicked.connect(self.clickBtnChooseChair)
        self.clean.clicked.connect(self.clickClean)
        self.listChair.textChanged.connect(self.listChairChanged)
        self.num_popcorn.editingFinished.connect(self.numPopcornChanged)
        self.num_water.editingFinished.connect(self.numWaterChanged)
        self.payment.clicked.connect(self.payClick)

    def setMovieToday(self):
        nowtms = gen_time.getNowTimestamp()
        date = time.convertTimeStampToString(nowtms, "%d-%m-%Y")
        self.selectDay.setText(date)
        self.changeDay()

    def clickClean(self):
        self.cleanData()

    def cleanData(self):
        self.nameCustomer.setText("")
        self.email.setText("")
        self.listChair.setPlainText("")
        self.total_ticket.setText("0 đ")
        self.num_popcorn.setValue(0)
        self.total_popcorn.setText("0 đ")
        self.num_water.setValue(0)
        self.total_water.setText("0 đ")
        self.calender.setCurrentIndex(0)
        self.totalWater = 0
        self.totalPopcorn = 0
        self.totalTicket = 0
        self.ticketAuthened = None

    def payClick(self):
        if self.authenTicket() is False:
            return
        self.payment_window = QtWidgets.QMainWindow()
        self.payment_ui = Ui_Payment(self)
        self.payment_ui.setupUi(self.payment_window)
        self.payment_window.show()

    def listChairChanged(self):
        if self.frameWorking.frameWorkingShowed is False:
            return
        if self.priceMovie is None:
            price = self.getPriceMovie()
            if price is None:
                return
            self.priceMovie = price
        if len(self.selecting) == 0:
            self.total_ticket.setText("0 đ")
            return
        totalTicket = self.getTotalTicket()
        self.totalTicket = totalTicket["total_number"]
        self.total_ticket.setText(f"{totalTicket['total_money']} đ")

    def getPriceMovie(self):
        resultGetPriceMovie = self.movieController.getPriceMovie(
            self.listIdMovie[self.nameMovie.currentIndex()]
        )

        if resultGetPriceMovie.success is False:
            toast.toastWarning(resultGetPriceMovie.message)
            return None

        return resultGetPriceMovie.data

    def getTotalTicket(self):
        resultTotalTicket = self.totalController.cal_totalTicket(
            self.selecting, self.priceMovie
        )
        if resultTotalTicket.success is False:
            toast.toastWarning(resultTotalTicket.message)
            return
        return resultTotalTicket.data

    def numPopcornChanged(self):
        quantity = self.num_popcorn.value()
        if quantity == 0:
            self.total_popcorn.setText("0 đ")
            self.totalPopcorn = 0
            return
        resultGetPricePopcorn = self.totalController.cal_totalPopcorn(
            self.num_popcorn.value()
        )
        if resultGetPricePopcorn.success is False:
            return toast.toastWarning(resultGetPricePopcorn.message)

        dataRes = resultGetPricePopcorn.data
        self.totalPopcorn = dataRes["total_number"]
        self.total_popcorn.setText(f"{dataRes['total_money']} đ")

    def numWaterChanged(self):
        quantity = self.num_water.value()
        if quantity == 0:
            self.total_water.setText("0 đ")
            self.totalWater = 0
            return
        resultGetPriceWater = self.totalController.cal_totalWater(
            self.num_water.value()
        )
        if resultGetPriceWater.success is False:
            return toast.toastWarning(resultGetPriceWater.message)

        dataRes = resultGetPriceWater.data
        self.totalWater = dataRes["total_number"]
        self.total_water.setText(f"{dataRes['total_money']} đ")

    def changeDay(self):
        self.frameWorking.clearLayoutChooseChair()
        self.listChair.setPlainText("")

        time = self.selectDay.text()
        result = self.movieController.getAllMovieInDate(time, "%d-%m-%Y")

        if result.success is False:
            toast.toastWarning(result.message)
            return

        self.clearListMovie()
        self.clearListCalendar()
        self.setDataMovies(result.data)
        self.renderSelectMovie()

    def setDataMovies(self, data):
        for item in data:
            itemList = list(item)
            self.listIdMovie.append(itemList[0])
            self.listMovie.append(itemList[1])

    def setDataCalendar(self, data):
        for item in data:
            itemList = list(item)
            self.listIdCalendar.append(itemList[0])
            self.listCalendar.append(
                time.convertTimeStampToString(itemList[1], "%H:%M %d-%m-%Y")
            )

    def changeValueSelectDay(self, value):
        self.calendar_window.close()
        self.selectDay.setText(value)

    def showFrameSelectCalendar(self, event):
        self.calendar_window = QtWidgets.QMainWindow()
        self.ui_select_calendar = Ui_SelectCalendar(
            self, self.selectDay.text(), "dd-MM-yyyy"
        )
        self.ui_select_calendar.setupUi(self.calendar_window)
        self.calendar_window.show()

    def clearListMovie(self):
        self.listMovie = ["Chọn phim"]
        self.listIdMovie = [0]
        self.nameMovie.clear()

    def clearListCalendar(self):
        self.listCalendar = ["Chọn lịch chiếu"]
        self.listIdCalendar = [0]
        self.calender.clear()

    def renderSelectMovie(self):
        self.nameMovie.addItems(self.listMovie)

    def renderSelectCalendar(self):
        self.calender.addItems(self.listCalendar)

    def changeMovie(self, index):
        self.clearListCalendar()
        self.frameWorking.clearLayoutChooseChair()
        self.listChair.setPlainText("")
        self.priceMovie = None

        if index <= 0:
            return

        indexSelected = self.nameMovie.currentIndex()
        self.handleAddCalendar(indexSelected)

    def changeCalendar(self, index):
        self.frameWorking.clearLayoutChooseChair()
        self.listChair.setPlainText("")
        self.timeRemaing.setText("")
        if index <= 0:
            return
        indexSelected = self.calender.currentIndex()

        result = self.calendarController.getRemaingMovie(
            self.listIdCalendar[indexSelected]
        )

        if result.success is False:
            toast.toastWarning(result.message)
            return

        dataList = list(result.data)

        timeMovie = dataList[0]
        playTime = dataList[1]
        room = dataList[2]
        now = gen_time.getNowTimestamp()
        played = int((now - playTime) / 60)

        if played > timeMovie:
            self.timeRemaing.setText(f"Đã hết phim")
        elif 0 < played < timeMovie:
            self.timeRemaing.setText(f"P{room} - {played}/{timeMovie} phút")
        else:
            if room is None:
                return
            self.timeRemaing.setText(f"P{room}")

    def handleAddCalendar(self, indexSelected):
        idMovie = self.listIdMovie[indexSelected]
        result = self.getCalendar(idMovie)

        if result.success is False:
            toast.toastWarning(result.message)
            return

        self.setDataCalendar(result.data)
        self.renderSelectCalendar()

    def getCalendar(self, idMovie):
        date = self.selectDay.text()
        return self.calendarController.getCalendar(idMovie, date)

    def clickBtnChooseChair(self):
        if (
            self.frameWorking.frameWorkingShowed is True
            or self.calender.currentIndex() <= 0
        ):
            return

        resultGetSelectedChairs = self.seatController.getAllChairSelected(
            self.listIdCalendar[self.calender.currentIndex()]
        )

        if resultGetSelectedChairs.success is False:
            toast.toastWarning(resultGetSelectedChairs.message)
            return

        listChairsSelected = [x[0] for x in resultGetSelectedChairs.data]
        self.frameWorking.showFormChooseChair(listChairsSelected)
        return

    def setSelectedIdChair(self, selecting: list):
        self.selecting = selecting
        self.listChair.setPlainText(", ".join(map(str, selecting)))
        return

    def getInfoTicket(self):
        ticket = Ticket(
            self.nameCustomer.text(),
            self.email.text(),
            str(self.listIdCalendar[self.calender.currentIndex()]),
            len(self.selecting),
            self.num_popcorn.value(),
            self.num_water.value(),
            self.totalTicket,
            self.totalPopcorn,
            self.totalWater,
        )
        return ticket

    def authenTicket(self):
        ticket = self.getInfoTicket()
        result = self.ticketController.checkInfoTicket(ticket)
        if result.success is False:
            toast.toastWarning(result.message)
            return False
        self.ticketAuthened = result.data
        return True

    def order(self):
        order = self.orderController.orderTicket(
            self.ticketAuthened, self.selecting, self.staffCurrent.id
        )

        if order.success is False:
            toast.toastWarning(order.message)
            return
        self.payment_window.destroy()
        self.payment_ui = None
        resultSendMail = self.ticketController.sendMailTicket(
            self.ticketAuthened.id,
            self.nameMovie.currentText(),
            self.calender.currentText(),
            self.selecting,
            self.nameCustomer.text(),
            self.email.text(),
        )
        self.cleanData()
        if resultSendMail.success is False:
            toast.toastWarning(resultSendMail.message)
        else:
            toast.toastInfo("Đặt vé thành công")
