from faces import *
import numpy as np

gl_rt = (np.sqrt(5.) + 1.) / 2.  # золотое сечение
vdata = []  # список с координатами вершин
vdata.append(
    crdvtx(-1. / np.sqrt(1. + pow(gl_rt, 2)), -(pow(gl_rt, 2) / (1. + pow(gl_rt, 2))), gl_rt / (1. + pow(gl_rt, 2))))
vdata.append(
    crdvtx(1. / np.sqrt(1. + pow(gl_rt, 2)), -(pow(gl_rt, 2) / (1. + pow(gl_rt, 2))), gl_rt / (1. + pow(gl_rt, 2))))
vdata.append(
    crdvtx(-(1. / np.sqrt(1. + pow(gl_rt, 2))), pow(gl_rt, 2) / (1. + pow(gl_rt, 2)), -(gl_rt / (1. + pow(gl_rt, 2)))))
vdata.append(
    crdvtx(1. / np.sqrt(1. + pow(gl_rt, 2)), pow(gl_rt, 2) / (1. + pow(gl_rt, 2)), -(gl_rt / (1. + pow(gl_rt, 2)))))
vdata.append(crdvtx(0., 0., 1.))
vdata.append(crdvtx(0., (2 * gl_rt) / (1. + pow(gl_rt, 2)), (-1. + pow(gl_rt, 2)) / (1. + pow(gl_rt, 2))))
vdata.append(crdvtx(0., -((2 * gl_rt) / (1. + pow(gl_rt, 2))), (1. - pow(gl_rt, 2)) / (1. + pow(gl_rt, 2))))
vdata.append(crdvtx(0., 0., -1.))
vdata.append(crdvtx(gl_rt / np.sqrt(1. + pow(gl_rt, 2)), 1. / (1. + pow(gl_rt, 2)), gl_rt / (1. + pow(gl_rt, 2))))
vdata.append(crdvtx(-(gl_rt / np.sqrt(1 + pow(gl_rt, 2))), 1. / (1. + pow(gl_rt, 2)), gl_rt / (1. + pow(gl_rt, 2))))
vdata.append(crdvtx(gl_rt / np.sqrt(1. + pow(gl_rt, 2)), -(1. / (1. + pow(gl_rt, 2))), -(gl_rt / (1 + pow(gl_rt, 2)))))
vdata.append(
    crdvtx(-(gl_rt / np.sqrt(1. + pow(gl_rt, 2))), -(1. / (1. + pow(gl_rt, 2))), -(gl_rt / (1. + pow(gl_rt, 2)))))
