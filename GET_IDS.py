import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

nodes = IN[0]

results = []
for node in nodes:
	results.append(node["id"])

OUT = results