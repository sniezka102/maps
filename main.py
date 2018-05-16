import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("source", help="source file")
args = parser.parse_args()

BODY_FMT='<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document><name>{}</name><Style id="inline"><LineStyle><color>ff0880fd</color><width>4</width></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style><StyleMap id="inline2"><Pair><key>normal</key><styleUrl>#inline</styleUrl></Pair><Pair><key>highlight</key><styleUrl>#inline3</styleUrl></Pair></StyleMap><Style id="inline3"><LineStyle><color>ff0880fd</color><width>4</width></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style><Placemark><name>propozycja</name><styleUrl>#inline2</styleUrl><LineString><tessellate>1</tessellate><coordinates>{}</coordinates></LineString></Placemark></Document></kml>'

src = args.source
dst = os.path.splitext(args.source)[0] + ".kml"

with open(src) as file:
	data = file.read()

#check the file configuration, now ';' is not used, points are splited by new line separator

split = data.split(';')
name = split.pop(0)

coords = ''

for item in split:
	itemsplit = item.split(',')
	if len(itemsplit) == 3:
		coords = coords + itemsplit[2] + "," + itemsplit[1] + ",0,"

coords = coords[:-1]

with open(dst, "w") as file:
	file.write(BODY_FMT.format(name,coords))

