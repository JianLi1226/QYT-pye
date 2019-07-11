import pymysql

user_notify = '''
请输入查询选项：
输入 1：查询整个数据库
输入 2：基于姓名查询
输入 3: 基于年龄查询
输入 4：基于作业数查询
输入 0：退出
'''

mydb = pymysql.connect('192.168.64.131', 'lijian', 'rootdb', database='ljdb')
cursor = mydb.cursor()

# cursor.description will return a tuple of tuples where [0] for each is the column header
cursor.execute("select * from qytang_homework_info") # Must select the table with a query command first
num_fields = len(cursor.description) # Numbers of all column fields
field_names = [x[0] for x in cursor.description ]


def print_rows_with_header(rows):
    for row in rows:
        row_printed = ''
        for i in range(num_fields):
            row_printed += f'{field_names[i]}:{row[i]} '
        print(row_printed)


while True:
    print(user_notify)
    user_input = input('请选择：')
    if user_input == '0':
        break

    elif user_input == '1':
        cursor.execute("select * from qytang_homework_info")
        result = cursor.fetchall()
        print_rows_with_header(result)
        continue

    elif user_input == '2':
        user_sn = input('请输入学员姓名: ')
        if not user_sn:
            continue
        cursor.execute("select * from qytang_homework_info where 姓名 = '%s' "%(user_sn))
        result = cursor.fetchall()
        if result:
            print_rows_with_header(result)
        else:
            print('学员信息未找到！')

    elif user_input == '3':
        user_age = int(input('搜索大于输入年龄的学员，请输入学员年龄: '))
        if not user_age:
            continue
        cursor.execute("select * from qytang_homework_info where 年龄 > %d " % (user_age))
        result = cursor.fetchall()
        if result:
            print_rows_with_header(result)
        else:
            print('学员信息未找到！')

    elif user_input == '4':
        user_homework = int(input('搜索大于输入作业数的学员，请输入作业数量: '))
        if not user_homework:
            continue
        cursor.execute("select * from qytang_homework_info where 作业数 > %d " % (user_homework))
        result = cursor.fetchall()
        if result:
            print_rows_with_header(result)
        else:
            print('学员信息未找到！')
    else:
        print('输入错误！请重试！')