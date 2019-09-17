##############################################
# Interpolation Search                       #
# by Vishal Nirmal                           #
#                                            #
# An Interpolation Search algorithm.         #
##############################################




def search(arr, data):

    low, high = 0, len(arr)-1

    while low < high:

        mid = low + ((data - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if mid > high or mid < low:

            return False

        if data == arr[mid]:

            return True

        elif data < arr[mid]:

            high = mid - 1

        else:

            low = mid + 1

    return False