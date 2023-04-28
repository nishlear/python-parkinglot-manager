import pandas as pd
from sqlalchemy import create_engine

# kết nối đến SQL Server
server = 'LAPTOP-1BHQJ95V'
database = 'parking'
username = 'dh'
password = '123123'
driver = '{ODBC Driver 17 for SQL Server}'
conn_str = f'mssql+pyodbc://dh:123123@LAPTOP-1BHQJ95V/parking?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn_str, echo = True)

# đọc dữ liệu từ file Excel
data_NguoiGuiXe = pd.read_excel('NguoiGuiXe.xlsx')
data_Xe = pd.read_excel('Xe.xlsx')
data_NhanVien = pd.read_excel('NhanVien.xlsx')
data_VeGuiXe = pd.read_excel('VeGuiXe.xlsx')

# lưu dữ liệu vào SQL Server
table_name = 'NguoiGuiXe'
data_NguoiGuiXe.to_sql(table_name, engine, index=False, if_exists='replace')
table_name = 'Xe'
data_Xe.to_sql(table_name, engine, index=False, if_exists='replace')
table_name = 'VeGuiXe'
data_VeGuiXe.to_sql(table_name, engine, index=False, if_exists='replace')
table_name = 'NhanVien'
data_NhanVien.to_sql(table_name, engine, index=False, if_exists='replace')

# đóng kết nối
engine.dispose()