#!/usr/bin/env python3
# Measure the power spectrum of a PKDGRAV output

# simulation mode is skipped when PKDGRAV imported
import PKDGRAV as msr
from sys import argv,exit

# Name and grid size are required; box size is optional
if len(argv)<=2:
    print(f"Usage: {argv[0]} <filename> <grid> [box-length]")
    exit(1)
name=argv[1]
nGridPk = int(argv[2])
L = 1 if len(argv)<4 else int(argv[3])

# Load the file and setup the tree, then measure the power
time = msr.load(name,nGridPk=nGridPk)
msr.domain_decompose()
msr.build_tree()
(K,PK,N,*rest) = msr.measure_pk(nGridPk,L=L)

with open(f'{name}.pk','w') as f:
  for k,pk,n in zip(K,PK,N):
    if n>0: f.write(f'{k} {pk} {n}\n')
