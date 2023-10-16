import random
import pymysql
from Customer_CMDS import *
DB= pymysql.connect(host='localhost',user='t1',password='x')
CR=DB.cursor()
CR.execute(f"CREATE DATABASE Hotel_Taj")
CR.execute(f"use Hotel_Taj")
CR.execute(f"create table Customer(PID int(5), PName varchar(255), Age int, SUITE char(1), OCCUPANCY int, CHECKIN date, CHECKOUT date,ROOMNO int)")
CR.execute(f"create table Admin(ROOMNO int, AVAILABILITY char(1), SUITE char(1), PID int(5), CHECKIN date, CHECKOUT date)")
CR.execute(f"use Hotel_Taj")

BookRoom()
