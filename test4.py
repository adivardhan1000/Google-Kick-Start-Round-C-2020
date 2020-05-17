import math 
  
def isPerfectSquare(x): 
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0) 

for i  in range(int(input())):
    number = int(input())
    cases = list(map(int,input().split()))
    count = 0
    while len(cases) != 0:
        #print('popped')
        for j in range(0,len(cases)):
            temp = cases[0:j+1]
            print(temp)
            if sum(temp)>0:
                if (isPerfectSquare(sum(temp))):
                    count = count + 1
                print('count',count)
        cases.pop(0)
    print('Case #'+str(i+1)+':',count)