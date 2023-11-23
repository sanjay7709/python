if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    a=max(l)
    c=l.count(a)
    for i in range(c):
        l.remove(a)
    print(max(l))
