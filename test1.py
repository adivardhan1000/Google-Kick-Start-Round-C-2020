'''for i in range(int(input())):
    total_elements, size_countdown = map(int,input().split())
    cases = list(map(int,input().split()))
    count = 0
    j = 0
    if size_countdown > 2:
        while j != total_elements-size_countdown-1:
            if j + size_countdown <= total_elements-1:
                print('j',j)
                #print('j',j)
                temp = 0
                for k in range(size_countdown-1):
                #print('inside',k)
                    if cases[j+k] - cases[j+k+1] != 1:
                        break
                    else:
                        temp = temp + 1
                        print('temp',temp)
                    if temp == size_countdown-1:
                        count = count + 1
                        #print('j',j)
                        j = j+k-1
                                    if j+k < total_elements:
                                        next = 1
                                    else:
                                        next = 0
                j=j+1
            else:
                break
    else:
        count = 0
    print('Case #'+str(i+1)+':',count)
'''
for i in range(int(input())):
    total_elements, size_countdown = map(int,input().split())
    cases = list(map(int,input().split()))
    count = 0
    j = 0
    if size_countdown > 2:
        while j != total_elements-size_countdown+1:
            next = 1
            #print('j',j)
            for k in range(size_countdown-1):
            # print('inside',k)
                if  cases[j+k] - cases[j+k+1] == 1:
                    #print('inside if at j =',j)
                    next = 1
                else:
                    break
                if k == size_countdown-2:
                    count = count + 1
                    #print('j',j)
                    if j+k < total_elements:
                        j = j+k-1
                        next = 1
            if next == 1:
                j = j + 1
            else:
                break
    else:
        count = 0
    print('Case #'+str(i+1)+':',count)