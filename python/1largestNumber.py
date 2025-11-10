number=[]
limit=int(input("Enter the limit : "))
for x in range(limit):
    a=int(input("Enter element : "))
    number.append(a)
print(max(number))