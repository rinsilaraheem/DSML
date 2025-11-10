limit=int(input("Enter the limit : "))
listt=[]
for x in range(limit):
    key=input("key : ")
    value=input("value : ")
    listt.append((key,value))

tup=tuple(listt)
dict=dict(tup)
print(dict)

