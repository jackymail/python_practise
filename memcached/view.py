#!/usr/bin/python

import sys, MySQLdb, cache


def infomation_of_student():

   sql = "SELECT * FROM students"
   cached = cache.get_result(sql)
   if not cached:
     db = MySQLdb.connect(host='127.0.0.1', user="root", passwd="123456", db="student_management")
     cursor = db.cursor()
     cursor.execute(sql)
     result = cursor.fetchall()
     print result
     cache.set_result(sql,result)
   else:
       print("cached results")
       print_students(cached)

def print_students(students):
    print("students")
    print("-" * 15)
    for student in students:
        print(student[0],student[1],student[3],student[4],student[5],student[6])
infomation_of_student()
