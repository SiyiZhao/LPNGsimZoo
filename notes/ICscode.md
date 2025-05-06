# ICs Codes

We test several codes that *generate the Initial Conditions (ICs) of N-body simulations*.

## Prepare

The ICs codes need inputs of linear power spectrum (or transfer function) as well as cosmology parameters.

We recommand to run `ic-input/cosmo.ipynb` first, where you can set the cosmology parameters and generate the linear power spectrum (and transfer function).

When generating ICs, you should check the cosmology parameters in the configuration files, and move the output of `ic-input/cosmo.ipynb` to the working directory. 

## PNG-2LPTic

The original of [PNG-2LPTic](https://github.com/SiyiZhao/PNG-2LPTic) is the [2LPTnonlocal code](https://cosmo.nyu.edu/roman/2LPT/) from Roman Scoccimarro.

## FastPM-DESI

FastPM is a fast simulation code for cosmological N-body simulations. It can generate the ICs with the LPNG.

We use the version of FastPM that *is used in the DESI-PNG project*, so we call it FastPM-DESI.


## Our tests

We first compare *the output of FastPM-DESI* with *the output of PNG-2LPTic* codes.

We use the following setup:
- boxL = 1 Gpc/h, grid = 256, 
- cosmology = Planck2015Table4LastColumn, z = 99,
- $f_{\rm NL} = 100$.