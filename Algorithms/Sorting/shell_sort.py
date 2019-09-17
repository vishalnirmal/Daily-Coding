##############################################
# Shell Sort                                 #
# by Vishal Nirmal                           #
##############################################




def sort(arr, reverse=False):

    n = len(arr)

    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            value = arr[i]

            j = i

            if reverse:

                while arr[j-gap] < value and j >= gap:

                    arr[j] = arr[j-gap]

                    j-=gap

            else:

                while arr[j-gap] > value and j>=gap:

                    arr[j] = arr[j-gap]

                    j-=gap

            arr[j] = value

        gap //= 2