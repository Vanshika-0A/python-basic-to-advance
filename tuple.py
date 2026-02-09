t = tuple(map(int,input("Enter tuple elements: ").split()))
even = ()
odd = ()
for i in t:
    if(i%2==0):
        even = even+(i,)
    else:
        odd = odd+ (i,)
print(f"Even tuple:{even}")
print(f"odd tuple:{odd}")            

