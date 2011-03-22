# -*- coding: utf-8 -*-
# The following line must be present in the pytpm.pyx file.
# cimport _tpm_vec

POS = _tpm_vec.POS
VEL = _tpm_vec.VEL
CARTESIAN = _tpm_vec.CARTESIAN
SPHERICAL = _tpm_vec.SPHERICAL
POLAR = _tpm_vec.POLAR

cdef class V3(object):
    """Class that wraps _tpm_vec.V3; for use from Cython only."""
    cdef _tpm_vec.V3 _v3

    def __cinit__(self):
        self._v3.type = CARTESIAN
        self._v3.v[0] = 0.0
        self._v3.v[1] = 0.0
        self._v3.v[2] = 0.0

    def __init__(self, ctype=CARTESIAN, X=0.0, Y=0.0, Z=0.0):
        self._v3.type = ctype
        self._v3.v[0] = X
        self._v3.v[1] = Y
        self._v3.v[2] = Z

    cdef int getType(self):
        return self._v3.type

    cdef setType(self, int t):
        self._v3.type = t
    
    cdef setX(self, double X):
        self._v3.v[0] = X
        
    cdef setY(self, double Y):
        self._v3.v[1] = Y

    cdef setZ(self, double Z):
        self._v3.v[2] = Z

    cdef double getX(self):
        return self._v3.v[0]
        
    cdef double getY(self):
        return self._v3.v[1]

    cdef double getZ(self):
        return self._v3.v[2]

    cdef _tpm_vec.V3 getV3(self):
        return self._v3

    cdef setV3(self, _tpm_vec.V3 _v3):
        self._v3 = _v3


cdef class V3CP(V3):
    """A V3 Cartesian position vector."""
    # The following are read only.
    ctype = CARTESIAN
    vtype = POS
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        self.setType(self.ctype)

    def __getx(self):
        return self.getX()
    def __setx(self, x):
        self.setX(x)
    x = property(__getx, __setx, doc="X coordinate.")

    def __gety(self):
        return self.getY()
    def __sety(self, y):
        self.setY(y)
    y = property(__gety, __sety, doc="Y coordinate.")

    def __getz(self):
        return self.getZ()
    def __setz(self, z):
        self.setZ(z)
    z = property(__getz, __setz, doc="Z coordinate.")
