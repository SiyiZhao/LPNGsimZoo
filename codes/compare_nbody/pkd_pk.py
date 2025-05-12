#!/usr/bin/env python3
# Measure the power spectrum of a Tipsy snapshot with Pylians

import numpy as np
import sys
import MAS_library as MASL
import Pk_library as PKL

def read_tipsy(name, offset=0, count=-1):
    """
    Reads out particles from a Tipsy snapshot file
    :param name: Path to the snapshot file
    :param offset: Skip this many particles at the beginning
    :param count: Read this many particles, -1 -> read all particles
    """
    with open(name, "rb") as f:
        #header
        p_header_dt = np.dtype([('a','>d'),('npart','>u4'),('ndim','>u4'),('ng','>u4'),('nd','>u4'),('ns','>u4'),('buffer','>u4')])
        p_header = np.fromfile(f, dtype=p_header_dt, count=1, sep='')
        print(p_header)
        # get the total number of parts
        n_part = ((p_header["buffer"] & 0x000000ff).astype(np.uint64) << 32)[0] + p_header["npart"][0]
        print(f"Total number of particles: {n_part}")

        #particles
        p_dt = np.dtype([('mass','>f'),("x",'>f'),("y",'>f'),("z",'>f'),("vx",'>f'),("vy",'>f'),("vz",'>f'),("eps",'>f'),("phi",'>f')])
        count = int(n_part-int(offset)) if count == -1 else count
        p = np.fromfile(f, dtype=p_dt, count=count, sep='', offset=offset*p_dt.itemsize)

    return p_header, p

file_name = sys.argv[1]
boxL = 1000 # Mpc/h
nGridPk = int(sys.argv[2])
MAS = 'CIC'
axis = 0
threads = int(sys.argv[3]) if len(sys.argv) > 3 else 1
verbose = True

header, particles = read_tipsy(file_name)
x = particles["x"] * boxL + boxL / 2
y = particles["y"] * boxL + boxL / 2
z = particles["z"] * boxL + boxL / 2

pos = np.array([x, y, z]).T

## Pylians
delta = np.zeros((nGridPk,nGridPk,nGridPk), dtype=np.float32)
MASL.MA(pos, delta, boxL, MAS, verbose=verbose)
# compute density contrast: delta = rho/<rho> - 1
delta /= np.mean(delta, dtype=np.float64)
delta -= 1.0
# compute power spectrum
Pk = PKL.Pk(delta, boxL, axis, MAS, threads, verbose)
# 3D P(k)
k       = Pk.k3D
Pk0     = Pk.Pk[:,0] #monopole
Nmodes  = Pk.Nmodes3D
# save P(k)
np.savetxt(f"{file_name}.pypk", np.array([k, Pk0, Nmodes]).T, header="k P(k) Nmodes", fmt="%12.6e")
