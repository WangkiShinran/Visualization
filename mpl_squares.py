#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

input = range(1,1001)
squares = [x ** 2 for x in input]
print(squares)
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input,squares,c=squares,cmap=plt.cm.Blues,s=10)

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
ax.axis([0,1100,0,1100000])

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.savefig('squares_plot.png',bbox_inches='tight')
