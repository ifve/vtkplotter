"""Load an existing vtkStructuredGrid and draw
the streamlines of the velocity field
"""
import vtk
from vtkplotter import *

######################## vtk
# Read the data and specify which scalars and vectors to read.
pl3d = vtk.vtkMultiBlockPLOT3DReader()
pl3d.SetXYZFileName(datadir+"combxyz.bin")
pl3d.SetQFileName(datadir+"combq.bin")
pl3d.SetScalarFunctionNumber(100)
pl3d.SetVectorFunctionNumber(202)
pl3d.Update()
# this vtkStructuredData already has a vector field:
domain = pl3d.GetOutput().GetBlock(0) 

######################## vtkplotter
comment = Text(__doc__, c='w')
box = Actor(domain, c=None, alpha=0.1)

probe= Grid(pos=[9,0,30], normal=[1,0,0], sx=5, sy=5, resx=6, resy=6)
probe.color('k')

stream = streamLines(domain, probe, direction='backwards')

show(stream, probe, box, comment, axes=8)
