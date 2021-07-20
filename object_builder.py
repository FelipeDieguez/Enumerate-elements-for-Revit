import re
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

points = IN[0]
uid = IN[1]

results = []

for index, point in enumerate(points):
	id = uid[index]
	
	x, y, z = re.sub(r'Point\(X = (.*), Y = (.*), Z = (.*)\)', r'\1,\2,\3', point).split(',')
	
	results.append({
		"id": id,
		"x": float(x),
		"y": float(y),
	})

OUT = results