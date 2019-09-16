def count_sort(arr, div, reverse):
    count = list([0]*10)
    n = len(arr)
    output = list([0]*n)
    for i in arr:
        count[(i//div)%10]+=1
    low, high, step, inc = (8, -1, -1, 1) if reverse else (1, 10, 1, -1)
    for i in range(low, high, step):
        count[i] += count[i+inc]
    i = n-1
    while i>=0:
        index = (arr[i]//div)%10 
        output[ count[index] - 1] = arr[i] 
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
def sort(arr, reverse=False):
    mx = max(arr)
    div = 1
    while mx/div > 0:
        count_sort(arr, div, reverse)
        div*=10

if __name__ == "__main__":
    from random import randint as r
    n = r(20, 30)
    print(n)
    arr = [r(100, 200) for i in range(n)]
    print(arr)
    sort(arr, reverse=False)
    print(arr)  
    
