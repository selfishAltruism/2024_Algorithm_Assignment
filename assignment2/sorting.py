import sys
import random

#naive quick sort
def naive_quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    #choose a pivot element: typically the last element in the array
    pivot = arr[-1]
    mid = 0

    for i in range(0, len(arr)-1):
        if arr[i] <= pivot:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1

    #recursively apply quick sort to the left and right sub-arrays
    return naive_quick_sort(arr[:mid]) + [pivot] + naive_quick_sort(arr[mid:-1])

#ramdomized quick sort
def ramdomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #choose a pivot element randomly from the array.
    pivot = random.choice(arr) 

    #partition the array into three parts
    ##elements less than the pivot
    left = [x for x in arr if x < pivot]

    ##elements equal to the pivot
    mid = [x for x in arr if x == pivot]

    ##elements greater than the pivot
    right = [x for x in arr if x > pivot]

    #recursively apply quick sort to the left and right sub-arrays
    return ramdomized_quick_sort(left) + mid + ramdomized_quick_sort(right)


#tail-recursive quick sort
##sub tail-recursive quick sort
def sub_tail_resusive_quick_sort(arr, low, high):
    if low < high:

        #choose a pivot element: typically the first element in the array
        pivot = arr[low]
            
        #partition the array into elements less than and greater than the pivot
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left = left + 1
            while arr[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
            
        #tail-recursively apply quick sort to the smaller partition
        sub_tail_resusive_quick_sort(arr, low, right - 1)

        #tail-recursively apply quick sort to the larger partition
        sub_tail_resusive_quick_sort(arr, right + 1, high)
        
    return arr

##main tail-recursive quick sort
def tail_resusive_quick_sort(arr):
    #call sub tail-recursive quick sort 
    return sub_tail_resusive_quick_sort(arr, 0, len(arr) - 1)


#open file
input = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

length = int(input.readline())
arr_naive = list(map(int, input.readline().split(' ')))
arr_random = arr_naive.copy()
arr_tail = arr_naive.copy()

#run sort
arr_naive = naive_quick_sort(arr_naive)
arr_random = ramdomized_quick_sort(arr_random)
arr_tail = tail_resusive_quick_sort(arr_tail)

#write file
output.write(' '.join(list(map(str, arr_naive))) + '\n')
output.write(' '.join(list(map(str, arr_random))) + '\n')
output.write(' '.join(list(map(str, arr_tail))) + '\n')

#close file
input.close()
output.close()
