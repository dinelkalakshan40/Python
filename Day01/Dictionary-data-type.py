my_dict = {
    'name':'kamal',
    'age':20,
    'float':24.343
}
print(my_dict)
print("my_dict :",my_dict)
print("my_dict :",type(my_dict))
print(my_dict['age'])
print("========================")
print("my_dict :",my_dict)

my_dict['name']="Lakshan"
print("my_dict :",my_dict)

my_dict['boolan']=False
print("my_dict :",my_dict)

print("=========================")

#remove values
del my_dict['age']
print(my_dict)

print(my_dict.pop('name'))
print(my_dict)

print(my_dict.clear())


