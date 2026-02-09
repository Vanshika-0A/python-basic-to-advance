l1 = list(map(int , input("enter element of lists: ").split()))
l2 = list(map(int, input("Enter element of lists: ").split()))
s1 = set(l1)
s2 = set(l2)
s3 = s1 & s2

common = list(s3)
if len(common)==0:
    print("The two list have nothing in common")
else:
    print(f"Common elements are: {common}")
