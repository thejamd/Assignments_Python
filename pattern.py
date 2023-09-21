#    *
#    *  *
#    *  *  *
#    *  *  *  *
#    *  *  *  *  *
 #a=int(input("enter the size of pattern"))
# for i in range(a):
#     for j in range(i+1):
#         print(" * ",end='')
#     print()
    # 1
    # 2  3
    # 4  5  6
    # 7  8  9  10
# p=1
# for i in range(1,5):
#     for j in range(i):
#         print(p , end=" ")
#         p+=1
 #   print()
    # A
    # A  B
    # A  B  C
    # A  B  C  D
# for i in range(65,69):
#     for j in range(65,i+1):
#         print(chr(j),end=' ')
#     print()
    # A
    # B  C
    # D  E  F
    # G  H  I  J
# n=4
# p=65
# for i in range(n):
#     for j in range(i+1):
#          print(chr(p),end=' ')
#          p+=1

#     print()



    # 2
    # 4   6
    # 8   10  12
    # 14  16  18  20

# n=4
# p=2
# for i in range(n):
#      for j in range(i+1):
#           print(p,end=' ')
#           p+=2
#      print()

               #
           #       #
        #      #      #
     #     #      #       #

#n=int(input("enter the size of pattern"))
# n=4
# for i in range(n):
#      for j in range(i,n):
#           print('  ',end=' ')
#      for j in range(i):
#           print("# ",end=' ')
#      for j in range(i+1):
#           print("# ",end=' ')
#      print()



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
n=4
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end='')
    print()


