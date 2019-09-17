def search(arr, data):
    for i in arr:
        if i == data:
            return True
    return False

if __name__ == "__main__":
    from random import randint as r
    n = 100000
    arr = [r(10000, 100000) for i in range(n)]
    print(search(arr, r(10000, 100000)))