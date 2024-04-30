A= [1,2,3,5]
A.insert(4, 5)#we will insert element 5 at index 4
print (A)
A[4] = 6 #we will change the elemnt 5 to 6 by indexing
print(A)
del A[-1] #delete the last element
print(A)
del A[:0]#it dosent delete any element
print(A)
A= [1,2,3,5, 10,20, 55,3]
print("Sum of items in A:",sum(A))#prints sum
print("MAX item in A:",max(A))#prints max
print("Min item in A:",min(A))#prints min
print("Avg item in A:",sum(A)/len(A))#prints avg

