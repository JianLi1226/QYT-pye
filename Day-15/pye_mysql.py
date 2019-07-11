import pymysql

homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1},
                 {'姓名': '学员2', '年龄': 33, '作业数': 5},
                 {'姓名': '学员3', '年龄': 32, '作业数': 10}]

# Connect to mysql DB
mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
cursor = mydb.cursor()
print(mydb)

#
try:
    cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

# To void table already exists error
except pymysql.err.InternalError as e:
    code, msg = e.args
    if code == 1050:
        print(msg)


for teacher in homework_dict:
    name = teacher['姓名']
    age = teacher['年龄']
    homework = teacher['作业数']
    cursor.execute("insert into qytang_homework_info values('%s', %d, %d)"%(name, age, homework))

mydb.commit()
