# make a new directionary
my_dict = {}
# input some keys and values
countries = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}

# calculate the frequency of these statistics
import numpy as np
# extract the keys from the countries dictionary
a,b,c,d,e = countries.keys()
# extract the values from the dictionary
A,B,C,D,E = countries.values()
# calculate the total cases of five countries
x = A+B+C+D+E
# turn the values and the total cases into two arrays
m = np.array([A,B,C,D,E])
n = np.array([x,x,x,x,x])
# divide the m array by the n array correspondingly to calculate the frequency
frequency = np.true_divide(m,n)
# turn the keys into a new array
Countries = np.array([a,b,c,d,e])
# match the frequency to corresponding countries
s = dict(zip(Countries,frequency))
print(s)





# use matplotlib to draw a statistical chart
import matplotlib.pyplot as plt
# make a list of countries
labels = countries.keys()
# input the total cases of each country
sizes =  countries.values()
# show the distance each part away from the center of the circle
explode = (0, 0.1, 0, 0,0)
# give the pie chart a title
plt.title("The total number of cases for USA, India, Brazil and Russia")
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# ensure that the chart is a circle
plt.axis('equal')
plt.show()