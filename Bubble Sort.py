def bubbleSort(arr):
    length = len(arr) #finding the length of array to be sorted

    for i in range(length): # executing the outer loop
        for j in range(0,length-i-1): # execiting the inner loop
            if arr[j]>arr[j+1]: # comparing two consecutive values
                arr[j], arr[j+1] = arr[j+1], arr[j] #swapping the values if latter is greater
    return arr

arr = [6,87,43,25,7,31,89,90,0,21,43,65,76,23,65,87,23,65,23,31,65,87,433,544,565,876,432]
#arr = [3,5,2,4,0,1]
sorted_arr = bubbleSort(arr)
print(f"The Sorted array is: {sorted_arr}")