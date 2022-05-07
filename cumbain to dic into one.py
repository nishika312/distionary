#write a Python program to combine two dictionary adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
b={}
for i in d2:
    if i in d1:
        d1[i]=d1[i]+d2[i]
        b.update(d1)
    else:
        d1[i]=d2[i]
print(b)

    