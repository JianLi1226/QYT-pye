#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456


# line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!'%(department1, depart1_m, COURSE_FEES_SEC)
# line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f The End!'%(department2, depart2_m, COURSE_FEES_Python)

line1 = 'Department1 name:{0:<10s} Manager:{1:<10s} COURSE FEES:{2:<10.2f} The End!'\
        .format(department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department2 name:{0:<10s} Manager:{1:<10s} COURSE FEES:{2:<10.2f} The End!'\
        .format(department2, depart2_m, COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)