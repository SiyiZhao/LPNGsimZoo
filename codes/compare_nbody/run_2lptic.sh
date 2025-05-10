#!/bin/bash
# @r88

export OMP_NUM_THREADS=1

mpirun -n 64 /root/main/2lpt/2LPTic 2LPT.param