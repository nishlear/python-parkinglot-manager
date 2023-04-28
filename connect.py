import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database='parking'
)

cursor = mydb.cursor()

# vehicle
def addVehicle(plate, type):
    val = (plate, type)
    sql = "INSERT INTO Xe VALUES (%s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "xe đã được thêm vào database.")

def removeVehicle(plate):
    val = (plate)
    sql = "DELETE FROM Xe WHERE plate = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "xe đã được xoá khỏi database")

def showVehicle():
    sql = "SELECT * FROM Xe"
    cursor.execute(sql)
    vehicleList = cursor.fetchall()

    for x in vehicleList:
        print(x)

def updatePlateVehicle(updatedPlate, vehicleType):
    val = (updatedPlate, vehicleType)
    sql = "UPDATE Xe SET Plate = %s WHERE vehicleType = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("Thông tin biển số đã được thay đổi")

def updateTypeVehicle(plate, updatedVehicleType):
    val = (updatedVehicleType, plate)
    sql = "UPDATE Xe SET vehicleType = %s WHERE plate = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("Thông tin loại xe đã được thay đổi")

# staff
def addStaff(name, phone):
    val = (None, name, phone)
    sql = "INSERT INTO NhanVien VALUES (%s, %s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "nhân viên đã được thêm vào database.")

def removeStaff(id):
    val = (id,)
    sql = "DELETE FROM NhanVien WHERE workerID = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "nhân viên đã được xoá khỏi database")

def showStaff():
    sql = "SELECT * FROM NhanVien"
    cursor.execute(sql)
    staffList = cursor.fetchall()

    for x in staffList:
        print(x)

def updateStaffInfo(id, name, phone):
    val = (name, phone, id)
    sql = "UPDATE NhanVien SET name = %s, phone = %s WHERE workerID = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("Thông tin nhân viên đã được thay đổi")

# nguoi gui xe 

def addPerson(phone, name):
    val = (phone, name)
    sql = "INSERT INTO NguoiGuiXe VALUES (%s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "người gửi xe đã được thêm vào database")

def removePerson(phone):
    val = (phone)
    sql = "DELETE FROM NguoiGuiXe WHERE Phone = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "người gửi xe đã được xoá khỏi database")

def showPerson():
    sql = "SELECT * FROM NguoiGuiXe"
    cursor.execute(sql)
    personList = cursor.fetchall()

    for x in personList:
        print(x)
    
def updatePersonName(phone, name):
    val = (name, phone)
    sql = "UPDATE NguoiGuiXe SET name = %s WHERE Phone = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("Tên người gửi xe đã được thay đổi")

def updatePersonName(phone, name):
    val = (name, phone)
    sql = "UPDATE NhanVien SET Phone = %s WHERE Name = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("SDT người gửi xe đã được thay đổi")

# ve gui xe
def addTicket(staffID, cash, plate):
    val = (None, staffID, cash, plate)
    sql = "INSERT INTO VeGuiXe VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "vé gửi xe đã được thêm vào database")

def removeTicket(ticketID):
    val = (ticketID,)
    sql = "DELETE FROM VeGuiXe WHERE ticketID = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "vé gửi xe đã được xoá khỏi database")

def showTicket():
    sql = "SELECT * FROM VeGuiXe"
    cursor.execute(sql)
    ticketList = cursor.fetchall()

    for x in ticketList:
        print(x)

def updateTicket(workerID, cash, plate):
    val = (workerID, cash, plate)
    sql = "UPDATE VeGuiXe SET workerID = %s, cash = %s WHERE plate = %s;"
    cursor.execute(sql, val)
    mydb.commit()

    print("Thông tin vé gửi xe đã được thay đổi")

