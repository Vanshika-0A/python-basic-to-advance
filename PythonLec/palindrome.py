# s = input("give a word: ")
# rev = s[ : :-1] #for reversing
# if(s==rev):
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")   



# using loop now
s = input("Enter a string: ")
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
