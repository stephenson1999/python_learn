ar = [0 for _ in range(10)]
n = 10

# declaring front and rear and initializing both with -1
front = -1
rear = -1
#fun for Enqueue
def enqueue(item):
  #chk overflow
  global n
  global rear
  global front
  if rear==n-1:
    print("Overflow",end=' ')
    print('\n',end=" ")
    return
    #front and rear are -1
    #set front and rear as 0 , else increment

  else:
    if front==-1 and rear==-1:
      front=0
      rear=0
    else:
      rear+=1
    #insert element at rear
    ar[rear]=item
    print("Element Inserted")
#Func for dequeue
def dequeue():
  global n
  global rear
  global front
  # checking underflow condition
  if front==-1 and front>rear:
    print("Underflow",end=" ")
    return
  else:
    item=ar[front]
    #display deleted element
    print("Element is deleted from queue: ",end=" ")
    print(item,end=" ")
    print("\n",end=" ")
    #if front & rear reach till the end the initialize
    if rear==front:
      rear=-1
      front=-1
    else:
      front=front+1
      front+=1
#function to display all elements of queue
def display():
  global n
  global rear
  global front
  #chk whether queue is empty or not
  if front==-1:
    print("Queue is empty",end=" ")
    print("\n",end=" ")
    return
  #if queue is not empty
  #print ele from rear to front
  else:
    print("Elements are ", end=" ")
    i=front
    while i<=rear:
      print ([ar[i]],end=" ")
      print(" ",end=" ")
      i+=1
    print("\n",end=" ")
#function to display front ele of queue
def frontt():
  global n
  global rear
  global front
  # chking queue is empty or not
  if front==-1:
    print("Queue is empty",end=" ")
    print("\n",end=" ")
    return
  else:
    #if queue is not empty print front element
    print("Front element is ",end=" ")
    print(ar[front],end=" ")
    print("\n",end=" ")
ch=None
#displaying enqueue,dequeue,front
print("1.Inserting",end="")
print("\n",end=" ")
print("2.Deleting",end="")
print("\n",end=" ")
print("3.Front",end="")
print("\n",end=" ")
print("4.All elements",end="")
print("\n",end=" ")
print("5.EXIT",end="")
print("\n",end=" ")
condition=True

while condition:
  ch=int(input("enter choice"))
  if ch==1:
    item=int(input("Element to be inserted"))
    enqueue(item)
  elif ch==2:
    dequeue()
  elif ch==3:
    frontt()
  elif ch==4:
    display()
  elif ch==5:
    print("EXIT",end=" ")
    print("\n",end=" ")
  else:
    print("INVALID CHOICE",end=" ")
    print("\n",end=" ")
  condition=ch!=5