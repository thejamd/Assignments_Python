#1. Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".
# num1=int(input("enter the numbers:")) 
# def my_even(num1):
#     if num1%2==0:
#         print("enetred number is even")
#     else:
#         print("entered number is odd")
# my_even(num1)
#2. Write a program to define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# d=dict()
# def my_dict():
#    for i in range(1,21):
#        d[i]=i**2
#    return d
# result=my_dict()
# for key,value in result.items():
#  print(d)

#3. Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)
# def vowels(str):
#   str=input("enter the string :")
#   str1="AOEIUaeiou"
#   result_str=[i for i in str if i not in str1]
#   return result_str
# result=vowels(str)
# print(result)
#4. Write a program to display Powers of 2  using Anonymous functions?(lambda,map).
# power=10
# num_power=map(lambda x:x**x,range(power))
# m=list(num_power)
# print(m)

#7.Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.

# key=input("enter a list ".split(','))
# valuelist=input("enter another list".split(','))
# def key_values(keys,value):
#     if len(keys)!=len(value):
#      print("not same length,must have a same length")

# dic1=dict(zip(key,valuelist))
# print(dic1)

#11. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.(implement generator).

# def divisible(n):
#    for i in range(n+1):
#       if i%5==0 and i%7==0:
#          yield i
# print(list(divisible(1000)))

#10. Program to implement concept of decorator to calculate the time needed to execute one or more function in a program.
#12. Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator)
# def even(n):
#     for i in range(0,n+1):
#         if i%2==0:
#             yield i
# print(list(even(10)))


#8. Write a program to print fibonocci series using recursion.
# def fibb(n):
#    if n<=1:
#       return n
#    else:
#         return (fibb(n-1)+fibb(n-2))
# n=int(input("enter the numbers"))
# for i in range(n):
#  print("fibonacci series:",fibb(i))






# #9. Write a program to find the factorial of a number using recursion.

# # def fact(n):
# #    if n==1 or n==0:
# #      return 1
# #    else:
# #        return n*fact(n-1)
# # n=int(input("enter n value"))
# # # if n<0:
# # #    print("factorial not exist")
# # # else:
# # print("facoral of",n,"is",fact(n))
# # 5. Write a program to implement bubble-sort algorithm
# def bubble_sort(arr):
#     n = len(arr)
    
#     # Traverse through all elements in the list
#     for i in range(n):
#         # Last i elements are already in place, so we don't need to check them
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage:
# if __name__ == "__main__":
#     # Input list to be sorted
#     arr = [64, 34, 25, 12, 22, 11, 90]
    
#     # Call the bubble_sort function
#     bubble_sort(arr)
    
#     # Output the sorted list
#     print("Sorted array is:", arr)


# # 6. Write a program to implement binary-search algorithm
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1

#     while left <= right:
#         mid = left + (right - left) // 2

#         # Check if the middle element is equal to the target
#         if arr[mid] == target:
#             return mid
#         # If the target is greater, ignore the left half
#         elif arr[mid] < target:
#             left = mid + 1
#         # If the target is smaller, ignore the right half
#         else:
#             right = mid - 1

#     # Target element is not in the list
#     return -1

# # Example usage:
# if __name__ == "__main__":
#     # Sorted list to search in
#     arr = [2, 4, 6, 8, 10, 12, 14, 16]
#     target = 10
    
#     # Call the binary_search function
#     result = binary_search(arr, target)
    
#     if result != -1:
#         print(f"Element {target} is present at index {result}.")
#     else:
#         print(f"Element {target} is not present in the list.")

# # 13. Write a program to implement Insertion-Sort algorithm in python.
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
        
#         # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # Example usage:
# if __name__ == "__main__":
#     # Input list to be sorted
#     arr = [64, 34, 25, 12, 22, 11, 90]
    
#     # Call the insertion_sort function
#     insertion_sort(arr)
    
#     # Output the sorted list
#     print("Sorted array is:", arr)


# # 14. Program to implement Linear-Search Algorithm.
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
        
#         # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# # Example usage:
# if __name__ == "__main__":
#     # Input list to be sorted
#     arr = [64, 34, 25, 12, 22, 11, 90]
    
#     # Call the insertion_sort function
#     insertion_sort(arr)
    
#     # Output the sorted list
#     print("Sorted array is:", arr)


# # 15. Program to implement Selection-Sort Algorithm.
# def selection_sort(arr):
#     for i in range(len(arr)):
#         # Find the minimum element in the remaining unsorted part of the list
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         # Swap the found minimum element with the first element
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# # Example usage:
# if __name__ == "__main__":
#     # Input list to be sorted
#     arr = [64, 34, 25, 12, 22, 11, 90]
    
#     # Call the selection_sort function
#     selection_sort(arr)
    
#     # Output the sorted list
#     print("Sorted array is:", arr)


# # 16. Write a Python program to find the second smallest number in a list using function.
# def find_second_smallest(arr):
#     if len(arr) < 2:
#         return "List is too short to find the second smallest element."

#     smallest = float('inf')  # Initialize with positive infinity
#     second_smallest = float('inf')  # Initialize with positive infinity

#     for num in arr:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest and num != smallest:
#             second_smallest = num

#     if second_smallest == float('inf'):
#         return "There is no second smallest element in the list."
#     else:
#         return second_smallest

# # Example usage:
# if __name__ == "__main__":
#     # Input list
#     arr = [64, 34, 25, 12, 22, 11, 90]

#     # Call the find_second_smallest function
#     result = find_second_smallest(arr)
    
#     print("Second smallest element is:", result)


