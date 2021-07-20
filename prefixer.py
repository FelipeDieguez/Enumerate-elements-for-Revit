import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

nodes = IN[0]
prefix = IN[1]

results = []
counter = 0

def get_name(node):
	global counter
	for item in results:
		if node["x"] == item["x"] and node["y"] == item["y"]:
			return item["name"]
			
	counter = counter + 1
	return '{prefix}{counter}'.format(prefix=prefix, counter=counter)

for node in nodes:
	result = node.copy()
	result.update({
		"name": get_name(node)
	})
	results.append(result) 

OUT = results