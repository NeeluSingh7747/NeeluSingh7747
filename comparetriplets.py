def compareTriplets(a, b): 
    alice = 0
    bob = 0
    for i in range(len(a)):   
        if a[i]>b[i]:
            alice +=1
        elif a[i]<b[i]:
            bob += 1
        else:
            print("0")
    return [alice,bob]
        
    
a = [1,3,5]
b = [5,7,3]

compareTriplets(a, b)
    # Write your code here





















