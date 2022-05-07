ishu=  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']} 
count=0
for i in ishu:
   for j in range(len(ishu[i])):
      count+=1
print("Total count:",count)


