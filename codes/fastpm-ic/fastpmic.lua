-- parameter file
------ Size of the simulation---------- 

-- For Testing
nc = 1024
boxsize = 1000.0
-------- Time Sequence ----
time_step = {0.01}

output_redshifts= {99.0}  -- redshifts of output

-- Cosmology --
Omega_m = 0.3089
h       = 0.6774
------- Initial power spectrum --------
-- See libfastpm/pngaussian.c for documentation
-- Amplitude of primordial power spectrum at pivot scale
scalar_amp = 2.120631e-9   -- same as scalar_amp in CAMB
-- Pivot scale k_pivot in 1/Mpc
scalar_pivot = 0.05  -- same as pivot_scalar in CAMB
-- Primordial spectral index n_s
scalar_spectral_index = 0.9667  -- same as scalar_spectral_index in CAMB
sigma8 = 0.8147
-- Start with a power spectrum file
-- Linear power spectrum at z=0: k P(k) in Mpc/h units
-- Must be compatible with the Cosmology parameter
read_powerspectrum = 'Planck2015Table4LastColumn_matterpower.dat'
f_nl_type = 'local'
f_nl = 100.
kmax_primordial_over_knyquist = 0.666
random_seed = 1001
remove_cosmic_variance = true
inverted_ic = true
particle_fraction = 1
-------- Approximation Method ---------------
force_mode = 'fastpm'
pm_nc_factor = 2      -- Particle Mesh grid pm_nc_factor*nc per dimension in the beginning
change_pm = 0.2
np_alloc_factor = 1.5
loglevel=0                 -- 0=verbose increase value to reduce output msgs

-------- Output ---------------

-- Dark matter particle outputs (all particles)
write_snapshot= '../../data/L1000fnl100r1001/ic/ic'       -- comment out to suppress snapshot output
