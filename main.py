from crash import *
import matplotlib.pyplot as plt
from numpy import *
import pylab as p
#import matplotlib.axes3d as p3
import mpl_toolkits.mplot3d.axes3d as p3
# from mayavi import mlab
from mpl_toolkits.mplot3d import Axes3D
import random

farsh = 1  # количество разбиений треангуляции
times = 3000  # количество шагов по времени
tau = 0.01  # шаг по времени
sigma = 0.5  # коэффициент устойчивости схемы

V = 12  # количество вершин в исходном икосаэдре
E = 30  # количество рёбер в исходном икосаэдре
F = 20  # количество граней в исходном икосаэдре

coefficient = 0.0  # коэффициент, необходимый для пересчёта и нахождения точек, лежащих в одном слое
square = 0.0  # площадь первоначальной поверхности
list_faces = []  # лист всех граней
Vertex = F * pow(2, 2 * farsh - 1) + 2
with open('icosahedron.txt') as icos:  # загружаем нумерацию вершин в икосаэдре
    lines = icos.readlines()

for line in lines:
    ns_vtx = line.rstrip('\n').split('\t')
    a = int(ns_vtx[0])
    b = int(ns_vtx[1])
    c = int(ns_vtx[2])
    list_faces.append(Faces(a, b, c))
grind_faces = grinding(list_faces, V, vdata, Vertex)
new_data = grind_faces.grindin()

# fig = plt.figure()
# ax = plt.axes(projection ='3d')
list_of_x = []
list_of_y = []
list_of_z = []
for data in new_data:
    list_of_x.append(data[0])
    list_of_y.append(data[1])
    list_of_z.append(data[2])
# ax.scatter3D (list_of_x, list_of_y, list_of_z)
fig = p.figure()
ax = p3.Axes3D(fig)
# ax.plot_wireframe(list_of_x, list_of_y,list_of_z )
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# p.show()

