#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

mpirun -n 32 /root/main/pkdgrav3/build/pkdgrav3 nb-pkdgrav3.par