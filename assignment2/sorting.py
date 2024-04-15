import sys
import random

#naive quick sort
def naive_quick_sort(arr, str, end):
    if end-str+1 < 2:
        return
    
    #choose a pivot element: typically the last element in the array
    pivot = arr[end]
    #position fot pivot after loop
    mid = str

    for i in range(str, end):
        #If element is smaller than pivot, change position
        if arr[i] <= pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1

    #move pivot postion to mid
    arr[mid], arr[end] = arr[end], arr[mid]

    #recursively apply quick sort to the left and right sub-arrays
    naive_quick_sort(arr, str, mid-1)
    naive_quick_sort(arr, mid+1, end)

#randomized quick sort
def randomized_quick_sort(arr, str, end):
    if end-str+1 < 2:
        return
    #if there are 2 lengths naive quick sort
    if end-str+1 == 2:
        naive_quick_sort(arr, str, end);
        return
    
    #pick 3 random indices
    median_index = end-1
    random_indexs = random.sample(range(str, end+1), 3)
    #sort to get median
    random_values = [arr[random_indexs[0]], arr[random_indexs[1]], arr[random_indexs[2]]]
    naive_quick_sort(random_values, 0, 2)
    #get median value index
    for i in random_indexs:
        if arr[i] == random_values[1]:
            median_index = i

    #change last value and random value
    arr[end], arr[median_index] = arr[median_index], arr[end]
    pivot = arr[end]
    #position fot pivot after loop
    mid = str

    for i in range(str, end):
        #If element is smaller than pivot, change position
        if arr[i] <= pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1

    #move pivot postion to mid
    arr[mid], arr[end] = arr[end], arr[mid]

    #recursively apply quick sort to the left and right sub-arrays
    randomized_quick_sort(arr, str, mid-1)
    randomized_quick_sort(arr, mid+1, end)

#tail-recursive quick sort
def tail_resusive_quick_sort(arr, str, end):
    if end-str+1 < 2:
        return

    while str < end:
        #choose a pivot element: typically the last element in the array
        pivot = arr[end]
        #position fot pivot after loop
        mid = str

        for i in range(str, end):
            #If element is smaller than pivot, change position
            if arr[i] <= pivot:
                arr[mid], arr[i] = arr[i], arr[mid]
                mid += 1

        #move pivot postion to mid
        arr[mid], arr[end] = arr[end], arr[mid]

        #called recursively in smaller parts based on mid
        if mid - str < end - mid:
            tail_resusive_quick_sort(arr, str, mid-1)
            #once a small part has been processed, run it again based on the remaining part
            str = mid+1
        else: 
            tail_resusive_quick_sort(arr, mid+1, end)
            #once a small part has been processed, run it again based on the remaining part
            end = mid-1

#open file
input = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

length = int(input.readline())
arr_naive = list(map(int, input.readline().split(' ')))
arr_random = arr_naive.copy()
arr_tail = arr_naive.copy()

#run sort
naive_quick_sort(arr_naive, 0, length-1)
randomized_quick_sort(arr_random, 0, length-1)
tail_resusive_quick_sort(arr_tail, 0, length-1)

#write file
output.write(' '.join(list(map(str, arr_naive))) + '\n')
output.write(' '.join(list(map(str, arr_random))) + '\n')
output.write(' '.join(list(map(str, arr_tail))) + '\n')

#close file
input.close()
output.close()
