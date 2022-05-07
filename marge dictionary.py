dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# d={}
# d.update(dic1)
# d.update(dic2)
# d.update(dic3)
# print(d)





i=0
sum=0
while i<len(dic1):
    if dic1==dic2:
        sum=sum+{dic1[i]}
        pass
        dic1.update(dic2)
        dic1.update(dic3)
        i=i+1
print(dic1)


