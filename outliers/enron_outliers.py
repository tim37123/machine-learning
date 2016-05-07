#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salary = []
bonus = []
biggest_bonus = 0
biggest_salary = 0
largest_bonus_location = 0
largest_salary_location = 0
i = 0
### your code below
for point in data:
	if biggest_bonus < point[1]:
		biggest_bonus = point[1]
		largest_bonus_location = i
	if biggest_salary < point[0]:
		biggest_salary = point[0]
		largest_salary_location = i
	salary.append(point[0])
	bonus.append(point[1])
	i = i + 1

for line in data_dict:
	sub_vals = data_dict[line]
	if sub_vals['salary'] >= 1000000:
		if sub_vals['bonus'] >= 5000000:
			print line, "SALARY: ", sub_vals['salary'], "BONUS: ", sub_vals['bonus']

salary = salary[:largest_salary_location] + salary[largest_salary_location+1:]
bonus = bonus[:largest_bonus_location] + bonus[largest_bonus_location+1:]
# matplotlib.pyplot.scatter( salary, bonus )
# matplotlib.pyplot.xlabel("salary")
# matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()