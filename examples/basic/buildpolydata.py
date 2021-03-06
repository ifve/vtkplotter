"""
Load a mesh, extract the vertex coordinates,
and build a new vtkPolyData object.
Faces (vertex connectivity) can be specified too.

(press p to increase point size)
"""
from vtkplotter import *


pts = load(datadir+"bunny.obj").subdivide(2).coordinates()

poly = buildPolyData(pts, faces=None)  # vtkPolyData made of just vertices

doc = Text(__doc__)

show(poly, doc)
