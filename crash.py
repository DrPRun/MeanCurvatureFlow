from smeg_matrix import *
from faces import *
from coor_data import *
from faces import *
import numpy as np
from scipy import sparse


# adj_max = adjacency_matrix( list_faces, V, crash_vertex )

class grinding(object):
    def __init__(self, faces, vertex, vdata, crash_vertex):
        self.faces = faces
        self.vertex = vertex
        self.faces_new = []
        self.new_vdata = list(range(0, crash_vertex )) # лист для того, чтобы хранить новые координаты вершин
        self.vdata = vdata
        self.adj_mtx = adjacency_matrix(self.faces, self.vertex)  # получена матрица смежности, вместо 1, как в

    def grindin(self):
        self.adj_mtx = adjacency_matrix(self.faces, self.vertex)  # получена матрица смежности, вместо 1, как в
        # классическом варианте стоят ненулевые значения необходимо пройтись по всем элементам матрицы смежности и
        # каждому ненулевому элементу сопоставить конкретный номер вершины
        for i in range(0, self.vertex):
            for j in range(i, self.vertex):
                self.new_vdata[i] = vdata[i]
                self.new_vdata[j] = vdata[j]
                x_coord = (self.vdata[i][0] + self.vdata[j][0]) / 2.
                y_coord = (self.vdata[i][1] + self.vdata[j][1]) / 2.
                z_coord = (self.vdata[i][2] + self.vdata[j][2]) / 2.
                self.new_vdata[self.adj_mtx[i, j]] = crdvtx(x_coord, y_coord, z_coord)
                print(self.new_vdata[self.adj_mtx[i, j]][0], self.new_vdata[self.adj_mtx[i, j]][1], self.new_vdata[self.adj_mtx[i, j]][2], sep=',', end='\n')
        print("длина: ", len(self.new_vdata))
        # type(self.new_vdata)
        # countvertex = 0
        # for nw_dt in self.vdata:
        #     print(nw_dt[0], nw_dt[1], nw_dt[2], sep=';', end='\n')

        return self.new_vdata
        # number_of_vertex = 0
        # for cord in self.new_vdata:
        #     print(cord[0])
            # print(number_of_vertex,  cord[0], cord[1], cord[2], sep=',', end='\n')
            # number_of_vertex += 1






        for i in range(0, len(self.faces)):
            v0 = self.faces[i][0]
            v1 = self.faces[i][1]
            v2 = self.faces[i][2]
            self.faces_new.append(crdvtx(v0, self.adj_mtx[v0, v1], self.adj_mtx[v0, v2]))
            self.faces_new.append(crdvtx(v1, self.adj_mtx[v1, v2], self.adj_mtx[v1, v0]))
            self.faces_new.append(crdvtx(v2, self.adj_mtx[v2, v1], self.adj_mtx[v1, v2]))
            self.faces_new.append(crdvtx(self.adj_mtx[v2, v1], self.adj_mtx[v0, v1], self.adj_mtx[v0, v2]))
            # print(adjacency_matrix(self.faces_new, 42))
        # for face in self.faces_new:
        #     print(face[0], '\t', face[1], '\t', face[2])



        # print( 'adjency_matrix', adjency_matrix)
        # print('faces_new', faces_new)
