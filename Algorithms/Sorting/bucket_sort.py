##############################################
# Bucket Sort                                #
# by Vishal Nirmal                           #
##############################################




def sort(arr, reverse=False):

    k = max(arr)+1

    c = [0 for i in range(k)]

    b = []

    for i in arr:

        c[i] += 1

    low, high, step = (k-1, -1, -1) if reverse else (0, k, 1)

    i = 0

    for j in range(low, high, step):

        for k in range(c[j], 0, -1):

            arr[i] = j

            i+=1