#6.Write a program to find the sum of all the elements in a list.
# list1=[12,3,2,4]
# print(sum(list1))
# list1=[]
# for i in range(5):
#     num=int(input("enter numbers:"))
    
#     list1.append(num)
# sum=0
# for i in range(5):
#     sum=sum+list1[i]
# print("sum is:",sum)

#2.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#string
# a=input("enetr any sequence of line")
# print(a)
# print(a.upper())
#list
# lines=[]

# while True:
#     line=input("enetr sequence of line")
#     if not line:
#         break
#     lines.append(line)

# #for line in lines:
# print(line.upper())

#8.Write a program that accepts a sentence and calculate the number of letters & digits
# digits=0
# letter=0
# str=input("enter the string")
# for i in str:
#     if i.isdigit():
#         digits+=1
#     elif i.isalpha():
#         letter+=1
#     else:
#         pass
# print("digits",digits)
# print("letters",letter)


#10.Write a program to implement List Comprehension
 #square
# x=[i**2 for i in range(0,50,2) if i%5==0]#even numbers that are divisible by 5
# print(x)
#12.Write a program to find the largest and smallest element from a list.
# list2=[]

# for i in range(5):
#     num=int(input("enter numbers"))
#     list2.append(num)
# print("maximum number is:",max(list2), "\nminimum number is :",min(list2))
#using list comprehension
# x=[i for i in range(1,33)]
# print("maximum:",max(x))
# print("minimum:",min(x))
#13.Write a Python program to print the numbers of a specified list after removing even numbers from it.
# x=[i for i in range(1,100)] 
# y=[]
# for i in x:
#     if i%2!=0:
     
#      y.append(i)
# print(y)
#comprehension
# w=[i for i  in range(1,100) ]

#14.Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30
# w=[]
# y=[i for i in range(1,31)]
# for i in y:
#     w.append(i**2)
# print(y)
# print(w)
# print(w[:5])
# print(w[-5:])
#comprehension
# y=[i**2 for i in range(1,31) ]
# print(y[:5])
# print(y[-5:])
#15.Write a Python program to insert a given string at the beginning of all items in a list. 
# list1=["apple","banana","cherry"]
# list2=[]
# y="fruit"
# for i in list1:
#     x=list1[i]+y
#     list2.append(x)
# print(list2)

# 1.Write a program to find the transpose of a matrix.

# x=[[1,2],
#    [3,2],
#    [3,3]]
# r=[[0,0,0],
#    [0,0,0]]

# for i in range(len(x)):#for row
#     for j in range(len(x[0])):#for column
#         r[j][i]=x[i][j]
#     for n in r:
#         print(n)


#using list comprehension
# p=int(input("enter the number of rows:"))
# q=int(input("enter the number of columns:"))
# pq1=print("enter the elements")
# pq=[[int(input()) for i in range(p)] for j in range(q)]
# print("matrix:")
# for i in range(p):
#     for j in range(q):
#         print((pq[i][j]),end=' ')
#     print()
# print("transpose of matrix:")
# pq2=[[0 for i in range(q)] for j in range(p)]
# for i in range(q):
#     for j in range(p):
#         pq2[j][i]=pq[i][j]
# for i in range(q):
#     for j in range(p):
#         print((pq2[i][j]),end=' ')
#     print()

# 4. Write a program to read dictionary values through keyboard and merge two dictionaries.

# d=dict()
# for i in range(1,11):
#  d[i]=i**2
# print(d)
# d1=dict()
# for j in range(1,11):
#  d1[j]=j**3
# print(d1)
# d1.update(d)
# print(d1)

#11.Write a program to implement Dictionary Comprehension 
# dict_1={x:x**3 for x in range(1,11)}
# print(dict_1)

# old_price={"book":11,"pen":3,"bag":120,"box":30}
# new_amt=10
# new_price={i:v+new_amt for (i,v) in old_price.items()}
# print(new_price)

# old={"id1":11,"id2":12,"id3":13,"id4":14}
# new={k:v for (k,v) in old.items() if v%2==0}
# print(new)
# old1={"g":14,"p":24,"y":44}
# new1={j:u for (j,u) in old.items() if u%2!=0 if u>11}
# print(new1)

# 9.Write a program to implement filter(), map() and reduce()
# def numbers(num):
#     return num%2==0
# num=[1,2,3,4,5,6]
# fil=filter(numbers,num)
# print(list(fil))








