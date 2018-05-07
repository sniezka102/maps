#!usr/bin/env python
# encoding: utf-8
#program do obliczania odleglosci pomiedzy dwoma punktami
#obliczenie odleglosci z uwzglednieniem sferycznosci

import sys
import math

def distance(origin,destination):
#Parameters:
#origin: tuple of float (lat,long)
#	origin =(21.0122287,52.2296759)
#	destination =(16.9251681, 52.406374)
	earthRadius = 6373.0 #km

	lat1,lon1 = origin
	lat2, lon2 = destination
	lon1 = math.radians(lon1)
	lat1 = math.radians(lat1)
	lon2 = math.radians(lon2)
	lat2 = math.radians(lat2)

	dlon = lon2 - lon1 #dlugosc
	dlat = lat2 - lat1 #szerokość

	a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
	baseCalc = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	distance = earthRadius * baseCalc

	return round(distance,3)


#przyklad wywolania funkcji:
#calc = distance((52.2296759, 21.0122287), (52.406374, 16.9251681))

#print("distance = ", calc, " km")
