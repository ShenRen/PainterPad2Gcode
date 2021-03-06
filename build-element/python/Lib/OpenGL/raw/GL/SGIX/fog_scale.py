'''OpenGL extension SGIX.fog_scale

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_fog_scale'
_DEPRECATED = False
GL_FOG_SCALE_SGIX = constant.Constant( 'GL_FOG_SCALE_SGIX', 0x81FC )
GL_FOG_SCALE_VALUE_SGIX = constant.Constant( 'GL_FOG_SCALE_VALUE_SGIX', 0x81FD )


def glInitFogScaleSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
