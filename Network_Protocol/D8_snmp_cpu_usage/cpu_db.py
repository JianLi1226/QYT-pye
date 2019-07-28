import datetime
import pymysql
from Day_6 import line_chart



## Use APscheduler to set intervals
# def collect_store_cpu_usage():
#     start_time = datetime.datetime.now()
#     collected_data = list()
#     for i in range(24):
#         cur_time =  start_time + datetime.timedelta(seconds= 5*i)
#         cpu_usage_5s = snmpv2_get("192.168.1.131", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)
#         collected_data.append((cur_time, cpu_usage_5s))
#         time.sleep(5)
#     print(collected_data)
#
#     # Create a new table
#     mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
#     cursor = mydb.cursor()
#     try:
#         # The table existed
#         cursor.execute("create table routerdb(id INTEGER AUTO_INCREMENT, time timestamp, cpu int, PRIMARY KEY (id) )")
#     except pymysql.err.InternalError as e:
#         code, msg = e.args
#         print('Error MSG: ' + msg)
#
#     #Store cpu usage info to database
#     for t, cpu in collected_data:
#         # Note cpu data is a tuple, second element is integer of cpu usage
#         # Datetime object can be directed inserted into mysql, with %s as flag
#         cursor.execute("insert into routerdb (time, cpu) values (%s, %s)", (t, cpu[1]))
#     mydb.commit()
#     mydb.close()


def read_from_db():
    mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
    cursor = mydb.cursor()
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(minutes=1)
    cursor.execute("select * from routerdb where time >=(%s) and time <=(%s)", (start_time, end_time))
    result = cursor.fetchall()
    collected_data = list()
    for row in result:
        collected_data.append((row[1], row[2]))
    mydb.commit()
    mydb.close()
    print(collected_data)
    return collected_data


data = read_from_db()
line_chart.mat_line(data)
