string = input("Enter a string: ")
words = []
# for i in range(len(string)):
words = string.split()
biggest = 0
smallest = 9999999999999999999999999999999999999999999999999999
for i in range(len(words)):
    if len(words[i]) > biggest:
        biggest = len(words[i])
    if len(words[i]) < smallest:
        smallest = len(words[i])

print(biggest)
print(smallest)

          

