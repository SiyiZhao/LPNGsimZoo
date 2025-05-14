#!/bin/bash
# @r88

export OMP_NUM_THREADS=4

STDOUT="logs/mpg_pk_stdout.log"
STDERR="logs/mpg_pk_stderr.log"

source ~/miniconda3/etc/profile.d/conda.sh
conda activate pylians
python3 mpg_pk.py /home/czhao/sims/nbody_mp_gadget/snap_004 1024 $OMP_NUM_THREADS > "$STDOUT" 2> "$STDERR"
