x = input("Enter a word +_+: ")
y = (list(x))
length = len(y)
length2 = length - 1
if y[0] == y[length2]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")