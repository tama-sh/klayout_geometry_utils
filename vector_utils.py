import pya
import numpy as np

def in_range(x, r):
    if isinstance(r, list):
        return any(map(lambda r_elt: in_range(x, r_elt), r))
    else:
        return (r[0] <= x) and (x <= r[1])

def det_mat(m):
    """
      m: pya.Matrix2d
      return: float
    """
    return (m.m11()*m.m22() - m.m12()*m.m21())

def dot_vec(p0, p1):
    """
      p0, p1: DPoint
    """
    return (p0.x*p1.x + p0.y*p1.y)

def norm_vec(p):
    """
      p: DPoint
    """
    return np.sqrt(p.x*p.x + p.y*p.y)
    
def unit_vec(p):
    """
      p: DPoint
    """
    return p/norm_vec(p)

def vec_angle(v0, v1):
    """
      v0, v1: pya.DPoint
      return: float
    """
    m = pya.Matrix2d.new(v0.x, v0.y, v1.x, v1.y)
    return np.arctan2(det_mat(m), dot_vec(v0,v1))

def rot_vec(v, angle):
    """
      v: pya.DPoint
      angle: float
      return: pya.DPoint
    """
    mat = pya.Matrix2d.new(np.cos(angle), -np.sin(angle),
                           np.sin(angle), np.cos(angle))
    return mat.trans(v)
