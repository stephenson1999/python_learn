def iprice(barcode):

    l=[]

    for i in barcode:

        n=ord(i) #ordinal that returns a unicode

        print(n)

        if n//10: # if a num is > 9

            max=0

            while n>0:

                if n % 10>max:

                    max=n%10

                    print(max)

                    n=n//10

                    print(n)

                    l.append(max)

                    print(l)

                else:

                    l.append(n)

                    return sum(l)

barcode=input("Enter")

print(iprice(barcode))

