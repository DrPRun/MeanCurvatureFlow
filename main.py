import numpy as np
import random as rd
from faces import *
from coor_data import *
import math
import numpy as np
from scipy import sparse
from crash import *
from smeg_matrix import *
import numpy as np

farsh = 2 # количество разбиений треангуляции
times = 3000 # количество шагов по времени
tau = 0.01 # шаг по времени
sigma = 0.5 # коэффициент устойчивости схемы

V = 12 # количество вершин в исходном икосаэдре
E = 30 # количество рёбер в исходном икосаэдре
F = 20 # количество граней в исходном икосаэдре

coefficient = 0.0 # коэффициент, необходимый для пересчёта и нахождения точек, лежащих в одном слое
square = 0.0 # площадь первоначальной поверхности
list_faces = [] # лист всех граней
Vertex = F*pow(2, 2*farsh - 1) + 2
with open('icosahedron.txt') as icos: # загружаем нумерацию вершин в икосаэдре
    lines = icos.readlines()

for line in lines:
    ns_vtx = line.rstrip('\n').split('\t')
    a = int(ns_vtx[0])
    b = int(ns_vtx[1])
    c = int(ns_vtx[2])
    list_faces.append(Faces(a, b, c))
# print('hello')
# adj_max = adjacency_matrix(list_faces, V)
# print('adj_max')
