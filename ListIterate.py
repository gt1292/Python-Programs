
# Data : haterogeneous
# Ordered : yes
# Indexed : yes
# Mutable : yes
# Duplicates : yes

data = [11,21,51,101]

print("Output using for loop")
################################################
for no in data:
    print(no,end =" ")
print()
###############################################
print("Output using for loop with index")
for i in range(0,len(data)):
    print(data[i],end =" ")
print()
###############################################
print("Output using while loop with index")
i=0
while(i < len(data)):
    print(data[i],end=" ")
    i+=1
print()