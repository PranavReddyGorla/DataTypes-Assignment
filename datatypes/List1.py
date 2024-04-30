List1 = ['CSE', 'IT', 'EEE', 'ECE','MECH']
List2 = List1 #elements in  both the lists will be same
List2.append('CIVIL') #It adds civil element to the list2
print ('List1 = ', List1) # prints List1 =  ['CSE', 'IT', 'EEE', 'ECE', 'MECH', 'CIVIL']
print ('List2 = ', List2) #prints List2 =  ['CSE', 'IT', 'EEE', 'ECE', 'MECH', 'CIVIL']
List2.extend('CIVIL') #It will extend the element civil to C I V I L
print ('List2 = ', List2) #prints List2 =  ['CSE', 'IT', 'EEE', 'ECE', 'MECH', 'CIVIL', 'C', 'I', 'V', 'I', 'L']
List1.sort() #sort the elments in ascending order
print(List1) #as the elements are same in both list1 and list2 it will sort and prints ['C', 'CIVIL', 'CSE', 'ECE', 'EEE', 'I', 'I', 'IT', 'L', 'MECH', 'V']
