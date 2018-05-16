import pymysql

#db connection

connection = pymysql.connect(host='localhost',
                             port=3306,
                            user='root',
                            passwd='Apr/2018',
                            database='ProjectLearn')

cur=connection.cursor()

cur.execute("select host,user from user")

print(cur.description)

print 'Connection Established!'

