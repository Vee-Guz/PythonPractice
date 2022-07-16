""" Function named sum_of_items
argument list of nums ex. [1, 2, 3]
print out the sum of list values

Requirements:
loops, functions, and list
"""

def sum_of_items(num_list):
    total = 0
    for number in num_list:
        total += number
    print("The sum of the list is: " + str(total))

sum_of_items([5, 3, 2, 0, 4, 7])

