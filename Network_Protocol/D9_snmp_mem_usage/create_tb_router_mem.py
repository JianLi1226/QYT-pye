import pymysql

mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
cursor = mydb.cursor()
try:
    # The table existed
    cursor.execute("create table router_mem(id INTEGER AUTO_INCREMENT, time timestamp, mem_percent int, PRIMARY KEY (id) )")
except pymysql.err.InternalError as e:
    code, msg = e.args
    print('Error MSG: ' + msg)
mydb.commit()
mydb.close()