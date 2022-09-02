# printing prime numbers between 1 - 200 usng for and range

for i in range(1,201):
    if i > 1:
        for num in range(2,i):
            if(i%num==0):
                break
        else:
            print(i)
    

