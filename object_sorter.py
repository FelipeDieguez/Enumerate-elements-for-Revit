import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

coord = IN[0]

OUT = sorted(coord, key=lambda k: [-k["y"],k["x"]])