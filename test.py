import numpy as np
import mysql.connector
import pydicom
import datetime
mydb = mysql.connector.connect(
  host="137.82.56.208",
  user="ghazal",
  passwd="ghazal",
  database="cardiac"
)
ds = pydicom.dcmread('/media/ghazal/01D176301231DAE0/depth for blob/007_1.2.840.113619.2.185.2838.1343722344.0.10.512.dcm')

id=ds.PatientID
date=ds.StudyDate
year=date[0:4]
month=date[4:6]
day=date[6:]
date_str=year+'-'+month+'-'+day
mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM exam where (HospID='00561967' OR Patient_ID='00561967') AND DateOfStudy=$date_str  ")
mycursor.execute("SELECT * FROM exam where (HospID=%s OR Patient_ID=%s) AND DateOfStudy=%s", (id,id,date_str))
myresult = mycursor.fetchall()
col_num=0

for x in myresult:
  # print(type(x))
  print(x)
  for y in x:
    if (y!=None) and (type(y)!=str) and (y!=1) and type(y)!=datetime.datetime and (type(y)!=int):
            # (col_num!=111)\
            # and (col_num!=137):
      print('y: ',y)
      print('type y:, ',type(y))
      print('col_num: ', col_num)
    col_num=col_num+1
