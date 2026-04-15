name=input("Enter a name: ")
for i in range(len(name)):
    for j in range(i+1):
        print((name[j]),end=" ")
    print()
