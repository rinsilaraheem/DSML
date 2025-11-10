list1=[]
list2=[]

limit1=int(input("Enter the first limit : "))
for x in range(limit1):
    a=int(input("Enter element : "))
    list1.append(a)

limit2=int(input("Enter the second limit : "))
for x in range(limit2):
    a=int(input("Enter element : "))
    list2.append(a)


for x in list1:
    for y in list2:
        if x==y:
            print("True")