
Batches = {"PPA":18000,"LB":16700,"Python":16500,"Angular":15000}

print("Data of Dictionary :",Batches)

print("Data Traversal using for each")
for x in Batches:
    print(x)
    
print("Data Traversal using for loop")
for x in Batches:
    print(x,Batches[x])
    
keysbatches = Batches.keys()
print(type(keysbatches))
print(keysbatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)