# # 17.  Write a Python program to add a key to a dictionary.
# dict1={"name":"theja","age":21,"occupation":"programmer"}
# dict1["place"]="kdlr"
# print(dict1)
# # 18. Write a Python script to concatenate following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# print(dic1|dic2|dic3)

# # 20. Write a Python program to sum all the items in a dictionary.
# sum1={"item1":12,"item2":1.2,"item3":10,"item4":20}
# print(sum(sum1.values()))

# # 21.  Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}

# #     Put at least 3 key-value pairs in your dictionary.
# #     Use a for loop to print out a series of statements such as "Willie is a dog."
# animals={"dog":"willie","cat":"birman","rat":"black rat"}
# for name,kind in animals.items():
#     print(f"{kind} is a {name}.")


#  # 19. Write a Python program to iterate over dictionaries using for loops.   
    

# places={"kerala":47,"tamilnadu":44,"andra":33,"karnadaka":56}
# for i in places.items():
#     print(i)

# #7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1 and n. And then the program should print the dictionary.
# dict11={}
# for i in range(1,11):
#     dict11[i]=i*i
# print(dict11)

# # 16.  Write a Python program to iterate over two lists simultaneously.
# list1=[1,2,3,4,5]
# list2=[22,33,44,55]
# for item1,item2 in zip(list1,list2):
#     print(item1,item2)
# # 9.Write a program to implement filter(), map() and reduce()
# # def numbers(num):
# #     return num%2==0
# # num=[1,2,3,4,5,6]
# # fil=filter(numbers,num)
# # print(list(fil))
# #map
# def sqr(num):
#     return num**2
# num=[1,2,3,4,5]
# squared=map(sqr,num)
# print(list(squared))

# #without def function convert string in to int
# str_num=["1","2","3","4","5"]
# int_num=map(int,str_num)
# print(int_num)
# print(list(int_num))
# print(list(str_num))

# def even(num):
#     return num%2==0
# num=[1,2,3,4,5,6,7,8,9]
# even_num=map(even,num)
# print(list(even_num))


# #filter
# numbers=[1,2,3,4,5,6]
# even_numbers=filter(lambda x:x%2==0,numbers)
# print(list(even_numbers))


# letters=["i","o","u","a","j","k"]
# vowels=["i","o","u","a","e"]
# def filter_vowels(letters):
#     return True if letters in vowels else False
# sds=filter(filter_vowels,letters)
# print(tuple(sds))

# def numbers(num):
#     return num%2==0
# num=[1,2,3,4,5]
# fil=filter(numbers,num)
# print(list(fil))



# #reduce
# from functools import reduce
# my_list=[1,2,3,4,5]
# num=reduce(lambda x,y:x*y,my_list)
# print(num)


#22. Write a python function to create and return a new dictionary from the given
#dictionary (subject: mark).
#Create a new dictionary with subject having marks more than 50.
#marks = {English: 40,&#39;Maths&#39;: 60, &#39;Hindi: 30,&#39;Chemistry&#39;: 46,&#39;Physics&#39;: 70}
# d=dict()
# def dictionary(marks):
#     for subject,mark in marks.items():
#         if mark>50:
#             d[subject]=mark
#         return d
# marks={"maths":69,"phy":70,"chemistry":19}
# result=dictionary(marks)
# print(result)
# # 23. Write a python function which accepts a sentence and finds the number of letters and
# # digits in the sentence.
# # It should return a dictionary in which the key should be letter count and value should be
# # digit count. Ignore the spaces or any other special character in the sentence.
# digit1=0
# alpha1=0
# d=dict()
# def python_fun(str):
#     for i in str:
#      if i.isalpha():
#         alpha1+=1
#      elif i.isdigit():
#         digit1+=1
#      result={"alpha1":alpha1,"digit1":digit1}
#      return result
# str="hello world" 
# result=python_fun(str)
# print(result)

# 24. Write a Python function which generates and returns a dictionary where the keys are
# numbers between 1 and n (both inclusive) and the values are square of keys.
 
 
def dict_fun(n):
   d=dict() 
   for i in range(1,n+1):
      d[i]=i**2
      i+=1
      return d
n=20
res=dict_fun(n)
print(res)
      
      
      












     


    


