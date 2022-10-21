L= list(input("Enter the list").split(","))
s=0
for a in range(0,len(L)):
    s= s + int(L[a])
print(s)