for i in range(int(input())):
    r,c = map(int,input().split())
    main = set(list(input()))
    next = 1
    cases = []
    for k in range(r-1):
        cases.append(set(input()))
    for k in range(r-1):
        if cases[k].issubset(main):
            next = 1
        else:
            next = 0
            break
    if next == 1:
        main = list(main)
        main.sort(reverse=True)
        output = ''.join(main)
        print('Case #'+str(i+1)+':',output)
    else:
        print('Case #'+str(i+1)+':',-1)