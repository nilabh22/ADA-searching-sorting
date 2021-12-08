## Python Program for Linear Search ##

def linear_search(arr, item): # defining a function
    for i in range(len(arr)): # Loop till the length of the array.
        if arr[i] == item: # check if item is equal to the the element at ith index in array.
            return f"Item is found at index: {i}" # return the index
    print("Item doesn't exist in the array")

# Tests
print(linear_search([1,2,3,4,5], 3))