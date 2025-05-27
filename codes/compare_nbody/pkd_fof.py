#!/usr/bin/env python3
# Friends of friends (fof) group finding of a PKDGRAV output

# simulation mode is skipped when PKDGRAV imported
from sys import argv,exit
import PKDGRAV as msr
from PKDGRAV import OUT_TYPE

# Parse parameters. Name and grid size are required; box size is optional
if len(argv)<=2:
    print(f"Usage: {argv[0]} <filename> <grid number> <linking length/grid length> [minimum particle number]")
    # print("Usage: {} <filename> <dTau> [nMinMembers]".format(argv[0]))
    exit(1)
name=argv[1]
Ngrid = int(argv[2])
dTau = float(argv[3])/Ngrid
nMinMembers = 10 if len(argv)<4 else int(argv[4])

# Load the file and setup the tree, then run fof.
time = msr.load(name,bFindGroups = True,bMemGlobalGid = True, nMemEphemeral=8)
msr.domain_decompose()
msr.build_tree()

print(f"Running fof with dTau={dTau} and nMinMembers={nMinMembers} on {name}")
msr.fof(dTau,nMinMembers)
msr.reorder()

# Compare group assignments to some standard reference.
# msr.write_array(f"{name}.fof",OUT_TYPE.OUT_GLOBALGID_ARRAY)
msr.write_group_stats(f"{name}.fofstats")
