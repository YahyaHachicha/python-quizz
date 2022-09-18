if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    # find the maximum
    maxi = arr[0]
    for e in arr:
        if e>maxi:
            maxi=e
    # select an element different from the maximum
    j=0
    while j<n and arr[j]==maxi:
        j+=1
    sec = arr[j]
    # find the second maximum
    for i in arr:
        if i>sec and i<maxi:
            sec=i
    print(sec)
