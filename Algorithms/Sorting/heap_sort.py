##############################################
# Heap Sort                                  #
# by Vishal Nirmal                           #
##############################################




def heapify(arr, n, index, reverse):

    left = 2*index+1

    right = 2*index+2

    pos = index

    if reverse:

        if left < n and arr[left] < arr[pos]:

            pos = left

        if right < n and arr[right] < arr[pos]:

            pos = right

    else:

        if left < n and arr[left] > arr[pos]:

            pos = left

        if right < n and arr[right] > arr[pos]:

            pos = right

    if pos != index:

        arr[pos], arr[index] = arr[index], arr[pos]

        heapify(arr, n, pos, reverse)

def sort(arr, reverse=False):

    n = len(arr)

    for i in range((n-1)//2, -1, -1):

        heapify(arr, n, i, reverse)

    

    for i in range(n-1, -1, -1):

        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0, reverse)