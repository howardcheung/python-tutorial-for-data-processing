#!/bin/usr/python3
"""
    Created for examples

    Author: Howard Cheung
    Date: 2016/11/19
"""

print('Classwork 1:')
print('Hello World!')


print('\nClasswork 2:')
txt_str = 'Hello World!'
for ind in range(len(txt_str)):
    if txt_str[ind] != ' ':
        print(txt_str[ind])
        
print('\nClasswork 4:')
from datetime import datetime, timedelta
datetime_list = [datetime(2015, 1, 1)+timedelta(ind) for ind in range(365)]
for item in datetime_list:
    print(item)
    # the code below is used to shorten the display on screen.
    # no need in the exercise
    if item > datetime(2015, 1, 5):
        break
