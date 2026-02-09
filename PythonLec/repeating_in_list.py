s = list(map(int,input("enter element of list: ").split()))
seen = set()
repeated = set()
for i in s:
    if i in seen:
        repeated.add(i)
    else :
        seen.add(i) 
print(f"repeated elements: {repeated}")