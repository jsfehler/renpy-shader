
import renpy

import utils
from controller import RenderController, RenderContext, ControllerContextStore
from rendering import Renderer2D, Renderer3D, SkinnedRenderer
from rigeditor import RigEditor
from skinnedplayer import TrackInfo, AnimationPlayer
from shadercode import *
from is_supported import config, log, isSupported


PROJECTION = "projection"

WORLD_MATRIX = "worldMatrix"
VIEW_MATRIX = "viewMatrix"
PROJ_MATRIX = "projMatrix"

TEX0 = "tex0"
TEX1 = "tex1"

MODE_2D = "2d"
MODE_3D = "3d"
MODE_SKINNED = "skinned"

ZERO_INFLUENCE = "zeroinfluence.png"


_controllerContextStore = ControllerContextStore()

_coreSetMode = None
_coreSetModeCounter = 0


def _wrapSetMode(*args):
    global _coreSetModeCounter
    _coreSetModeCounter += 1

    _coreSetMode(*args)


def getModeChangeCount():
    return _coreSetModeCounter

# TERRBILE HACK!
# Mode change can reset the OpenGL context, so we need to track the
# mode change count in order to know when we must free and reload
# any OpenGL resources.


def _setupRenpyHooks():
    global _coreSetMode
    if _coreSetMode:
        # Already hooked
        return

    _coreSetMode = renpy.display.interface.set_mode
    renpy.display.interface.set_mode = _wrapSetMode
