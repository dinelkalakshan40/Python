#In Python, a list is a built-in data type that stores an ordered collection of elements,
# which can be of any type (e.g., integers, strings, objects).

my_list =["Dinelka",12,122,23,False]
print(my_list)
print(type(my_list))

#Acess elements
####### my_list =["Dinelka",12,122.23,False]
####### index=====>     0    1    2    3
####### NegativeIndex  -4   -3   -2    -1

my_list2 =["Kamal",20,False ,32323.23,50]

print("my_list2[0] :", my_list2[0])
print("my_list2[-1] :", my_list2[-1])
print("my_list2[-4] :", my_list2[-4])

print()

print("my_list2[2:4] :",my_list2[2:4])
print("my_list2[2:] :",my_list2[2:])
print("my_list2[:2] :",my_list2[:2])
print("my_list2[2:3] :",my_list2[2:3])

#Changing Elements:
my_list2 =["Kamal",20,False ,32323.23,50]
my_list2[2]=30
print(my_list2)

#Add values
my_list2.append("Lakshan") # add only one values in the end
print(my_list2)

my_list2.extend(["saman","kdc"]) #Add mutiple values
print(my_list2)

#Add value specific index
# my_list2.insert(0,"hello")
# print(my_list2)

my_list2.insert(2,"hello")
print(my_list2)

print()

#Remove elements
my_list3 =["my",343,True,50.45]
print(my_list3)

# my_list3.pop()
# print(my_list3)
#
# my_list3.pop(1)
# print(my_list3)

my_list3.remove(True)
print(my_list3)

my_list3.remove(343)
print(my_list3)

print(len(my_list3))
print(my_list3.index("my"))
