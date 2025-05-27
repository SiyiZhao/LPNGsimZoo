#!/bin/bash
#SBATCH -J pkdnbfof         
#SBATCH -p xahctest
#SBATCH -n 4
#SBATCH --exclusive
#SBATCH -o logs/pkdnbfof_stdout.log
#SBATCH -e logs/pkdnbfof_stderr.log

export OMP_NUM_THREADS=4
source /public/software/apps/anaconda3/2023.09/etc/profile.d/conda.sh
conda activate nbodylians

/usr/bin/time -f "real\t%E\nuser\t%U\nsys\t%S" -o logs/pkdnbfof_time.log python3 pkd_nbfof.py /work/share/acgy7e66b1/sims/nbody/pkdgrav3_test.01000 0.2 19
