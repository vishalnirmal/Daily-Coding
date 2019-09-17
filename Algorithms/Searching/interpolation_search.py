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


if __name__ == "__main__":
    from random import randint as r
    n = 1000
    # arr = [r(10000, 11000) for i in range(n)]
    arr = [r(1000, 2000) for i in range(n)]
    arr.sort()
    data = r(1000, 2000)
    print(data)
    print(search(arr, data))