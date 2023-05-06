import mysql.connector
import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database='parking'
)
cursor = mydb.cursor()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# staff
def addStaff(name, phone):
    sql = "INSERT INTO staff (name, phone) VALUES (%s, %s)"
    val = (name, phone)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Nhân viên {name} đã được thêm vào.")

def addStaffwithAccount(name, phone):
    sql = "INSERT INTO staff (name, phone) VALUES (%s, %s)"
    val = (name, phone)
    cursor.execute(sql, val)
    staff_id = cursor.lastrowid  # get the staffID of the newly inserted staff
    
    # default account
    username = "staff" + str(staff_id)
    password = "123"

    sql = "INSERT INTO account (staffID, username, password) VALUES (%s, %s, %s)"
    val = (staff_id, username, password)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Nhân viên {name} đã được thêm vào cùng với tài khoản.")

def removeStaff(staffID):
    sql = "DELETE FROM staff WHERE staffID = %s"
    val = (staffID,)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Nhân viên có ID {staffID} đã được xoá.")

def showStaff():
    cursor.execute("SELECT * FROM staff")
    result = cursor.fetchall()
    # for row in result:
    #     print(row)
    return result

def showStaffwithAccount():
    cursor.execute("""
    SELECT s.staffID, s.name, s.phone, a.username, a.password
    FROM staff s
    LEFT JOIN account a ON s.staffID = a.staffID;
    """)
    result = cursor.fetchall()
    return result

def updateStaff(staffID, name=None, phone=None):
    sql = "UPDATE staff SET "
    updates = []

    if name is not None:
        updates.append(f"name='{name}'")
    if phone is not None:
        updates.append(f"phone='{phone}'")

    if len(updates) == 0:
        return # nothing to update

    sql += ",".join(updates) + f" WHERE staffID={staffID}"
    cursor.execute(sql)
    mydb.commit()
    print(f"Thông tin nhân viên ID {staffID} đã được cập nhật")

def findStaff(x, y):
    sql = f"SELECT * FROM staff WHERE {x} = '{y}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
print(findStaff("name", 'Tran Khoa'))
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
    print(f"Cập nhật thông tin thành viên ID {memberID} thành công.")

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

def member_getColumnName(column_index):
    column_names = ["memberID", "name", "plate"]
    return column_names[column_index]

# ticket
def addTicket(staffID, plate, vehicletype): # Quet xe di vao
    # Check if plate is already registered in database as a member
    sql = "SELECT memberID FROM member WHERE plate = %s"
    val = (plate,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result:
        memberID = result[0]
        cash = 0
    else:
        memberID = None
        # Xe dap = 0
        # Xe may = 1
        # Xe hoi = 2
        if (vehicletype == 0):
            cash = 2
        if (vehicletype == 1):
            cash = 5
        if (vehicletype == 2):
            cash = 20

    val = (None, staffID, memberID, cash, plate, vehicletype, current_time, None)
    sql = "INSERT INTO ticket VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, val)
    mydb.commit()

    print(f"Xe {plate} đã được thêm vào database.")
# addTicket(8, '43-A3 99999', 2)
# addTicket(11, '32-S2 81221', 0)
def saveTicket(plate): # Quet xe di ra
    sql = "UPDATE ticket SET time_out = %s WHERE plate = %s"
    val = (current_time, plate)
    cursor.execute(sql, val)
    mydb.commit()
    print(f"Xe {plate} đã rời khỏi bãi xe.")
# saveTicket('43-A3 99999')
def removeTicket(ticketID):
    #TODO: print plate of deleted ticket
    val = (ticketID,)
    sql = "DELETE FROM ticket WHERE ticketID = %s"
    cursor.execute(sql, val)
    mydb.commit()

    print(f"Xoá thành công vé xe có ID {ticketID}")

def showTicket():
    sql = "SELECT * FROM ticket"
    cursor.execute(sql)
    result = cursor.fetchall()

    # for x in result:
    #     print(f"({x[0]}, {x[1]}, {x[2]}, {x[3]}, {x[4]}, {x[5]}, {x[6].strftime('%Y-%m-%d %H:%M:%S')}, {x[7]})")
    return result

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

def findTicket(x, y):
    sql = f"SELECT * FROM ticket WHERE {x} = '{y}'"
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

# account
def createAccount(staffID, username, password):
    sql = "INSERT INTO account VALUES (%s, %s, %s, %s)"
    val = (None, staffID, username, password)
    cursor.execute(sql, val)
    mydb.commit()

    print(f'Tài khoản của nhân viên có ID {staffID} đã được thêm vào.')

def deleteAccount(usernameID):
    sql = "DELETE FROM account WHERE usernameID = %s"
    val = (usernameID)
    cursor.execute(sql, val)
    mydb.commit()

    print(f'Tài khoản có UID {usernameID} đã được xoá')

def changeUsername(usernameID):
    pass

def changePassword(usernameID):
    pass

def login(username, password):
    sql = "SELECT * FROM account WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    data = cursor.fetchone()

    # print(data)
    return data

def showAccount():
    sql = "SELECT * FROM account"
    cursor.execute(sql)
    result = cursor.fetchall()

    # for row in result:
        # print(row)
    return result

def updateAccount(staffID, username=None, password=None):
    sql = "UPDATE account SET "
    updates = []

    if username is not None:
        updates.append(f"username='{username}'")
    if password is not None:
        updates.append(f"password='{password}'")

    if len(updates) == 0:
        return # nothing to update

    sql += ",".join(updates) + f" WHERE staffID={staffID}"
    cursor.execute(sql)
    mydb.commit()
    print(f"Tài khoản nhân viên ID {staffID} đã được cập nhật")
# print(showStaff()[0][1])