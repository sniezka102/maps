#!usr/bin/env python
# encoding: utf-8
#program do obliczania odleglosci pomiedzy dwoma punktami
#obliczenie odleglosci z uwzglednieniem sferycznosci

import sys
import math

initPoint = [21.0122287,52.2296759]
endPoint = [16.9251681, 52.406374]
earthRadius = 6373.0 #km


lon1 = math.radians(initPoint[0])
lat1 = math.radians(initPoint[1])
lon2 = math.radians(endPoint[0])
lat2 = math.radians(initPoint[1])

dlon =lon2 - lon1 #dlugosc
dlat = lat2 - lat1 #szerokość

a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
baseCalc = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
destination = earthRadius * baseCalc

print("destination = ", round(destination,3)," km")
