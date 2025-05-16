#  %% [markdown]
# Compare pkdgrav3 outputs with Quijote: halo mass function

# %%
import numpy as np
import bigfile
import readfof
from matplotlib import pyplot as plt

# %% [markdown]
# ## pkdgrav halo in bigfile

# %%
filename = '../../data/l/pkdgrav3_test.01000_fof'

with bigfile.File(filename) as bf:
    boxL = bf['Header'].attrs['BoxSize'][0]
    halo_pos = bf['CMPosition'][:]
    halo_vel = bf['CMVelocity'][:]
    halo_len = bf['Length'][:]

# %%
omega_m = 0.3175
rho_cr = 2.776e11 # M_sun h^2/Mpc^3
boxL = 1000 # Mpc/h
ngrid = 512 
mass_box = omega_m * rho_cr * boxL * boxL * boxL # M_sun/h
mp = mass_box / ngrid**3 # M_sun/h

# %%
halo_mass = halo_len[1:] * mp

# %% [markdown]
# ## Quijote halos

# %%
snapdir = '../../data/l/Quijote/Halos/FoF/fiducial/0/'
snapnum = 4
redshift = 0.0

# %%
# read the halo catalogue
FoF = readfof.FoF_catalog(snapdir, snapnum, long_ids=False, swap=False, SFR=False, read_IDs=False)

# %%
# get the properties of the halos
pos_h  = FoF.GroupPos/1e3            #Halo positions in Mpc/h
vel_h  = FoF.GroupVel*(1.0+redshift) #Halo peculiar velocities in km/s
mass_h = FoF.GroupMass*1e10          #Halo masses in Msun/h
Np_h   = FoF.GroupLen                #Number of CDM particles in the halo. Even in simulations with massive neutrinos, this will be just the number of CDM particles

# %% [markdown]
# ## HMF

# %%
min_mass = 1e13 #minimum mass in Msun/h
max_mass = 6e15 #maximum mass in Msun/h
bins     = 30   #number of bins in the HMF

# Correct the masses of the FoF halos
mass_h = mass_h*(1.0-Np_h**(-0.6))

bins_mass = np.logspace(np.log10(min_mass), np.log10(max_mass), bins+1)
mass_mean = 10**(0.5*(np.log10(bins_mass[1:])+np.log10(bins_mass[:-1])))
dM        = bins_mass[1:] - bins_mass[:-1]

# compute the halo mass function (number of halos per unit volume per unit mass)
HMF_quijote = np.histogram(mass_h, bins=bins_mass)[0]/(dM*boxL**3)
halo_mass = halo_mass*(1.0-halo_len[1:]**(-0.6))
HMF_pkdgrav3 = np.histogram(halo_mass, bins=bins_mass)[0]/(dM*boxL**3)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0, 'height_ratios': [2, 1]})
ax1.plot(mass_mean, HMF_quijote, label='Quijote halos', color='C0')
ax1.plot(mass_mean, HMF_pkdgrav3, '--', label='PKDgrav3+nbodykit.fof', color='C1')
ax1.set_ylabel(r'$HMF~[h^4M_\odot^{-1}{\rm Mpc}^{-3}]$')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend()
ax2.plot(mass_mean, HMF_pkdgrav3/HMF_quijote, label='PKDgrav3/Quijote', color='C2')
ax2.axhline(1.0, color='gray', linestyle='--')
ax2.axhspan(0.95, 1.05, color='gray', alpha=0.3)
ax2.set_xlabel(r'$M_{\rm halo}~[h^{-1}M_\odot]$')
# ax2.set_ylabel(r'$HMF_{\rm pkdgrav3}/HMF_{\rm Quijote}$')
ax2.set_xscale('log')
ax2.legend()
fig.savefig('../../figs/pkdgrav3_quijote_hmf.png', dpi=300, bbox_inches='tight')
