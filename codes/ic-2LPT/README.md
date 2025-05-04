# Generate ICs with PNG-2LPTic

Here we show an example (the scripts we used), replace the settings and input files with your own.

- Refer the `.sh` file for the (qsub) submission script. Pay attention that you should `mkdir` the output directory first, and the path should be same as in configuration file.
- The configuration file is `settings.param`.
- The input data are:
  - `glass1_le`: not used, but should provided.
  - `log10pkl_z0.dat`: the linear matter power spectrum at z=0, in form of 
  - `Tk_z0.dat`: the transfer function at z=0, in form of 