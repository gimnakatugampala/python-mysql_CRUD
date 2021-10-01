from os import curdir
import mysql.connector

config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'pythonproject'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()