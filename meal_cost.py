import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip_percent1=(tip_percent/100)*meal_cost
    tax_percent1=(tax_percent/100)*meal_cost
    meal_cost1=meal_cost+tip_percent1+tax_percent1
    meal_cost2=round(meal_cost1)
     return meal_cost2

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
    
print(solve(meal_cost,tip_percent,tax_percent))
