import math ### math library to use inbuilt functions ###
# floor() method in Python rounds a number down to the nearest integer, if necessary, and returns the output

def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start + end) / 2)
    while not (array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start + end) / 2)
        # print(start, middle, end)
    if array[middle] == value:
        return f"The value you searched is at index: {middle}"
    else:
        return "The value doesn't exist"

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))

"""
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME

"""
