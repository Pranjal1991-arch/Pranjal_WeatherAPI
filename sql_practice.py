import mysql.connector

dbcon = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Slidingmode@1',
    )
dbcur = dbcon.cursor()  # handler created
#sqlstmt = "SELECT * FROM city;"
dbcur.execute("show databases")
mydata = dbcur.fetchall()
for i in mydata:
    print(i)
dbcon.close
#print(mydata)
#dbcon.close
