import sys
import random

#naive quick sort
def quick_sort_naive(arr):
    if len(arr) <= 1:
        return arr
    
    #choose a pivot element (typically the last element in the array)
    pivot = arr[-1]

    #partition the array into three parts
    ##elements less than the pivot
    left = [x for x in arr[:-1] if x < pivot]

    ##elements equal to the pivot
    middle = [x for x in arr if x == pivot]

    ##elements greater than the pivot
    right = [x for x in arr[:-1] if x > pivot]
    
    #recursively apply quick sort to the left and right sub-arrays
    return quick_sort_naive(left) + middle + quick_sort_naive(right)

#ramdomized quick sort
def quick_sort_randomized(arr):
    if len(arr) <= 1:
        return arr
    
    #choose a pivot element randomly from the array.
    pivot = random.choice(arr) 

    #partition the array into three parts
    ##elements less than the pivot
    left = [x for x in arr if x < pivot]

    ##elements equal to the pivot
    middle = [x for x in arr if x == pivot]

    ##elements greater than the pivot
    right = [x for x in arr if x > pivot]

    #recursively apply quick sort to the left and right sub-arrays
    return quick_sort_randomized(left) + middle + quick_sort_randomized(right)

#tail-recursive quick sort
def quick_sort_tail_recursive(arr):
    def _quick_sort(arr, low, high):
        if low < high:
            #choose a pivot element (typically the first element in the array)
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
            
            #recursively apply quick sort to the smaller partition first
            _quick_sort(arr, low, right - 1)
            #use tail call optimization to sort the larger partition without accumulating call stack
            _quick_sort(arr, right + 1, high)
        
        return arr

    return _quick_sort(arr, 0, len(arr) - 1)

#open file
input = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

length = int(input.readline())
arr_naive = list(map(int, input.readline().split(' ')))
arr_random = arr_naive.copy()
arr_tail = arr_naive.copy()

#run sort
arr_naive = quick_sort_naive(arr_naive)
arr_random = quick_sort_randomized(arr_random)
arr_tail = quick_sort_tail_recursive(arr_tail)

#write file
output.write(' '.join(list(map(str, arr_naive))) + '\n')
output.write(' '.join(list(map(str, arr_random))) + '\n')
output.write(' '.join(list(map(str, arr_tail))) + '\n')

#close file
input.close()
output.close()
