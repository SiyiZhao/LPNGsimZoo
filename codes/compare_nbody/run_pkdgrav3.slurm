#!/bin/bash
#SBATCH -J pkdgrav3         
#SBATCH -p xahctest
#SBATCH -N 2
#SBATCH --exclusive
#SBATCH -o logs/pkdgrav3_stdout.log
#SBATCH -e logs/pkdgrav3_stderr.log

module purge
module load mpi/openmpi/openmpi-4.1.5-gcc9.3.0
module load mathlib/gsl/2.6-intel-2017
module load mathlib/hdf5/1.8.20-intel-2017
module load mathlib/boost/1.67.0-intel-2017

source /public/software/apps/anaconda3/2023.09/etc/profile.d/conda.sh
conda activate pkd 

export OMP_NUM_THREADS=4

/usr/bin/time -f "real\t%E\nuser\t%U\nsys\t%S" -o logs/pkdgrav3_time.log mpirun -n 32 /work/home/siyizhao/codes/pkdgrav3/build/pkdgrav3 nb-pkdgrav3.par
