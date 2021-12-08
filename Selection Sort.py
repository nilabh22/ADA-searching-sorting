def selectionSort(customList): # defining a function which will receive a custom list as a parameter.
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    return customList

cList = [2,1,7,6,5,3,4,9,8]
print("Original array is: {}".format(cList))
selectionSort(cList)
print("Sorted array is: {}".format(cList))