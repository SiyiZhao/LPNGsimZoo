#!/bin/bash
#SBATCH -J ic_L1000
#SBATCH -o ../../log/out/fastpmic_L1000_%J.out
#SBATCH -e ../../log/err/fastpmic_L1000_%J.err
#SBATCH -p intel
#SBATCH --nodes 8
#SBATCH --exclusive

module load intel/gsl/2.8/gcc8.5.0
module load intel/oneapi/2024.2.0
cd "$SLURM_SUBMIT_DIR"
export OMP_NUM_THREADS=1

mpirun -n 512 ../lib/fastpm-desi/src/fastpm ic-settings.lua
