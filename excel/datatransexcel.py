import pandas as pd
import pyodbc
import mysql.connector
# import openpyxl

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database='parking'
)

# kết nối với SQL Server
# server = 'ODBC Driver 17 for SQL Server'
# database = 'parking'
# user_name = "LAPTOP-1BHQJ95V\ADMIN"
# conn_str = f"Driver={{ODBC Driver 17 for SQL Server}};Server=LAPTOP-1BHQJ95V;Database=parking;Trusted_Connection=yes;"
# conn = pyodbc.connect(conn_str)

# truy vấn dữ liệu
query = "SELECT * FROM NguoiGuiXe"
data_NguoiGuiXe = pd.read_sql(query, conn)

query = "SELECT * FROM Xe"
data_Xe = pd.read_sql(query, conn)

query = "SELECT * FROM NhanVien"
data_NhanVien = pd.read_sql(query, conn)

query = "SELECT * FROM VeGuiXe"
data_VeGuiXe = pd.read_sql(query, conn)

# lưu dữ liệu vào file Excel
excel_file_1 = 'NguoiGuiXe.xlsx'
data_NguoiGuiXe.to_excel(excel_file_1, index=False)

excel_file_2 = 'Xe.xlsx'
data_Xe.to_excel(excel_file_2, index=False)

excel_file_3 = 'NhanVien.xlsx'
data_NhanVien.to_excel(excel_file_3, index=False)

excel_file_4 = 'VeGuiXe.xlsx'
data_VeGuiXe.to_excel(excel_file_4, index=False)