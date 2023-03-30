print("Demonstration on List Data Type")

# Data : haterogeneous
# Ordered : yes
# Indexed : yes
# Mutable : yes
# Duplicates : yes

data = [11,21,51,101,21,11]
data1 = [11,90.8,True,"Hello"] # Haterogeneous

print("data at index 2:",data[2])
print("data is ordered:",data1)
print("data at index 2:",data1[2])
print("Data with duplicate elements :",data)

print("List is mutable")

data.append(201)
print("data after append :",data)

data.pop()
print("data after pop :",data)
