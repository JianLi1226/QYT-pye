import pymysql



def create_tb_

    mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
    cursor = mydb.cursor()
    try:
        cursor.execute("create table syslog(id INTEGER AUTO_INCREMENT, time timestamp, mem_percent int, PRIMARY KEY (id) )")
    except pymysql.err.InternalError as e:
        # The table existed
        code, msg = e.args
        print('Error MSG: ' + msg)
    mydb.commit()
    mydb.close()