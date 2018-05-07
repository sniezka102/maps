#!usr/bin/env python
# encoding: utf-8
#program do obliczania odleglosci pomiedzy dwoma punktami

import sys
import math

initPoint = [10,50]
endPoint = [30,120]

x1 = initPoint[0]
y1 = initPoint[1]
x2 = endPoint[0]
y2 = initPoint[1]

print(x1,x2)

basicCalculation = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("basicCalculation = ", basicCalculation)
