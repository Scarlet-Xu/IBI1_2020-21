#Function: compute the sum of the first two numbers of the number
# f(1) = 1
# f(2) = 1
#repeat
#      f(n)= f(n-1) + f(n-2)
#      check if n = 13
#      if no: continue
#      if yes: done!


# assign the first one the value of 1
X = 1 
#output the number
print(X)
#assign the second one the value of 1
Y = 1
#output the number
print(Y)
# use a loop to describe fibonacci sequence
for i in range (3,14): 
    Z = X + Y
    X = Y
    Y = Z
#output the result
    print(Z)

