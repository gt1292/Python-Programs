print("Demonstration on List Data Type")

# Data : haterogeneous
# Ordered : yes
# Indexed : yes
# Mutable : no
# Duplicates : yes
# Tuple cant't change or can't modify thats why it is immutable

data = (11,21,51,101,21,11) # herrogeneous
data1 = (11,90.8,True,"Hello") # Haterogeneous

print("data at index 2:",data[2])
print("data is ordered:",data1)
print("data at index 2:",data1[2])
print("Data with duplicate elements :",data)
print()
print("______________________________________")
print("Demonstration of Tupple itterate")

print("Output using for loop with index")
for i in range(0,len(data)):
    print(data[i],end =" ")
print()

print("______________________________________")

print("Output using while loop with index")
i=0
while(i < len(data)):
    print(data[i],end=" ")
    i+=1
print()