"""
Global settings.
"""
from __future__ import division, print_function
import os

__all__ = [
    'computeNormals',
    'interactorStyle',
    'allowInteraction',
    'usingQt',
    'renderPointsAsSpheres',
    'textures',
    'textures_path',
    'datadir',
]

# recompute vertex and cell normals
computeNormals = None

# default style is TrackBallCamera
interactorStyle = None

# allow to interact with scene during interactor.Start() execution
allowInteraction = True

# usetex, matplotlib latex compiler
usetex = False

# Qt embedding
usingQt = False

# on some vtk versions/platforms points are redered as ugly squares
renderPointsAsSpheres = True

# path to Voro++ library
# http://math.lbl.gov/voro++
voro_path = '/usr/local/bin'

# axes titles
xtitle = 'x'
ytitle = 'y'
ztitle = 'z'



#####################
_cdir = os.path.dirname(__file__)
if _cdir == "":
    _cdir = "."
textures_path = _cdir + "/textures/"
textures = []

datadir = _cdir + "/data/"

#####################
collectable_actors = []


#####################
def _init():
    global plotter_instance, plotter_instances, collectable_actors
    global textures

    plotter_instance = None
    plotter_instances = []
    collectable_actors = []

    for f in os.listdir(textures_path):
        textures.append(f.split(".")[0])
    textures.remove("earth")
    textures = list(sorted(textures))

    import warnings
    warnings.simplefilter(action="ignore", category=FutureWarning)



