# arr = list(map(int, input("Enter elements: ").split()))
# if(len(arr)==0):
#     print("list is empty")
# else:
#     avg = sum(arr)/len(arr)
#     print(f"average is {avg}")          

#now creating list using loop also cal avg using loop
n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    x = int(input(f"Enter element {i+1}: "))
    arr.append(x)

total = 0
for i in range(n):
    total = total + arr[i]

avg = total / n

print("Average =", avg)
print("file updated")

