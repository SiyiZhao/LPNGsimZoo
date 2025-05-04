# ICs Codes

We test several codes that *generate the Initial Conditions (ICs) of N-body simulations*.


## PNG-2LPTic

The original of [PNG-2LPTic](https://github.com/SiyiZhao/PNG-2LPTic) is the [2LPTnonlocal code](https://cosmo.nyu.edu/roman/2LPT/) from Roman Scoccimarro.

## FastPM-DESI

FastPM is a fast simulation code for cosmological N-body simulations. It can generate the ICs with the LPNG.

We use the version of FastPM that *is used in the DESI-PNG project*, so we call it FastPM-DESI.


## Our tests

We first compare *the output of FastPM-DESI* with *the output of PNG-2LPTic* codes.

We use the following setup:
- boxL = 1 Gpc/h, grid = 1024, 
- cosmology = Planck2015Table4LastColumn, z = 99,
- $f_{\rm NL} = 100$.