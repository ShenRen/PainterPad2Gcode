'''OpenGL extension SUN.mesh_array

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SUN_mesh_array'
_DEPRECATED = False
GL_QUAD_MESH_SUN = constant.Constant( 'GL_QUAD_MESH_SUN', 0x8614 )
GL_TRIANGLE_MESH_SUN = constant.Constant( 'GL_TRIANGLE_MESH_SUN', 0x8615 )
glDrawMeshArraysSUN = platform.createExtensionFunction( 
'glDrawMeshArraysSUN',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(constants.GLenum,constants.GLint,constants.GLsizei,constants.GLsizei,),
doc='glDrawMeshArraysSUN(GLenum(mode), GLint(first), GLsizei(count), GLsizei(width)) -> None',
argNames=('mode','first','count','width',),
deprecated=_DEPRECATED,
)


def glInitMeshArraySUN():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
