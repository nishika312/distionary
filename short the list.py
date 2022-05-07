ishu=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, 
{"six":"9"},{"seven":"7"}]
a=[]
for i in range(len(ishu)):
    for j in ishu[i]:
        if ishu[i][j] not in a:
            a.append(ishu[i][j])
print(a)

# x=dict(name='sweety',age=36)
# print(x)