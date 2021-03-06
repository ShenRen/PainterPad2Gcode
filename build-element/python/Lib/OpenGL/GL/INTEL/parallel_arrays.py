'''OpenGL extension INTEL.parallel_arrays

This module customises the behaviour of the 
OpenGL.raw.GL.INTEL.parallel_arrays to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds the ability to format vertex arrays in a way that's 

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/INTEL/parallel_arrays.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INTEL.parallel_arrays import *
### END AUTOGENERATED SECTION