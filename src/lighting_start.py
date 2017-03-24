import math3d

Reflectpos = math3d.VectorN((0,0,0))
camPos = math3d.VectorN((-4,3,0))
L = math3d.VectorN.normalized_copy(math3d.VectorN((5,3,0)))
inverseL = L*-1
N = math3d.VectorN.normalized_copy(math3d.VectorN((0,1,0)))
r = 2*(math3d.dot(N,L))*N-L
rvector = r - inverseL
V = math3d.VectorN.normalized_copy(camPos - Reflectpos)
vaddl = V + L
h = vaddl / math3d.VectorN.magnitude(vaddl)
newh = math3d.VectorN.normalized_copy(h)





















































































