A = {"mahesh" : 100, "mahesh" : 99 } #dictionary
print(A) #prints mahesh : 99 because we are overwriting the variable a
A["mahesh"] = 67 # the value of mahesh will be 67 as we are overwriting the variable value
A["Ramu"] = 100
print(A) #prints mahesh:67 and ramu : 100 we are adding and overwriting the values
B = {"Ramu" : 37, "Mahesh" : 25, "Sam" : 100}
A.update(B)
print(A) # =the output will be {'mahesh': 67, 'Ramu': 37, 'Mahesh': 25, 'Sam': 100} as we are updating the dicA with dicB
B.update(A) #the output will be {'Ramu': 37, 'Mahesh': 25, 'Sam': 100, 'mahesh': 67} as we are updating dicB with dicA
print(B)
