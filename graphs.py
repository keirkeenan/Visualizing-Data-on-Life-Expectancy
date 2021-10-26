import json
import matplotlib.pyplot as plt


'''
Creating Graph 1 - US Life Expectancy Over Time
    - Calling on a JSON file with with years (1900-2017) stored as keys
    - Age of life expectancy stored as values
'''

files = ['years_and_ages.json']
for file in files:
    with open(file, encoding='ascii') as f:       # json ALWAYS in ascii
        text = f.read()
        data = json.loads(text)
        data = {int(float(k)):int(float(v)) for k,v in data.items()}


# get the plot data
xs = data.keys()
ys = data.values()


# plot the data
fig, ax = plt.subplots()
ax.plot(xs, ys)
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Average Life Expectancy', fontweight='bold')
plt.legend()
plt.savefig('US_life_expectancy(1900-2017).jpg')
plt.show()


'''
Creating Graph 2 - Comparing Avg Life Expectancy of Different Countries in 2017
'''

import csv

file = open('countries_life_expectancy.csv')
r = csv.reader(file)
data = list(r)

countries = []
age = []

# countries
x1 = data[13948][0]
countries.append(x1)
x2 = data[2543][0]
countries.append(x2)
x3 = data[11195][0]
countries.append(x3)
    
# life expectancy
y1 = int(float(data[13948][3]))
age.append(y1)
y2 = int(float(data[2543][3]))
age.append(y2)
y3 = int(float(data[11195][3]))
age.append(y3)


# plot bar graph
plt.bar(countries, age, color = 'b', width = 0.72)
plt.xlabel('Country', fontweight='bold')
plt.ylabel('Average Life Expectancy', fontweight='bold')
plt.legend()
plt.savefig('life_expectancy_diff_countries.jpg')
plt.show()