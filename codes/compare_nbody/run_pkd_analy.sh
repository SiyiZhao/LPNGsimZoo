#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

mpirun -n 32 /root/main/pkdgrav3/build/pkdgrav3 pkd_analy.py /home/czhao/sims/nbody/pkdgrav3_test.00100 512 1000
