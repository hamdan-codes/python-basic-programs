n = int(input("Enter size : "))
que = []
for i in range(n):
    que.append(0)

rear = 0

def insert():
    global rear
    if rear==n:
        print("Queue is full...")
    else:
        que[rear] = int(input("Enter Element to Insert : "))
        print(str(que[rear])+" inserted at "+str(rear))
        rear += 1

def delete():
    global rear
    if rear==0:
        print("Queue is empty...")
    else:
        print("Deleted Item : "+str(que[0]))
        for i in range(1, rear):
            que[i-1]=que[i]
        rear -= 1

def display():
    global rear
    if rear==0:
        print("Queue is empty...")
    else:
        print("Queue Elements :",end=" ")
        for i in range(rear):
            print(str(que[i]), end=" ")
        print("\n")




while True:
    print("1. Insert\n2. Delete\n3. Display\nAny other key to Quit")
    c = int(input("Enter choice : "))
    if c==1:
        insert()
    elif c==2:
        delete()
    elif c==3:
        display()
    else:
        break






