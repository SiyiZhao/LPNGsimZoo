#!/bin/bash

export OMP_NUM_THREADS=4

mpirun -n 32 /home/czhao/codes/MP-Gadget-master/gadget/MP-Gadget nb-mp-gadget.param
