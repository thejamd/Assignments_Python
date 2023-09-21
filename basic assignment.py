#1.Write a program to check whether the entered number is postive or negative
#a=int(input("enter the numbers"))
#if a<0:
#    print("entered number is negative")
#else:
#    print("entered number is positive")
#2.Write a program to  swap two variables.
# a=20
# b=10
# t=a
# a=b
# b=t
# txt="after swapping value of a is {} and value of b is {}"
# print(txt.format(a,b))
#3.Write a program to  Determine If Year Is Leap Year
# yr=int(input("enter the year"))
# if (yr%400==0 and yr%100==0):
#     print("{0} is leap year and also a centuary year".format(yr))
# elif(yr%4==0 and yr%100!=0):
#     print("{0}  is a leap year".format(yr))
# else:
#    print("{0} is not a leap year".format(yr))
#4.Write a program check whether the given number is odd or even
# nbr=int(input("enter any number"))
# if nbr%2==0:
#   print("it's a even number")
# else:
#    print("it's a odd number")
#5.Write a program to print the fibonocci series.
# a=int(input("how many terms?"))
# n1=0
# n2=1
# count=0

# print("fibonocci sesies of {}".format(a))
# while count<a:
#    print(n1)
#    n3=n1+n2
#    n1=n2
#    n2=n3
#    count+=1

#8.Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.
# sum=0
# for i in range(1,50,2):
#     print(i)
#     sum=sum+i
# print("sum is :",sum)
#9.Write a program to find the factorial of the given number
# f=int(input("enter any number"))
# fact=1
# for i in range(1,f+1):
#    fact=fact*i
# print(fact)
#10.Write a program to Check if the given string  is Palindrome or not.
# x=input("enter the string")
# revstr=""
# for i in x:
#    print(i)
#    revstr=i+revstr
# print(revstr)
# if x==revstr:
#     print("entered string is palindrome")
# else:
#    print("not a palindrome")

#slice method
# x=input("enter the string")
# if x==x[::-1]:
#     print(x,"is palindrome")
# else:
#     print(x,"is not palindrome")

#11.Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.
# sum=0
# for i in range(100,201):
#     if i%7==0:
#       sum=sum+i
# print("sum is :",sum)
#12.Write a program to Display Multiplication Table
# multi=int(input("enter any number"))
# for i in range(1,11):
#     c=i*multi
#     print(i,"*",multi,"=",c)
#7.write a program to print prime number between given interval
# for num in range(1,20):
#  if num>1:
#   for i in range(2,num):
#       if num%i==0:
#            break
#       else:
#         print(num)
#pattern printing
# sqr=int(input("enter the size of pattern"))
# for i in range(sqr):
#    for j in range(sqr):
#       print(" * ",end='')
#    print()
#13.Write a program to calculate the area and perimeter of a rectangle.
# area=int(input("enter the sides of triangle"))
# a1=int(input())
# a2=int(input())
# print("{},{},{} are the sides of triangle".format(area,a1,a2))
# p=area+a1+a2
# a=(a1*a2)/2
# print("{} is the perimeter of triangle".format(p))
# print(a,"is the area of the triangle")
# 14.Write a program to find the sum of n' Natural Numbers.
# n=int(input("enter the n natural number" ))
# sum=n*(n+1)//2#floor operator ie. '//'is used for remove the point value
# print("Sum is :",sum)
#other method is using while loop
# n=int(input("enter n natural numbers"))
# if n<0:
#     print("its a negative value")
# else:
#     sum=0
#     while n>0:
#         sum+=n
#         n-=1
#       print("sum is ",sum)

#15.Write a program to find whether given no. is Armstrong or not.
# n=int(input("enetr the number"))
# l=len(str(n))
# sum=0
# temp=n
# while temp>0:
#    r=temp%10
#    sum=sum+r**l
#    temp=temp//10
# if n==sum:
#      print("armstrong")
# else:
#    print("not armstrong")
    



#16.Write a program to find the largest among 3 numbers.
# num1=int(input("enter the numbers"))
# num2=int(input())
# num3=int(input())
# if num1>num2:
#    print("num1 is largest number")
# elif num2>num3:
#    print("num2 is largest number")
# else:
#    print("num3 is largest number")

#17. Write a program to remove all punctuations from given string.
# str1="hello,guyss! how are you?"
# str1=str1.replace(",","")
# str1=str1.replace("?","")
# str1=str1.replace("!","")
# print(str1)
#19.Write a program to count the no:of each vowel in a given string
# str=input("enter the string")
# list1=["a","e","o","i","u"]
# count=0
# for i in str:
#      if i in list1:#here we use membership function
#           count+=1
# print(count)


# 20.Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.
# com1=complex(input("enter complex numbers"))
# com2=complex(input())
# addition=com1+com2
# sub=com1-com2
# mul=com1*com2
# div=com1/com2
# print("{} is sum\n{} is the substraction\n{} is the multiplication\n{} is the division of the complex numbers".format(addition,sub,mul,div))
#21. Find Value of the following expressions

# num_1 = 10

# num_2 = 11

 

# print(num_1 % num_2)

# print(num_1 - num_2)

# print(num_1 * num_2)

#22.Find the results of the following expressions (True or False)

# num_1=7

# num_2 = 6

 

# print(num_1 < num_2)

# print(num_1 > num_2)

# print(num_1 <= num_2)

# print(num_1 >= num_2)

# print(num_1==num_2)


#23.Find the results of the following expressions (True or False)

# num_1=3

# num_2 = 4

 

# print((num_1 < num_2) and (num_1 != num_2))

# print((num_2 >= num_1) or (num_1 > num_2))

# print(not (num_1 == num_2))

#24.Output of the following while loop

# i=1

# while (i<6):
#     print(i,end=' ')

#     i = i +1

#s25.elect the correct option

 

# customer_num =5

# invoice_num =1212

# print("Invoice No(s):")

# while(customer_num >0):

#      print("INV -", invoice_num)

#      invoice_num = invoice_num +3

#      customer_num = customer_num -1

#18. Write a program to  Display Triangle as follow :

#  1

#  2 2

#  3 3 3

#  4 4 4 4...
# n=4
# p=1
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=' ')
        
#     print()
#6.
# #******
# #*****
# #****
# #***
# #**
# #*

# n=6
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*",end='')
#     print()
# *
# **
# ***
# ****
# ****
# ***
# **
# *  
# n=4
# for i in range(n):
#     for j in range(i+1):
#         print("*",end='')
#     print()
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*",end='')
#     print()
#26. Write a python function to add ‘python’ at the end of a given string and return the new string. If the given string already ends with ‘python’ then add ‘java’. If the length of the given string is less than 5, then add ‘php’.
def python_fun(str):
    if str.endswith("python"):
        return str+"java"
    elif len(str)<5:
        return str+"php"
    else:
        return str+"python"
input_str=input("enter the string")
input=python_fun(input_str) 
print(input) 




















