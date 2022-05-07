# ishu = {'a':50, 'b':58,'c': 56,'d':40,'e':100, 'f':20,'h':300,'y':500,'r':1000}
# a=0
# for i in ishu:
#     if ishu[i]>50:
#         print(i)










# a = {(1,2):1,(2,3):2}
# print(a[1,2])

# a = {'a':1,'b':2,'c':3}
# print (a['b']),(a[a])

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
#         addone('Apple')
#         addone('Banana')
#         addone('apple')
#         addone('Apple')
#         print(len(fruit))
#     print(fruit)



# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print(len(Details["Student"])) 



# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)


rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id1 = id(rec)
del rec

rec = {
    "Name" : "Python", 
    "Age":"20", 
    "Addr" : "NJ", 
    "Country" : "USA"
    }
id2 = id(rec)
print(id1 == id2)