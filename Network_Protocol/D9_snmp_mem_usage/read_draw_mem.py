import datetime
import pymysql
from line_chart_mem import mat_line



def read_from_db():
    mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
    cursor = mydb.cursor()
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(minutes=1)
    cursor.execute("select * from router_mem where time >=(%s) and time <=(%s)", (start_time, end_time))
    result = cursor.fetchall()
    collected_data = list()
    for row in result:
        collected_data.append((row[1], row[2]))
    mydb.commit()
    mydb.close()
    print(collected_data)
    return collected_data


data = read_from_db()
mat_line(data)
