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

if __name__ == "__main__":
    from random import randint as r
    n = 100000
    arr = [r(10000, 20000) for i in range(n)]
    arr.sort()
    print(search(arr, r(10000, 20000)))