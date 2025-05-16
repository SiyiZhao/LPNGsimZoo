#!/bin/bash
#PBS -N halo_ps
#PBS -V
#PBS -lselect=1:ncpus=32:mem=256gb
#PBS -j oe
#PBS -o ../../log/

export OMP_NUM_THREADS=32
cd "$PBS_O_WORKDIR"
source ~/miniconda3/etc/profile.d/conda.sh
conda activate nbodylians

python3 halo_ps.py 512 $OMP_NUM_THREADS