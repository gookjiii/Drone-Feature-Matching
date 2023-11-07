from __future__ import print_function
import numpy as np
import math as m
import matplotlib.pyplot as plt

def Rx(theta):
    return np.matrix([[1, 0, 0],
                      [0, m.cos(theta), -m.sin(theta)],
                      [0, m.sin(theta), m.cos(theta)]])

def Ry(theta):
    return np.matrix([[m.cos(theta), 0, m.sin(theta)],
                      [0, 1, 0],
                      [-m.sin(theta), 0, m.cos(theta)]])

def Rz(theta):
    return np.matrix([[m.cos(theta), -m.sin(theta), 0],
                      [m.sin(theta), m.cos(theta), 0],
                      [0, 0, 1]])

def LinePlaneCollision(planeNormal, planePoint, rayDirection, rayPoint, epsilon=1e-6):

	ndotu = planeNormal.dot(rayDirection)
	if abs(ndotu) < epsilon:
		raise RuntimeError("no intersection or line is within plane")

	w = rayPoint - planePoint
	si = -planeNormal.dot(w) / ndotu
	Psi = w + si * rayDirection + planePoint
	return Psi

if __name__ == '__main__':
    height = float(input())
    angle = float(input())
    planeNormal = np.array([0,0,1])
    planePoint = np.array([0,0,-height])
    DFOV = 84
    HFOV = DFOV * m.sin(m.atan(4 / 3))
    VFOV = DFOV * m.sin(m.atan(3 / 4))
    print(HFOV, VFOV)
    Hor = height * m.tan(m.radians(HFOV/2))
    Ver = height * m.tan(m.radians(VFOV/2))
    print(Hor, Ver)
    PointO = np.array([0,0,0])
    PointA = np.squeeze(np.asarray(np.array([-Hor, Ver, -height]) * Ry(m.radians(angle))))
    PointB = np.squeeze(np.asarray(np.array([Hor, Ver, -height]) * Ry(m.radians(angle))))
    PointC = np.squeeze(np.asarray(np.array([Hor, -Ver, -height]) * Ry(m.radians(angle))))
    PointD = np.squeeze(np.asarray(np.array([-Hor, -Ver, -height]) * Ry(m.radians(angle))))
    OA = PointA - PointO
    OB = PointB - PointO
    OC = PointC - PointO
    OD = PointD - PointO
    IntersetA = LinePlaneCollision(planeNormal, planePoint, OA, PointA)
    IntersetB = LinePlaneCollision(planeNormal, planePoint, OB, PointB)
    IntersetC = LinePlaneCollision(planeNormal, planePoint, OC, PointC)
    IntersetD = LinePlaneCollision(planeNormal, planePoint, OD, PointD)

coord = [IntersetA, IntersetB, IntersetC, IntersetD]
coord.append(coord[0])

xs, ys, zs = zip(*coord)

plt.figure()
plt.plot(ys,xs,zs)
plt.show()