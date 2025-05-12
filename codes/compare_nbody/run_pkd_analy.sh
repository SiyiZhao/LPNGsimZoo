#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

STDOUT="logs/pkd_analy_1000_stdout.log"
STDERR="logs/pkd_analy_1000_stderr.log"

mpirun -n 32 /root/main/pkdgrav3/build/pkdgrav3 pkd_analy.py /home/czhao/sims/nbody_step1000/pkdgrav3_test.01000 512 1000 > "$STDOUT" 2> "$STDERR"
