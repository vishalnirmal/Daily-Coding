##############################################
# Selection Sort                             #
# by Vishal Nirmal                           #
##############################################




def sort(arr, reverse=False):

    for i in range(len(arr)):

        pos = i

        for j in range(i, len(arr)):

            if reverse:

                if arr[j] > arr[pos]:

                    pos = j

            else:

                if arr[j] < arr[pos]:

                    pos = j

        arr[pos], arr[i] = arr[i], arr[pos]