
import os

from dotenv import load_dotenv
load_dotenv()

import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connector.connect(host=os.getenv("DB_HOST"),database=os.getenv("DB_DATABASE"),user=os.getenv("DB_USERNAME"),password=os.getenv("DB_PASSWORD"))
	print("connected")
	if connection.is_connected():
		cursor = connection.cursor()
		try:
			
			print("executing..")
			table_desc = (
			"CREATE TABLE `users` ("
			"  `fullname` varchar(40) NOT NULL,"
			"  `dob` varchar(12) NOT NULL,"
			"  `phone_number` varchar(10) NOT NULL,"
			"  `balance` int NOT NULL,"
			"  `aadhar_number` varchar(12) NOT NULL,"
			"  `account_number` varchar(15) NOT NULL);")
			cursor.execute(table_desc)
		except Error as e:
			pass
		
except Error as e:
	print("Error while connecting to MySQL", e)

