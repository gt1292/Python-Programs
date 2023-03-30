print("Demonstration on Set Data Type")

# Data : haterogeneous
# Ordered : no
# Indexed : no
# Mutable : yes
# Duplicates : no

data = {11,21,51,101,21,11}
data1 = {11,90.8,True,"Hello"} # Haterogeneous

print("First set data :",data)
print("Length of data:",len(data))
print("data is Hetrogeneous 2:",data)
print("data is unordered:",data1)
#print("data at index 2:",data1[2])
 
print("Set is mutable")
#insert element in set 
data.add(211)
print("Data after insertion :",data)

#Remove element 
data.remove(211)
print("Data after removal :",data)

data.discard(201)
print("Data after discard :",data)


print("Demonstration of Iterate Loop of Set")

print("Output using for loop")

for no in data:
    print(no,end =" ")
print()
