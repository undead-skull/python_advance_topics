""""Iterators"""
import sys

x = [1,2,3,4,5,6,7,8,9,10]

# for i/

print(x.__sizeof__())


y = map(lambda i : i**2, x)    

print(y)                            #its a object which stores iterator value

# print(sys.getsizeof(list(y)))   
# print(sys.getsizeof(y))



#####
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

print("*************")

# for _ in y:
#     print(_)
    
    
# print("*************")
# while y:
#     try:
#         print(next(y))
#     except StopIteration:
#         print("Loop Done")
#         break


"""Generators"""

def gen(n):
    for i in range(n):
        yield i

x = gen(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


#usage of generator
'''think you are processing a file and inside a file you are processing one line at a time
at that time we can use generator so that at a particular time memory will store only one line and process it'''

def csv_reader(file_name):
    for row in open(file_name,"r"):
        yield row
        
        


#generator comprehensions

x = (i for i in range(10))

print(x)    # it will give us a generator

for _ in x:
    print(_)