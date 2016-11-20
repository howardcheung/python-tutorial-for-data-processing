# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 14:17:06 2016

@author: Howard
"""

import hello_world

print(hello_world.add_and_sub(1, 2, 3))
print(hello_world.prod_and_div(1, 2, 3))

from hello_world import add_and_sub

print(add_and_sub(1, 2, 3))
print(prod_and_div(1, 2, 3))