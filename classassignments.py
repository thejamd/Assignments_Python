# 1. Define a class which has at least two methods one, to get a string from console  input and other is to print the string in uppercase.

# 2. Define a class, which have a class parameter and have a same instance parameter.

# 3. Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.

# 4. Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.

# 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. 
# 1. Define a class which has at least two methods one, to get a string from console  input and other is to print the string in uppercase
# class String:
#     def __init__(self,str):
#         self.str=str
#     def strin(self):
#         self.str=input("enter the string")
#     def upper(self):
#         print(self.str.upper())
#         # if hasattr(self,'str'):
#         #     print("Upper Case Of Given string",self.str.upper())
#         # else:
#         #     print("There is no string")
# obj=String("")
# obj.strin()
# obj.upper()

# 2. Define a class, which have a class parameter and have a same instance parameter.
# class Parameter:
#     classpara="this is a sentance"
#     def __init__(self,instpara):
#         self.instpara=instpara
# obj1=Parameter("Instance1")  
# obj2=Parameter("Instance2") 
# print(obj1.instpara)
# print(obj2.instpara)
# 3. Define a class named Circle which can be constructed by radius. The Circle class has a method which can compute the area.
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         self.area=3.14*(self.radius*self.radius)
#         return self.area
# obj=Circle(6)
# res=obj.area()
# print(res)
# 4. Define a class named BankAccount. This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account.
# class BankAccount:
#     def __init__(self,initial_balance=0):
#         self.balance=initial_balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount
#             print("bank balance after deposit:",self.balance)
#         else:
#             print("invalid deposit")
#     def withdraw(self,amount):
#         if 0<amount<=self.balance:
#             self.balance-=amount
#             print("bank balance after withdraw:",self.balance)
#         elif amount>self.balance:
#             print("insufficient account balance")
#         else:
#             print("invalid account")
#     def get_balance(self):
#         print("your account balance is",self.balance)

# obj=BankAccount(1000)
# print(obj.deposit(500))
# print(obj.withdraw(300))
# print(obj.get_balance())

# 5.Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. 
class Shape:
    def __init__(self,length):
        self.length=length
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
         super().__init__(self)
         self.length=length
        # a=length**2
        # print(a)
    def area(self):
        return self.length**2
shape=Shape(6)
square=Square(6)
print(shape.area())
print(square.area())



        

