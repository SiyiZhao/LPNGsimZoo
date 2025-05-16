#!/usr/bin/env python3
# Measure the power spectrum of halos with Pylians and plot the comparison with Quijote

import numpy as np
import sys
import bigfile
import readfof
import MAS_library as MASL
import Pk_library as PKL

print('Compare pkdgrav3 / Quijote halo power spectrum')
## read bigfile for pkdgrav3
filename = '../../data/l/pkdgrav3_test.01000_fof_nmin19'
with bigfile.File(filename) as bf:
    boxL = bf['Header'].attrs['BoxSize'][0]
    halo_pos = bf['CMPosition'][:]
print(f'Loaded {halo_pos.shape[0]} pkdgrav3 halos')

## read Quijote halos
snapdir = '../../data/l/Quijote/Halos/FoF/fiducial/0/'
snapnum = 4
FoF = readfof.FoF_catalog(snapdir, snapnum, long_ids=False, swap=False, SFR=False, read_IDs=False)
pos_h  = FoF.GroupPos/1e3            #Halo positions in Mpc/h
# Np_h   = FoF.GroupLen
# mask = Np_h > 20
# pos_h = pos_h[mask]
print(f'Loaded {pos_h.shape[0]} Quijote halos')


## Pylians
nGridPk = int(sys.argv[1])
MAS = 'CIC'
axis = 0
threads = int(sys.argv[2]) if len(sys.argv) > 2 else 1
verbose = True

def measure_pk(pos):
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
    return k, Pk0
    
### for pkdgrav3
k_pkd, pk_pkd      = measure_pk(halo_pos)
### for Quijote
k_ref, pk_ref      = measure_pk(pos_h)
print(f'pk measured. k_diff={max(abs(k_pkd-k_ref))} should be 0.0')
boxV = boxL*boxL*boxL
SN_pkd = boxV / halo_pos.shape[0]
SN_ref = boxV / pos_h.shape[0]

## save pk 
np.savetxt('../../data/halo_pk/pkdgrav3_quijote_nmin19.txt', np.array([k_pkd, pk_pkd, pk_ref, pk_pkd-SN_pkd, pk_ref-SN_ref]).T, header='k pk_pkd pk_ref pk_pkd-SN pk_ref-SN', fmt="%12.6e")
print('Saved pkdgrav3 and Quijote pk to ../../data/halo_pk/pkdgrav3_quijote_nmin19.txt')
