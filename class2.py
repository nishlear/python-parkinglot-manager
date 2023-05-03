class NhanVien:
    def __init__(self, staffID, name, phone):
        self.staffID = staffID
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.staffID},{self.name},{self.phone}"
class VeGuiXe:
    def __init__(self, ticketID, staffID, memberID, cash, plate, type, time_in, time_out):
        self.ticketID = ticketID
        self.staffID = staffID
        self.memberID = memberID
        self.cash = cash
        self.plate = plate
        self.type = type
        self.time_in = time_in
        self.time_out = time_out

    def __str__(self):
        return f"{self.ticketID},{self.staffID},{self.memberID},{self.cash},{self.plate},{self.type},{self.time_in},{self.time_out}"

class ThanhVien:
    def __init__(self, memberID, plate, name):
        self.memberID = memberID
        self.plate = plate
        self.name = name
    
    def __str__(self):
        return f"{self.memberID},{self.plate},{self.name}"
