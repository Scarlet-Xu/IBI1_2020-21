#Function: compute the sum of the first two numbers of the number
# f(1) = 1
# f(2) = 1
#repeat
#      f(n)= f(n-1) + f(n-2)
#      check if n = 13
#      if no: continue
#      if yes: done!

X = 1 
print(X)
Y = 1
print(Y)
for i in range (3,14): 
    Z = X + Y
    X = Y
    Y = Z
    print(Z)

