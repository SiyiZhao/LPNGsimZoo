#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

mpirun -n 32 /home/zsy/code/pkdgrav3-dev/pkdgrav3 pkd_fof.py /home/czhao/sims/nbody_correct/pkdgrav3_test.01000 512 0.2 20
