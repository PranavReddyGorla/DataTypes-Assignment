A = [1,2,3,4,3] # lista
B = [1,4,5,6,7,2] #listb
print(set(A))
print(set(B))
print(set(A).intersection(set(B))) #prints the elements present both in A and B
A = [2,7,6,5,4,1,3]
B = [1,4,5,6,7,2]
print(set(A).intersection(set(B))) #prints the elements present both in A and B
print(set(A).difference(set(B))) #prints the elements which are not present in set B
C = (5,4)*10
print(C)
C[1] = 3 #tuples are immutable you cannot change after creation
print(C)
