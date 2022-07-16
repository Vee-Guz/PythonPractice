#first practice
"""Fucntion checks if the num is btw 10 and 20
if it is print yay!
else print boo!

Requirements:
-Variable
-input
-if-else

Extra pnts. if you site the num
ex. 1 is not between 10 and 20
"""

input_num = int(input("Write a number: "))

if input_num > 10 and input_num < 20:
   print("yay!")
   print(str(input_num) + " is between 10 and 20")
else:
   print("boo!")
   print(str(input_num) + " is not between 10 and 20")

