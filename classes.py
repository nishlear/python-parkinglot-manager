class NguoiGuiXe:
    def __init__(self, name, phone):
        self.phone = phone
        self.name = name

    def __str__(self):
        return f"{self.name},{self.phone}"

class Xe:
    def __init__(self, plate, vehicleType):
        self.plate = plate
        self.vehicleType = vehicleType

    def __str__(self):
        return f"{self.plate},{self.vehicleType}"

class VeGuiXe:
    def __init__(self, cardID, staffID, cash):
        self.cardID = cardID
        self.staffID = staffID
        self.cash = cash
    
    def __str__(self):
        return f"{self.cardID},{self.staffID},{self.cash}"

class NhanVien:
    def __init__(self, staffID, name, phone):
        self.staffID = staffID
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.staffID},{self.name},{self.phone}"
    
class SoHuu:
    def __init__(self, phone, plate):
        self.phone = phone
        self.plate = plate

    def __str__(self):
        return f"{self.phone},{self.plate}"
    
class Cam:
    def __init__(self, phone, cardID):
        self.phone = phone
        self.cardID = cardID

    def __str__(self):
        return f"{self.phone},{self.cardID}"

class QuanLi:
    def __init__(self, staffID, cardID):
        self.staffID  = staffID
        self.cardID = cardID

    def __str__(self):
        return f"{self.staffID},{self.cardID}"