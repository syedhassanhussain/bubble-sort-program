list=[5,2,7,8,4,56,25,34,16,78,87,90,101,100]
def Bubblesort(list):
    n=len(list)
    while True:
        swapcounter=0
        for i in range(1,n):
            if(list[i-1]>list[i]):
                list[i-1],list[i]=list[i],list[i-1]
                swapcounter+=1
        n=n-1
        if(swapcounter==0):
            return list
print(Bubblesort(list))            


