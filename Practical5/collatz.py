# Function:describe r and the total number of infected students
#f(1) = 84
#repeat
#     f(n) = r * f(n-1)
#     if n <=  5
#      continue
#      if n > 5
       done!

#describe the given statistic
str(a) = 84
str(r) = 1.2
#use a loop to describe the process
for i in range (2,7)
#conduct the round
    b = a * r
#begin a new round with assigning the initial value
    a = b
#output the result
    print(r)
    print(b) 
