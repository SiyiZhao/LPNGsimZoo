#!/bin/bash
#PBS -N ic_2LPT
#PBS -V
#PBS -lselect=1:ncpus=48:mpiprocs=48:mem=600gb
#PBS -j oe
#PBS -o ../../log/

echo -e "\n\n======$PBS_JOBID - start `date`======\n"

module load gnu9 mpich gsl
# export LD_LIBRARY_PATH=/opt/ohpc/pub/libs/gnu9/gsl/2.7/lib/:$LD_LIBRARY_PATH
cd "$PBS_O_WORKDIR"
export OMP_NUM_THREADS=1

mkdir -p ../../data/ic2LPT/L250fnl100r1001
mpirun -n 48 ../lib/PNG-2LPTic/2LPTnonlocal settings.param 

echo -e "\n\n======finish $PBS_JOBID -  `date`======\n"
