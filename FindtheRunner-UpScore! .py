if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis= list(arr)
    lis.sort()


    max = lis[len(lis)-1]
    for r in reversed(lis):
     if r<max :
        runner=r
        break
    print(runner)