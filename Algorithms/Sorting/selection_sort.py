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
    
if __name__ == "__main__":
    from random import randint as r
    n = r(10, 15)
    arr = [r(100, 200) for i in range(n)]
    print(arr)
    sort(arr, reverse=True)
    print(arr) 