# LPNG Simulations Zoo

For non-linear modeling of Cosmic Large Scale Stuctures (CLaSS, LSS) with Local-type Primordial non-Gaussianity (LPNG), we need sets of simulations with LPNG.

## Simulation Sets

We have following sets:
1. Nbody simulations in 1Gpc/h with several $f_{\rm NL}$ values for model calibrate and emulator. 

Refer **a summary of other LPNG simulation sets** in [TBD].

## Tests of Codes 

### Initial Condition

- 2LPT-PNGnonlocal
- MonofonIC 
- FastPM-DESI

### Nbody

We test 4 Nbody codes:
- Gadget4
- CUBE
- MP-Gadget
- PKDgrav3

See the details in the [Nbodycode.md](notes/Nbodycode.md) file.


---

## Dependency & Submodules

This repo contains several submodules.
- [PNG-2LPTic](https://github.com/SiyiZhao/PNG-2LPTic)

### How to use submodules

To clone this repository along with its submodules, use the following command:
```bash
git clone --recurse-submodules https://github.com/SiyiZhao/LPNGsimZoo.git
```

If you have already cloned the repository without submodules, you can initialize and update the submodules with:
```bash
git submodule update --init --recursive
```

To update the submodules to their latest versions, run:
```bash
git submodule update --remote
```
