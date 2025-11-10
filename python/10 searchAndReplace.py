f1 = open("t1.txt", "r")
content = f1.readlines()
f1.close()

old = input("Enter old word to replace: ")
new = input("Enter new word: ")

found = False
for i in range(len(content)):
    if old in content[i]:
        found = True
        content[i] = content[i].replace(old, new)

if found:
    f2 = open("file.txt", "w")
    f2.writelines(content)
    f2.close()

    f3 = open("file.txt", "r")
    print(f3.read())
    f3.close()
else:
    print("The word was not found.")
