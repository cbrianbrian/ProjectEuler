import roman
import numpy as np
import csv
import pandas as pd
from collections import defaultdict    
roman_map = {
    1: "I", 4: "IV", 5: "V", 9: "IX",
    10: "X", 40: "XL", 50: "L", 90: "XC",
    100: "C", 400: "CD", 500: "D",
    900: "CM", 1000: "M",
}

# INTEGER TO ROMAN NUMERAL    
def to_roman_numeral(value):
    result = ""
    remainder = value

    for i in sorted(roman_map.keys(), reverse=True):
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]

            times = remainder // multiplier         
            remainder = remainder % multiplier
            result += roman_digit * times           

    return result

def to_integer(value):
    tot = 0
    for item in sorted(roman_map.items(), reverse = True):
        for i in range(len(value)):
            if item[1] == value[i]:
                tot+=item[0]
    return tot

a = []

#txt to csv
df = pd.read_fwf('roman.txt')
df.to_csv('roman.csv')


with open('roman.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        a.append(row[1])
        
# GET NUMBER OF CHARACTERS IN LIST OF ROMANS
starting_roman_char = 0
for i in range(len(a)):
    starting_roman_char += len(a[i])
print(starting_roman_char)

# CONVERT LIST OF ROMANS TO INTEGERS AND BACK TO REDUCED ROMANS
romtoint = []
for i in range(len(a)):
    try:
        romtoint.append(roman.fromRoman(a[i]))
    except:
        romtoint.append(to_integer(a[i]))


inttorom = []
for i in range(len(romtoint)):
    inttorom.append(to_roman_numeral(romtoint[i]))

#GET NUMBER OF CHARACTERS IN NEW LIST OF ROMANS
end_roman_char = 0
for i in range(len(inttorom)):
    end_roman_char += len(inttorom[i])
print(end_roman_char)

print(starting_roman_char - end_roman_char)