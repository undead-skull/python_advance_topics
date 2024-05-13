'''List Comprehension'''

nums = [1,2,3,4,5,6,7,8,9,10]


#traditional way of writing codes
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)
'''to get rid from this multiple line codes and make in a single line we use list comprehension'''


#example 1 using list comprehension
my_list = [n for n in nums]
print(my_list)

#example 2
my_list = [n*n for n in nums]
print("using list comprehension {}".format(my_list))

#using MAP function
my_list = map(lambda x : x*x, nums)
print("using map and lambda func {}".format(list(my_list)))



#EVEN Number using compreshension
my_even_list = [n for n in nums if n % 2== 0]
print("using list compreshension {}".format(my_even_list))

#even number using map
my_even_list = map(lambda x: x % 2== 0,nums)
print("using map {}".format(list(my_even_list)))


# using Filter
my_even_list = filter(lambda x : x % 2 == 0,nums)
print("using filter {}".format(list(my_even_list)))