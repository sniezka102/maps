#!usr/bin/env python
# encoding: utf-8
#program do obliczania odleglosci pomiedzy dwoma punktami
#obliczenie odleglosci z uwzględnieniem długości 1stopnia
#na równiku jest to wartość 111km
#dla Polski ciężko określić ale przyjmuje się 73km

import sys
import math

initPoint = [10,50]
endPoint = [30,120]
numKmOneDegree = 73

x1 = initPoint[0]
y1 = initPoint[1]
x2 = endPoint[0]
y2 = initPoint[1]

basicCalculation = math.sqrt((x2-x1)**2 + (y2-y1)**2) * numKmOneDegree
print("basicCalculation = ", basicCalculation)
