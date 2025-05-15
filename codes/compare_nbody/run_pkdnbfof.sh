#!/bin/bash
# @r88

export OMP_NUM_THREADS=4
source ~/miniconda3/etc/profile.d/conda.sh
conda activate nbodykit

python3 pkd_nbfof.py /home/czhao/sims/nbody_correct/pkdgrav3_test.01000
