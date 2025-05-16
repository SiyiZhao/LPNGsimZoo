# %%
import numpy as np
from matplotlib import pyplot as plt

# %%
data = np.loadtxt('../../data/halo_pk/pkdgrav3_quijote_nmin19.txt')
k = data[:, 0]
pk_pkd = data[:, 1]
pk_ref = data[:, 2]
pk_pkd_osn = data[:, 3]
pk_ref_osn = data[:, 4]

# %%
## plot
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'hspace': 0, 'height_ratios': [2, 1]})
ax1.plot(k, pk_ref, label='Quijote halos', color='C0')
ax1.plot(k, pk_pkd, '--', label='PKDgrav3+nbodykit.fof', color='C1')
ax1.set_ylabel(r'$P(k)$ [Mpc/h]$^3$')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.legend()
ax2.plot(k, pk_pkd/pk_ref, label='PKDgrav3/Quijote w SN', color='C2')
# ax2.plot(k, pk_pkd_osn/pk_ref_osn, ':', label='PKDgrav3/Quijote w/o SN', color='C3')
ax2.axhline(1.0, color='gray', linestyle='--')
ax2.axhspan(0.98, 1.02, color='gray', alpha=0.3)
ax2.set_ylim(0.9, 1.1)
ax2.set_xlabel(r'$k$ [h/Mpc]')
ax2.set_ylabel(r'$P/P^{\rm Quijote}$')
ax2.set_xscale('log')
ax2.legend()
fig.savefig('../../figs/pkdgrav3_quijote_hpk.png', dpi=300, bbox_inches='tight')

# %%



