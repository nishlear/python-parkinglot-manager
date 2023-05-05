import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database='parking'
)
cursor = mydb.cursor()

# staff
def addStaff(name, phone):
    sql = "INSERT INTO staff (name, phone) VALUES (%s, %s)"
    val = (name, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Nhân viên {name} đã được thêm vào.")

def removeStaff(staffID):
    sql = "DELETE FROM staff WHERE staffID = %s"
    val = (staffID,)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Nhân viên có ID {staffID} đã được xoá.")

def showStaff():
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    for row in result:
        print(row)

def updateStaff(staffID, name=None, plate=None):
    sql = "UPDATE staff SET "
    updates = []

    if name is not None:
        updates.append(f"name='{name}'")
    if plate is not None:
        updates.append(f"plate='{plate}'")

    if len(updates) == 0:
        return # nothing to update

    sql += ",".join(updates) + f" WHERE staffID={staffID}"
    cursor.execute(sql)
    mydb.commit()
    print(f"Staff with ID {staffID} updated successfully")

# member
def addMember(name, plate):
    sql = "INSERT INTO member (name, plate) VALUES (%s, %s)"
    val = (name, plate)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Thành viên {name} có biển số {plate} đã được lưu.")

def removeMember(memberID):
    sql = "DELETE FROM member WHERE memberID = %s"
    val = (memberID,)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Thành viên có ID {memberID} đã được xoá.")

def updateMember(memberID, name=None, plate=None):
    sql = "UPDATE member SET "
    updates = []

    if name is not None:
        updates.append(f"name='{name}'")
    if plate is not None:
        updates.append(f"plate='{plate}'")

    if len(updates) == 0:
        return # nothing to update

    sql += ",".join(updates) + f" WHERE memberID={memberID}"
    cursor.execute(sql)
    mydb.commit()
    print(f"Member with ID {memberID} updated successfully")

def showMember():
    sql = "SELECT * FROM member"
    cursor.execute(sql)
    result = cursor.fetchall()

    # for row in result:
    #     print(row)
    return result

def findMember(x, y):
    sql = f"SELECT * FROM member WHERE {x} = '{y}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

# ticket
def addTicket(staffID, memberID, cash, plate, vehicletype, time_in, time_out):
    val = (None, staffID, memberID, cash, plate, vehicletype, time_in, time_out)
    sql = "INSERT INTO ticket VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "vé gửi xe đã được thêm vào database")

def removeTicket(ticketID):
    val = (ticketID,)
    sql = "SELECT plate FROM ticket WHERE ticketID = %s"
    plate = cursor.fetchone()[0]

    sql = "DELETE FROM ticket WHERE ticketID = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print("Vé gửi xe mang biển số" + plate + "đã được xoá khỏi database")

def showTicket():
    sql = "SELECT * FROM ticket"
    cursor.execute(sql)
    result = cursor.fetchall()

    for x in result:
        print(x)

def updateTicket(ticketID, staffID=None, memberID=None, cash=None, plate=None, vehicletype=None, time_in=None, time_out=None):
    sql = "UPDATE ticket SET "
    updates = []

    if staffID is not None:
        updates.append(f"staffID={staffID}")
    if memberID is not None:
        updates.append(f"memberID={memberID}")
    if cash is not None:
        updates.append(f"cash={cash}")
    if plate is not None:
        updates.append(f"plate='{plate}'")
    if vehicletype is not None:
        updates.append(f"type={vehicletype}")
    if time_in is not None:
        updates.append(f"time_in='{time_in}'")
    if time_out is not None:
        updates.append(f"time_out='{time_out}'")

    if len(updates) == 0:
        return # không có gì để update

    sql += ",".join(updates) + f" WHERE ticketID={ticketID}"
    cursor.execute(sql)
    mydb.commit()
    print(f"Vé gửi xe với ID {ticketID} đã được update thành công")


