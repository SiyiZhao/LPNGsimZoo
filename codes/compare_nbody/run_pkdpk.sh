#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

STDOUT="logs/pkd_pk_1000_stdout.log"
STDERR="logs/pkd_pk_1000_stderr.log"

python3 pkd_pk.py /home/czhao/sims/nbody_correct/pkdgrav3_test.01000 1024 $OMP_NUM_THREADS > "$STDOUT" 2> "$STDERR"
