#!/bin/bash
#SBATCH -J 2lptic         
#SBATCH -p xahctest
#SBATCH -N 1
#SBATCH --ntasks-per-node=64
#SBATCH -o logs/2lpt_stdout.log
#SBATCH -e logs/2lpt_stderr.log


export OMP_NUM_THREADS=1
module load mathlib/gsl/2.6-intel-2017

/usr/bin/time -f "real\t%E\nuser\t%U\nsys\t%S" -o logs/2lpt_time.log mpirun -n 64 /work/home/siyizhao/codes/2lpt/2LPTic 2LPT.param
