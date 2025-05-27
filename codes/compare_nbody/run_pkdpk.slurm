#!/bin/bash
#SBATCH -J pkdpk         
#SBATCH -p xahctest
#SBATCH -n 4
#SBATCH --exclusive
#SBATCH -o logs/pkdpk_stdout.log
#SBATCH -e logs/pkdpk_stderr.log

export OMP_NUM_THREADS=4
source /public/software/apps/anaconda3/2023.09/etc/profile.d/conda.sh
conda activate nbodylians

python3 pkd_pk.py /work/share/acgy7e66b1/sims/nbody/pkdgrav3_test.01000 1024 $OMP_NUM_THREADS
