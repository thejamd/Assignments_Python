#1.program to implementthe concept of calender module
# import calendar
# year=int(input("enter the year"))
# month=int(input("enter the month"))
# cal=calendar.month(year,month)
# print(cal)
# print(calendar.calendar(year))
#check year is leap year 
# print(calendar.isleap(2003))
# 2.implement datetime Module
# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# y=datetime.datetime(2023,9,27)
# print(x.strftime("%B"))
# print(y.strftime("%A"))
# print(y.strftime("%a"))
# print(y.strftime("%b"))
# print(y.strftime("%H"))

# 3.time Module
# import time
# x=time.time()
# print(x)
# y=time.ctime()
# print(y)
# time_tuple=(2022,12,28,8,44,4,4,362,0)
# z=time.mktime(time_tuple)
# print(z)
# i=time.asctime(time_tuple)
# print(i)
# 4.operator Module
# import operator
# a=int(input("enter first num:"))
# b=int(input("enter second num:"))
# result=operator.add(a,b)
# res=operator.sub(a,b)
# multi=operator.mul(a,b)
# div=operator.truediv(a,b)
# floor=operator.floordiv(a,b)
# power=operator.pow(a,b)
# print("ADDITION VALUE:",result)
# print("SUBSTRACTION VALUE:",res)
# print("MULTIPLICATION VALUE:",multi)
# print("DIVISION VALUE:",div)
# print("divition:",floor)
# print("power:",power)
# 5.math module
import math
x=math.sqrt(25)
print(x)
y=math.pow(2,2)
print(y)
z=math.exp(5)
print(z)
w=math.factorial(5)
print(w)
