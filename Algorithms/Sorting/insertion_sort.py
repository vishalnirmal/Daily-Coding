def sort(arr, reverse=False):
    for i in range(1, len(arr)):
        value = arr[i]
        j = i
        if reverse:
            while arr[j-1] < value and j > 0:
                arr[j] = arr[j-1]
                j-=1
        else:
            while arr[j-1] > value and j > 0:
                arr[j] = arr[j-1]
                j-=1
        arr[j] = value


if __name__ == "__main__":
    from random import randint as r
    n = r(10, 15)
    arr = [r(100, 200) for i in range(n)]
    print(arr)
    sort(arr)
    print(arr) 