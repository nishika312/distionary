ishu = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20,'g':321,'h':521}
i=0
for i in ishu:
    if ishu[i]>a:
        a=ishu[i]
        b=0
        for j in ishu:
            if ishu[j]>b and ishu[j]!=a:
                b=ishu[j]
                c=0
                for k in ishu:
                    if ishu[k]>c and ishu[k]!=a and ishu[k]!=b:
                        c=ishu[k]
print(a,b,c)