# my_dict = {'x':500, 'y':5874, 'z': 560}

# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])



dictionary = {"a": 5, "b": 2, "c": 8}
 
# get key with min value
# min_key = min(dictionary, key=dictionary.get)
 
# print(min_key)
# print output => "b"
 
# print(dictionary.get(min_key))
# min value
b=0
for i in dictionary:
    if dictionary[i]>b:
        b=dictionary[i]
print(b)
