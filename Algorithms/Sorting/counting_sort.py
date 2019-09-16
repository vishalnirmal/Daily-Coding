def sort(arr, reverse=False):
    k = max(arr)+1
    count = list([0]*k)
    n = len(arr)
    output = list([0]*n)
    for i in arr:
        count[i]+=1
    low, high, step, inc = (k-2, -1, -1, 1) if reverse else (1, k, 1, -1)
    for i in range(low, high, step):
        count[i] += count[i+inc]
    i = n-1
    while i >= 0:
        index = arr[i]
        output[count[index]-1] = arr[i]
        count[index]-=1
        i-=1
    for i in range(n):
        arr[i] = output[i]
if __name__ == "__main__":
    from random import randint as r
    n = r(20, 30)
    print(n)
    arr = [r(100, 200) for i in range(n)]
    print(arr)
    sort(arr, reverse=False)
    print(arr)  
