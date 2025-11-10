f1=open("t1.txt","r")
f2=open("t2.txt","a")
a=f1.readlines()
for i in a:
    f2.writelines(i)

f2.close()
f1.close()
f2=open("t2.txt","r")
print("Second file : \n"+f2.read())
f2.close()