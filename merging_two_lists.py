arr1=list(map(int,input("enter elemnt for list 1:").split()))
arr2 = list(map(int,input("enter element for list 2:").split()))
arr = arr1 + arr2
# yaha set use kiya hai dubplicates hatane k liye and then list m convert so that sort function use kr sake
c = sorted(list(set(arr)))
#  chahte to sort function use kr sakte the like arr.sort()
# but mene sorted use kiya bcz usse original arr change ni hota new banaya hai c name ka
print(f"results = {c}")
