#1
def reverse_num(num):
    if (num>0):
      last = num%10
      if (num//10>0):
         current_number = reverse_num((int)(num//10))
         return last*pow(10, len(str(current_number)))+current_number
      else:
         return last
    else:
       return 0
    
num = int(input("Enter a number: "))
print("Reverse num : ", reverse_num(num))


#2
def reverse_str(s):
   if len(s) == 1:
      return s[0]
   
   fist_char = s[0]
   return(reverse_str(s[1:])) + fist_char

s = str(input("Enter a string: "))
print("Reversed string: ", reverse_str(s))


#3
def powerof4(number):
   count = 0
   if number==0:
      return 0 
   while num > 1:
      number>>=1
      count+=1
   if count%2==0:
      return 1
   else: 
      return 0
   

number = int(input("What is the number?: "))
if powerof4(number):
   print("yes")
   print("It is a power of four.")
else:
   print("No it is not a power of four.")    