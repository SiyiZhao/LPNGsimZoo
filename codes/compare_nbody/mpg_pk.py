#!/usr/bin/env python3
# Measure the power spectrum of a Bigfile snapshot with Pylians

import numpy as np
import sys
import bigfile
import MAS_library as MASL
import Pk_library as PKL


## Settings
file_name = sys.argv[1]
boxL = 1000 # Mpc/h
nGridPk = int(sys.argv[2])
MAS = 'CIC'
axis = 0
threads = int(sys.argv[3]) if len(sys.argv) > 3 else 1
verbose = True

## Read the snapshot
print(f'Reading BigFile snapshot: {file_name}')
dataset = '1/Position' 
with bigfile.File(file_name) as bf:
    data = bf[dataset][:]
pos  = np.array(data, dtype=np.float32)
# covert to Mpc/h
pos /= 1000.0
print(f'Loaded {pos.shape[0]} particles')

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
