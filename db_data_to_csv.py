import csv
import sqlite3
import sys

cnx=sqlite3.connect("mytestDB")
cursor=cnx.cursor()

qry_ext="select * from my_table_2";
data=cursor.execute(qry_ext)

cnx.row_factory=sqlite3.Row
cursor=cnx.execute("SELECT * From my_table_2")
row=cursor.fetchone()
titles=row.keys()


if sys.version_info<(3,):
    fh=open("output2.csv",'wb')
else:
    fh=open("output2.csv",'w')

writer=csv.writer(fh,delimiter=';')
#first_item=next(data)
#writer.writerow(first_item.keys())
writer.writerow(titles)
writer.writerows(data)

fh.close()
cnx.close()