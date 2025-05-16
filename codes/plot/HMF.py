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
logMh = np.log10(halo_mass)

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
log_mass_h = np.log10(mass_h)
bins = np.linspace(min(logMh.min(), log_mass_h.min()), max(logMh.max(), log_mass_h.max()), 50)
plt.hist(logMh, bins=bins, histtype='step', label='PKDGRAV3+nbodykit.fof')
plt.hist(log_mass_h, bins=bins, histtype='step', label='Quijote')
plt.yscale('log')
plt.xlabel(r'$\log_{10} M_h \, [M_\odot]$')
plt.ylabel('Number of halos')
plt.legend()
plt.savefig('../../figs/pkdgrav3_quijote_hmf.png', dpi=300)
