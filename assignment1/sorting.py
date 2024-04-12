import sys

#insertion sort defined
def insertion_sort(arr):
    for i in range(1, len(arr)):
        #select key element
        key = arr[i]
        #shift element of arr[0..i-1] that are greater than key
        j = i-1
        #find index to insert the key
        while j >= 0 and arr[j] > key:
            #insert
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

#merge + insertion sort defined
##if merge sort, is_insertion_sort parameter is false
##if merge + insertion sort, is_insertion_sort parameter is true
def merge_insertion_sort(arr, is_insertion_sort):
    if len(arr) < 2 and not is_insertion_sort:
        return arr
    
    #if is_insertion_sort parameter is true, and sub array length is samller than 5 run insertion sort
    if len(arr) < 5 and is_insertion_sort:
        inserted_arr = arr.copy()
        insertion_sort(inserted_arr)
        #return insertion sort array
        return inserted_arr

    #find dividing point
    mid = len(arr) // 2
    #recursive execution based on dividing poiont
    front_arr = merge_insertion_sort(arr[:mid], is_insertion_sort)
    back_arr = merge_insertion_sort(arr[mid:], is_insertion_sort)

    #merge sequentially based on sorted sub array
    merged_arr = []
    f = b = 0
    while f < len(front_arr) and b < len(back_arr):
        if front_arr[f] < back_arr[b]:
            merged_arr.append(front_arr[f])
            f += 1
        else:
            merged_arr.append(back_arr[b])
            b += 1
    merged_arr += front_arr[f:]
    merged_arr += back_arr[b:]
    return merged_arr

#open file
input = open(sys.argv[1],"r")
output = open(sys.argv[2],"w")

length = int(input.readline())
arr_insertion = list(map(int, input.readline().split(' ')))
arr_merge = arr_insertion.copy()
arr_merge_insertion = arr_insertion.copy()

#run sort
insertion_sort(arr_insertion)
arr_merge = merge_insertion_sort(arr_merge, False)
arr_merge_insertion = merge_insertion_sort(arr_merge_insertion, True)

#write file
output.write(' '.join(list(map(str, arr_insertion))) + '\n')
output.write(' '.join(list(map(str, arr_merge))) + '\n')
output.write(' '.join(list(map(str, arr_merge_insertion))) + '\n')

#close file
input.close()
output.close()
