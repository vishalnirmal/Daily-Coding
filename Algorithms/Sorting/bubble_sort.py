def sort(arr, reverse=False):
    for i in range(len(arr)):
        swap = 0
        for j in range(len(arr)-i-1):
            if reverse:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = 1
            else:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swap = 1
        if swap == 0:
            break


if __name__ == "__main__":
    from random import randint as r
    n = r(10, 15)
    arr = [r(100, 200) for i in range(n)]
    print(arr)
    sort(arr, reverse=True)
    print(arr) 