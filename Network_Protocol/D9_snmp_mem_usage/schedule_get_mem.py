from get import snmpv2_get
import datetime
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler


def collect_store_mem_usage():
    cur_time = datetime.datetime.now()
    mem_used = int(snmpv2_get("192.168.1.131", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1])
    mem_free = int(snmpv2_get("192.168.1.131", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1])
    mem_used_pct = (mem_used / (mem_free + mem_used)) * 100
    # Write data into database
    mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
    cursor = mydb.cursor()
    cursor.execute("insert into router_mem (time, mem_percent) values (%s, %s)", (cur_time, mem_used_pct))
    mydb.commit()
    mydb.close()


def schedule_task():
    scheduler = BlockingScheduler()

    scheduler.add_job(func=collect_store_mem_usage, trigger='interval', seconds=5,
                      end_date=datetime.datetime(2019, 7, 28, 23, 5),
                      id='Collect MEM usage every 5s')
    scheduler.start()

schedule_task()