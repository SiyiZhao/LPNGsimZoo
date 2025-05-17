#!/bin/bash
#SBATCH -J convertic
#SBATCH -p xahctest
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH -o logs/convertic_stdout.log
#SBATCH -e logs/convertic_stderr.log

module load anaconda3/5.2.0
export PYTHONPATH=/work/home/siyizhao/codes:$PYTHONPATH

/usr/bin/time -f "real\t%E\nuser\t%U\nsys\t%S" -o logs/convertic_time.log python3 convert_IC.py /work/home/siyizhao/sims/IC_Quijote/raw/ics /work/home/siyizhao/sims/IC_Quijote/ics_for_pkdgrav3_correct.hdf5