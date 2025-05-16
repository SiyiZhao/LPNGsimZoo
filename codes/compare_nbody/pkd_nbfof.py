#!/usr/bin/env python3
# Run FoF halo Finder of a Tipsy snapshot with nbodykit

import numpy as np
import sys
from nbodykit.lab import ArrayCatalog
from nbodykit.algorithms.fof import FOF

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
linking_length = float(sys.argv[2]) 
nmin = int(sys.argv[3])

print(f"Reading {file_name} with box size {boxL} Mpc/h")
header, particles = read_tipsy(file_name)
x = particles["x"] * boxL + boxL / 2
y = particles["y"] * boxL + boxL / 2
z = particles["z"] * boxL + boxL / 2
f_vec = 100 * boxL * np.sqrt(3/8/np.pi)
vx = particles["vx"] * f_vec
vy = particles["vy"] * f_vec
vz = particles["vz"] * f_vec
print(f"Read {len(particles)} particles, min position: ({x.min()}, {y.min()}, {z.min()}), max position: ({x.max()}, {y.max()}, {z.max()}), min velocity: ({vx.min()}, {vy.min()}, {vz.min()}), max velocity: ({vx.max()}, {vy.max()}, {vz.max()})")

pos = np.array([x, y, z]).T
vec = np.array([vx, vy, vz]).T

## nbodykit
cat = ArrayCatalog({'Position': pos, 'Velocity': vec})
cat.attrs['BoxSize'] = [boxL, boxL, boxL]
print(f"ArrayCatalog created.")
fof = FOF(cat, linking_length=linking_length, nmin=nmin)
fof.run()
halos = fof.find_features()
print(f"Found {len(halos)} halos with nmin={nmin} and linking length={linking_length} * boxL/Ngrid.")
halos.save(file_name + '_halo/fof')
print(f"Saved halos to {file_name}_halo/fof")
