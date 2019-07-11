import pymysql

mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
cursor = mydb.cursor()
try:
    # Type of 'config' data should be changed, the max size of varchar is 21845
    cursor.execute("create table config_md5 (ip varchar(40), config text(99999), md5_config varchar(999))")
except pymysql.err.InternalError as e:
    code, msg = e.args
    print('Error MSG: ' + msg)