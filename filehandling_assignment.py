#1. Write a program to create a new file and write data to it ?
# f=open("new_file.txt","x")
# f=open("new_file.txt","w")
# f.write("yes..it's me!")
# f.write("everything is fine")
# f.close()
#2. Write a program to read data from a file ? (using read() and readline())?
# f=open("new_file.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readlines())
#3. Write a program to  solve Quadratic Equation ?
# import math
# a=float(input("enter coefficient a:"))
# b=float(input("enter coefficient b:"))
# c=float(input("enter coefficient c:"))
# dis=b**2-4*a*c
# if dis>0:
#     root1=(-b+math.sqrt(dis))//(2*a)
#     root2=(-b+math.sqrt(dis))//(2*a)
#     print("roots are:",root1,root2)
# elif dis==0:
#     root=-b/(2*a)
#     print("roots are:",root)
# else:
#     real_part=-b/(2*a)
#     image_part=math.sqrt(abs(dis))/(2*a)
#     root1=complex(real_part,image_part)
#     root2=complex(real_part,image_part)
# print("the root are complex:",root1,root2)
# 4. Write a program to perform read and write operation on a CSV File ?
# import csv
# with open("C:/Users/THEJAA/Downloads/income(1).csv","r") as csvfile:
#     read=csv.reader(csvfile)
#     for row in read:
#         print(','.join(row))
# with open("C:/Users/THEJAA/Desktop/python/Book1.csv","w") as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerow("SN","Name","Contribution")
#     writer.writerow("1","Linus Torvalds","Linux Kernel")
#     writer.writerow("2","Tim Berners-Lee","World Wide Web")
#     writer.writerow("3","Guido van Rossum","Python Programming")
#6. Write a program to append data to an existing file ?
f=open("new_file.txt","a")
f.write("i love you")
f.close()
#5. Write a program to write JSON data to a file ?
#write content
import json
dictionary={
    "name":"theja",
    "roll no":31,
    "age":21,
    "phone no":2349959555
}
obj=json.dumps(dictionary)
with open("sample.json","w") as outfile:
    outfile.write(obj)
#read content
# import json
# with open("sample.json","r") as openfile:
#     json_object=json.load(openfile)
#     print(json_object)







