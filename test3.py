for i in range(int(input())):
    total_candies , request = map(int,input().split())
    candies = list(map(int,input().split()))
    sum1 = []
    for j in range(request):
        query = input().split()
        if query[0] == 'Q':
            temp = candies[int(query[1])-1:int(query[2])]
            #print(temp)
            temp_sum = 0
            for k in range(len(temp)):
                temp_sum = temp_sum + ((-1)**(k))*temp[k]*(k+1)
            sum1.append(temp_sum)
            #print(sum1)
        elif query[0] == 'U':
            candies[int(query[1])-1] = int(query[2])
            #print(candies)
    print(sum(sum1))
        