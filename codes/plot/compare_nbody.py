#  %% [markdown]
# Compare pkdgrav3 / mp-gadget outputs with Quijote: matter power spectrum

# %%
import numpy as np
from matplotlib import pyplot as plt

# %% [markdown]
# ## Quijote reference

# %%
data = np.loadtxt('../../data/quijote/Pk/matter/fiducial/0/Pk_m_z=0.txt')
k_ref = data[:, 0]
pk_ref = data[:, 1]

# %% [markdown]
# ## PKDgrav3 outputs

# %%
data = np.loadtxt('../../data/pkd_out/pkdgrav3_test.01000.pypk')
k_pkd = data[:, 0]
pk_pkd = data[:, 1]
nk_pkd = data[:, 2]

# %% [markdown]
# ## MP-Gadget outputs

# %%
data = np.loadtxt('../../data/mp-gadget/snap_004.pypk')
k_mpg = data[:, 0]
pk_mpg = data[:, 1]
nk_mpg = data[:, 2]

# %%
data = np.loadtxt('../../data/mp-gadget/powerspectrum-1.0000.txt')
k_mpg2 = data[:, 0]
pk_mpg2 = data[:, 1]

# %% [markdown]
# ## Plot

# %%
from scipy import interpolate
f = interpolate.interp1d(k_ref, pk_ref, kind='cubic', bounds_error=False, fill_value=0.0)
pk_ref_interp = f(k_mpg2)

# %%
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0, 'height_ratios': [2, 1]})

# 上图
ax1.plot(k_ref, pk_ref, label='Quijote, z=0')
ax1.plot(k_pkd, pk_pkd, '--', label='pkdgrav3, step 1000')
ax1.plot(k_mpg, pk_mpg, ':', label='mp-gadget, pylians')
# ax1.plot(k_mpg2, pk_mpg2, ':', label='mp-gadget, output')
ax1.set_ylabel(r'$P(k)$ [Mpc/h]$^3$')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend()

# 下图
diff_pkd = pk_pkd / pk_ref - 1
ax2.plot(k_pkd, diff_pkd, color='C1', label='pkdgrav3')
diff_mpg = pk_mpg / pk_ref - 1
ax2.plot(k_mpg, diff_mpg, color='C2', label='mp-gadget')
diff_mpg2 = pk_mpg2 / pk_ref_interp - 1
# ax2.plot(k_mpg2, diff_mpg2, ':', color='C3', label='mp-gadget, output')
ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8)
ax2.axhspan(-0.01, 0.01, color='gray', alpha=0.3)
ax2.set_ylim(-0.1, 0.1)
ax2.set_xlabel(r'$k$ [h/Mpc]')
ax2.set_ylabel('P/P^Quijote - 1')
ax2.set_xscale('log')
ax2.legend()


# %%
fig.savefig('../../figs/compare_nbody.png', dpi=300, bbox_inches='tight')

