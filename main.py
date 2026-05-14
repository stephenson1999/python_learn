s = input("Enter a string: ")
words = 0

for i in range(len(s)):
    if s[i] == " ":
        words += 1

words += 1
print(words)


