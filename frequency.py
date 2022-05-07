ishu="MISSISSIPPI"
k={}
for i in range(len(ishu)):
    coun=0
    for j in range(len(ishu)):
        if ishu[i]==ishu[j]:
            coun=coun+1
    k.update({ishu[i]:coun})
print(k)


# i=0
# cout=0
# while i<len(ishu):
#     cout=cout+i
#     print(i)
# i=i+12


