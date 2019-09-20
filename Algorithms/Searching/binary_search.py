##############################################
# Binary Search                              #
# by Vishal Nirmal                           #
##############################################




def search(arr, data):

    low, high = 0, len(arr)-1

    while low<=high:

        mid = (low + high) // 2

        if arr[mid] > data:

            high = mid-1

        elif arr[mid] < data:

            low = mid+1

        else:

            return True

    return False