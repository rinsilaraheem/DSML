# str1={}
# str2={}
# limit1=int(input("Enter the first limit : "))
# for x in range(limit1):
#     key=input("Enter the key : ")
#     value=input("Enter the value : ")
#     str1[key]=value

# limit2=int(input("Enter the second limit : "))
# for x in range(limit2):
#     key=input("Enter the key : ")
#     value=input("Enter the value : ")
#     str2[key]=value
# str3=str1|str2
# print(str3)
items1 = input("Enter key-value pairs for first dictionary : ").split() 
items2 = input("Enter key-value pairs for second dictionary : ").split() 
dict1 = {items1[i]: items1[i+1] for i in range(0, len(items1), 2)}
dict2 = {items2[i]: items2[i+1] for i in range(0, len(items2), 2)} 
merged = dict1.copy()
merged.update(dict2) 
print("Merged dictionary:", merged)
