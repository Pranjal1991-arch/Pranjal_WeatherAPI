# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
list = [1, 3, 5, 6, 2, 8]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, list))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, list))
