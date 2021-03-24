#task 1
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/Scarlett/Desktop")
covid_data = pd.read_csv ("full_data.csv")

#task 2
print(covid_data.iloc[0:11:2, :])

#task 3
Afghanistan_total_cases = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'Afghanistan':
        Afghanistan_total_cases.append(covid_data.iloc[i, 5])
print(Afghanistan_total_cases)

#task 4
world_new_cases = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_new_cases.append(covid_data.iloc[i, 2])
print(world_new_cases)
import numpy as np
print(np.mean(world_new_cases))
print(np.median(world_new_cases))

#task 5
world_new_cases = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_new_cases.append(covid_data.iloc[i, 2])
print(world_new_cases)
import numpy as np
import matplotlib.pyplot as plt
plt.title('New cases worldwide')
plt.boxplot(world_new_cases,
            showbox= True,
            widths=0.15,
            meanline= True)
plt.show()

#task 6
world_dates = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_dates.append(covid_data.iloc[i, 0])
print(world_dates)

world_new_cases = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_new_cases.append(covid_data.iloc[i, 2])
print(world_new_cases)

world_new_deaths = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == 'World':
        world_new_deaths.append(covid_data.iloc[i, 3])
print(world_new_deaths)

import numpy as np
import matplotlib.pyplot as plt
plt.plot(world_dates, world_new_cases, 'r+',label = "new cases")
plt.plot(world_dates, world_new_deaths, 'b+', label = "new deaths")
plt.title('World new cases and new deaths')
plt.xticks(world_dates[0:len(world_dates):4], rotation= -90)
plt.xlabel('The dates')
plt.ylabel('number')
plt.legend()
plt.show()

#task 7
#choose all the total cases per day from South Korea
South_Korea_total = []
for i in range (0,7996):
    if covid_data.loc[i, 'location'] == "South Korea":
        South_Korea_total.append(covid_data.iloc[i,4])
print(South_Korea_total)

#choose all the total cases per day from Japan
Japan_total = []
for i in range(0,7996):
    if covid_data.loc[i,'location'] == "Japan":
        Japan_total.append(covid_data.iloc[i,4])
print(Japan_total)

#choose all the total cases per day from China
China_total= []
for i in range(0,7996):
    if covid_data.loc[i,'location'] == "China":
        China_total.append(covid_data.iloc[i,4])
print(China_total)

# draw a plot
import matplotlib.pyplot as plt
plt.title('Total cases in three different countries over time')
plt.xlabel("The dates")
#make a plot of South Korea
plt.plot(world_dates, South_Korea_total,"r+", label = 'total cases in South Korea')
#make a plot of Japan
plt.plot(world_dates, Japan_total, "g+", label = 'total cases in Japan')
#make a plot of China
plt.plot(world_dates, China_total, "b+", label = 'total cases in China')
#modify x axis so that x axis will not so crowded
plt.xticks(range(0,92,7))
#change the angle to make the date more clear
plt.xticks(rotation = 70)
#show the legend
plt.legend()
#show the whole chart consisting of three plots from three countries
plt.show()