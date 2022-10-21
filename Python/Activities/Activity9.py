list1= [1,2,3,4,5,6]
list2= [7,8,9,10,11]
newlist= []
for i in range(0,5):
    if (list1[i]%2)!=0:
        newlist.append(list1[i])
    if (list2[i]%2)==0:
        newlist.append(list2[i])
print(newlist)

"""also another code

list1= [1,2,3,4,5,6]
list2= [7,8,9,10,11]
newlist= []
for i in list1:
    if (i%2)!=0:
        newlist.append(i)
for k in list2:
    if (k%2)==0:
        newlist.append(k)
print(newlist)"""