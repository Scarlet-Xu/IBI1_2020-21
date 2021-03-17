# make a new directionary
my_dict = {}
# input some keys and values
countries = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}


# use matplotlib to draw a statistical chart
import matplotlib.pyplot as plt
# make a list of countries
labels = 'USA','India','Brazil','Russia','UK'
# input the total cases of each country
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
# show the distance each part away from the center of the circle
explode = (0, 0.1, 0, 0,0)
# 
plt.pie(sizes,explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90)
# ensure that the chart is a circle
plt.axis('equal')
plt.show()