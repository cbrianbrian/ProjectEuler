'''
Problem: Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
Answer: 5537376230

-cbrianbrian
'''
import numpy as np
import csv
import pandas as pd
from collections import defaultdict

a = []

#txt to csv
df = pd.read_fwf('num.txt')
df.to_csv('log.csv')


with open('log.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row[1])
    
int_a = []
for i in set(a):
    converted = int(i)
    int_a.append(converted)


sumnum = sum(int_a)
sumnum_str = str(sumnum)

print(sumnum_str[:10])
