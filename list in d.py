# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# k={}
# i=0
# while i<len(list1):
#     k.update({list1[i]:list2[i]})
#     i=i+1
# print(k)



# ishu={'one':2,'three':3,'four':6,'five':4} #key value
# for i in ishu.items():
#     print(ishu)

# ishu={'one':2,'three':3,'four':6,'five':4} #value
# for i in ishu:
#     print(ishu[i])

# ishu={'one':2,'three':3,'four':6,'five':4} #key
# for i in ishu:
#     print(i)

# ishu={'one':2,'three':3,'four':6,'five':4} #do sum
# sum=0
# for i in ishu:
#    sum=sum+(ishu[i])
# print(sum)

# ishu={'one':2,'six':3,'six':6,'five':4} # change value
# for i in ishu:
# #    ishu["three"]=4
#     print(ishu)
#     break

# ishu={'one':2,'six':3,'six':6,'five':4}# whithout using update fenction updating
# for i in ishu:
#     ishu['six']=3
# print(ishu)

# num=int(input("enter the no"))
# i=1
# k={}
# while i<=num:
#     k.update({i:i*i})
#     i=i+1
# print(k)

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# k={}
# for i in range(len(list1)):
#     k.update({list1[i]:list2[i]})
# print(k)


"Interview Questions"
        
# a={'add':{'a':5,
# 'b':3,
# 'c':4,
# 'd':6}
# }
# key=input("Enter key: ")
# value=int(input("Enter value: "))
# for i,j in a.items():
#     for k in j:
#         if k==key:
#             j[k]+=value
# print(a)




# a={'a':5,'b':3,'c':4,'d':6}
# key=input("Enter key: ")
# Value=int(input("Enter value: "))
# for i in a:
#        if i==key:
#             a[i]=a[i]+Value
# print(a)



# count=0
# b={}
# for i in(a):
#     k=input("enter the key")
#     v=input("enter the value")
#     b.update({k:v})
# print(b)



# a={'a':5,'b':3,'c':4,'d':6}
# b={}
# key=input("Enter key")
# value=input("enter the value")
# if a in key:
#     del(key)
#     if a not in key:
#          b.update(key+value)
# print(b)

a=int(input("enter the no"))
for i in a:
     print(i*i)
print(i)

