from get import snmpv2_get
import datetime
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler


def collect_store_cpu_usage():
    cur_time = datetime.datetime.now()
    cpu_usage_5s = snmpv2_get("192.168.1.131", "tcpipro", "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)

    # Write data into database
    mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
    cursor = mydb.cursor()
    cursor.execute("insert into routerdb (time, cpu) values (%s, %s)", (cur_time, cpu_usage_5s[1]))
    mydb.commit()
    mydb.close()


def schedule_task():
    scheduler = BlockingScheduler()

    scheduler.add_job(func=collect_store_cpu_usage, trigger='interval', seconds=5,
                      end_date=datetime.datetime(2019, 7, 28, 23, 5),
                      id='Collect CPU usage every 5s')
    scheduler.start()

schedule_task()