dog = input("What breed is your dog?")

print("dog") # print string "dog"
print(dog)   # print variable dog


#data types

var1 = 123 			# interger (int)
var2 = "German Shepard" 	# string (str)
var2_a = 'single quotes'
var2_b = """ doc-string """
var3 = 123.05 			# float (float)
var4 = [1, 2, 3, 4] 		# list
var5 = {1, 2, 3} 		# tuple
var6 = False 			# boolean (bool)

#indexing
lst = ["Apple", "Banana", "orange", "uva"]

print(lst[0:4:2])
print(lst[0])	#"Apple"
print(lst[1])	#"Banana"
print(lst[2])	#"orange"


var7 = "grass"
var7[0]		#"g"

#spliting
var8 = "grass is green"

var8[0:6] 	#"grass "

var8[:6]	#"grass "

var8[6:]	#"is green"


#numbers are not iterable

#for loops
num_list = [1, 2, 3, 4, 5]

for var in num_list:
    print(var)

"""
Output:
1
2
3
4
5
"""

for num in num_list:
    print(10**num)

"""
Output:
10
100
1000
10000
100000
"""

#range

#range(start, end, step)
for x in range(0, 11):
    print(x)

for x in range(0, 11, 2):
    print(x)


10 / 2 # division
10 + 2 # adding
10 - 2 # substraction
10**2  # exponent
10 % 2 # remainder

# 11 % 2 = 1


#comparing

# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal
# = assign content to variable
# and - both conditions true
# or = one codition true
# not - not False = True
#     - not True = False


#if conditions
if 3 > 10:
   print("I am bigger than 10")
else:
   print("I am smaller than 10")





