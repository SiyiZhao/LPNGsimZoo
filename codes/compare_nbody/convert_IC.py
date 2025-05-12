#!/usr/bin/env python3
# Convert 2LPTic outputs to pkdgrav3 compatible hdf5 initial condition

import sys
from pykdgrav3_utils.ic import from_gadget2binary

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} INPUT OUTPUT')
    print('  Convert 2LPTic outputs to pkdgrav3 compatible hdf5 initial condition')
    exit(1)


#from_gadget2binary(sys.argv[1], sys.argv[2], bMemSoft=True, ref_soft=48.828125)
from_gadget2binary(sys.argv[1], sys.argv[2], bMemSoft=True, ref_soft=50)

# Softening: 1/40 of interparticle spacing
