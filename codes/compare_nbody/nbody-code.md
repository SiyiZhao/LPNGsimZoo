# MP_Gadget

## repositories

https://github.com/MP-Gadget/MP-Gadget/tree/master

## installation

### pre-requests

#### manual install

- PFFT
   - may be automatically installed
   - manually download from https://github.com/rainwoodman/pfft/releases/download/1.0.8-alpha3-fftw3-2don2d/pfft-1.0.8-alpha3-fftw3-2don2d.tar.gz
   - build with `--prefix=/home/czhao/codes/MP-Gadget-master/depends --disable-shared --enable-static --enable-openmp --disable-fortran --disable-dependency-tracking --disable-doc --enable-mpi`

#### conda install

- nbodykit (for IC conversion)
   - `conda install bccp::nbodykit` with python 3.8
   - Make sure to use python <= 3.11 if installing manually (a limitation for classylss; this may work but I have not tested: https://github.com/nickhand/classylss/pull/30)
   - When installing with pip or manually, note that `mpi4py` requires cython >= 3.0, while `kdcount` requires cython 0.29. One may need to install different submodules individually and manually

## Others

### IC

Take the Quijote IC code, config file:

```lua
Nmesh  1024  % This is the size of the FFT grid used to
             % compute the displacement field. One
             % should have Nmesh >= Nsample.

Nsample  512 % sets the maximum k that the code uses,
             % i.e. this effectively determines the
             % Nyquist frequency that the code assumes,
             % k_Nyquist = 2*PI/Box * Nsample/2
             % Normally, one chooses Nsample such that
             % Ntot =  Nsample^3, where Ntot is the
             % total number of particles

Box  1000000.0  % Periodic box size of simulation

FileBase ics % Base-filename of output files
OutputDir  /home/czhao/sims/IC_Quijote/  % Directory for output

GlassFile  /root/main/2lpt/GLASS/dummy_glass_dmonly_64.dat  % Glass-File
GlassTileFac 8  % Number of times the glass file is
                % tiled in each dimension (must be
                % an integer)

Omega  0.3175  % Total matter density  (at z=0)
OmegaLambda  0.6825  % Cosmological constant (at z=0)
OmegaBaryon  0.0000  % Baryon density  (at z=0)
OmegaDM_2ndSpecies  0.0  % Omega for a second dark matter species (at z=0)
HubbleParam  0.6711  % Hubble paramater (may be used for power spec parameterization)

Redshift 127 % Starting redshift
Sigma8 0.834 % power spectrum normalization at z=0

SphereMode 0 % if "1" only modes with |k| < k_Nyquist are
             % used (i.e. a sphere in k-space), otherwise
             % modes with
             % |k_x|,|k_y|,|k_z| < k_Nyquist are used
             % (i.e. a cube in k-space)

WhichSpectrum  2 % "1" selects Eisenstein & Hu spectrum,
                 % "2" selects a tabulated power spectrum in
                 % the file 'FileWithInputSpectrum'
                 % otherwise, Efstathiou parametrization is used

FileWithInputSpectrum /root/main/2lpt/CAMB_TABLES/CAMB_matterpow_0.dat  % filename of tabulated MATTER powerspectrum from CAMB

InputSpectrum_UnitLength_in_cm  3.085678e24 % defines length unit of tabulated
                                            % input spectrum in cm/h.
                                            % Note: This can be chosen different
                                            % from UnitLength_in_cm

ShapeGamma 0.201 % only needed for Efstathiou power spectrum
PrimordialIndex  1.0 % may be used to tilt the primordial index
                     % (one if tabulated)

Phase_flip  0 % flip phase 0-no 1-yes for paired simulations)
RayleighSampling  1 % whether sampling modes amplitude (1) or not (0)
Seed  5 %  seed for IC-generator

NumFilesWrittenInParallel 64  % limits the number of files that are
                              % written in parallel when outputting

UnitLength_in_cm  3.085678e21  % define output length unit (in cm/h)
UnitMass_in_g 1.989e43 % define output mass unit (in g/cm)
UnitVelocity_in_cm_per_s  1e5  % define output velocity unit (in cm/sec)

WDM_On 0  % Putting a '1' here will enable a WDM small-scale
          % smoothing of the power spectrum
WDM_Vtherm_On  0  % If set to '1', the (warm) dark matter particles
                  % will receive an additional random thermal velocity
                  % corresponding to their particle mass

WDM_PartMass_in_kev  10.0 % This is the particle mass in keV of the WDM
                          % particle
```

### IC conversion

```bash
python3 /home/czhao/codes/MP-Gadget-master/tools/convert_from_gadget_1.py /home/czhao/sims/IC_Quijote/raw/ics /home/czhao/sims/IC_Quijote/ics_for_mp_gadget
```

### config file

```ini
InitCondFile        = /home/czhao/sims/IC_Quijote/ics_for_mp_gadget
OutputDir           = /home/czhao/sims/nbody_mp_gadget/
OutputList          = 0.25,0.33333333333333333,0.5,0.66666666666666666,1.0

TimeLimitCPU          = 10000000  # seconds
TimeMax	            = 1.00          # end at z=0

Omega0	            = 0.3175    # total matter density
OmegaLambda         = 0.6825
OmegaBaryon         = 0.0000     # maybe there are no baryons
HubbleParam         = 0.6711     # only needed for cooling

CoolingOn = 0
StarformationOn = 0
RadiationOn = 1
BlackHoleOn = 0
MetalReturnOn = 0
DensityIndependentSphOn = 1
HydroOn = 0
WindOn = 0
MassiveNuLinRespOn = 0

SnapshotWithFOF = 0
PartAllocFactor        = 2.5  
GravitySoftening       = 0.0256

###### Accuracy of time integration #######
   	                    
ErrTolIntAccuracy       = 0.025  
MaxSizeTimestep         = 0.025
MinSizeTimestep         = 0.0

####### Tree algorithm and force accuracy #######

ErrTolForceAcc              = 0.005

######## Parameters of SPH ########

MaxNumNgbDeviation = 2
ArtBulkViscConst   = 1.0
InitGasTemp        = 273.0  # initial gas temp in K, only used if not in ICs
MinGasTemp         = 10.0    
CourantFac         = 0.15

######## miscelanous ########

MinGasHsmlFractional   = 0.1  # min gas SPH in units of the grav softening
MaxRMSDisplacementFac  = 0.25 # limits the PM time step

######### output files  ##########

EnergyFile       = energy.txt
CpuFile          = cpu.txt
SnapshotFileBase = snap

```


## 3090

- 632m24.555s




# pkdgrav3

## repositories

- https://bitbucket.org/iacsimgro/pykdgrav3_utils/src/master/
- https://bitbucket.org/dpotter/pkdgrav3/src/master/
- https://bitbucket.org/iacsimgro/pkdgrav3_unittest/src/master/

## documentations

- https://research.iac.es/proyecto/PKDGRAV3/media/userguide.html
- https://pkdgrav3.readthedocs.io/_/downloads/en/latest/pdf/

## installation

### pre-requests

#### apt install

- openmpi
- cmake
- gsl (libgsl-dev)
- hdf5 (libhdf5-dev)

#### manual install

- FFTW3 (enable-mpi, enable-single, enable-threads)

#### pip install

- numpy
- tomli
- dill
- cython (version newer than that from apt)
- pykdgrav3_utils (for IC conversion)

### build

```bash
FFTW_DIR=/root/main/fftw-3.3.10
cmake -DFFTW_ROOT=$FFTW_DIR -DUSE_CPPTRACE=off .. && make
```

## others

### IC conversion

```python
#!/usr/bin/env python3
# Convert 2LPTic outputs to pkdgrav3 compatible hdf5 initial condition

import sys
from pykdgrav3_utils.ic import from_gadget2binary

if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} INPUT OUTPUT')
    print('  Convert 2LPTic outputs to pkdgrav3 compatible hdf5 initial condition')
    exit(1)


from_gadget2binary(sys.argv[1], sys.argv[2], bMemSoft=True, ref_soft=48.828125)

# Softening: 1/40 of interparticle spacing

```

### config file

```ini
from accuracy import classic_theta_switch,classic_replicas_switch

achOutName      = "/home/czhao/sims/nbody/pkdgrav3_test"

# Initial Condition
achInFile       = "/home/czhao/sims/IC_Quijote/ics_for_pkdgrav3_new.hdf5"
dBoxSize        = 1000
dRedFrom        = 127

# Cosmology
h               = 0.6711
dOmega0         = 0.3175
dOmegab         = 0.0000
dLambda         = 0.6825

iStartStep      = 0
nSteps          = 100
dRedTo          = 0.0

# Cosmological Simulation
bComove         = True          # Use comoving coordinates
bPeriodic       = True          # with a periodic box
bEwald          = True          # enable Ewald periodic boundaries

# Logging/Output
iOutInterval    = 10
bDoDensity      = True
bVDetails       = True

bOverwrite      = True
bParaRead       = True          # Read in parallel
bParaWrite      = True         # Write in parallel (does not work on all file systems)
nParaRead      = 8             # Limit number of simultaneous readers to this
nParaWrite     = 8             # Limit number of simultaneous writers to this

# Accuracy Parameters
bEpsAccStep     = True          # Choose eps/a timestep criteria
dTheta          = classic_theta_switch()        # 0.40, 0.55, 0.70 switch
nReplicas       = classic_replicas_switch()     # 1 if theta > 0.52 otherwise 2

# Memory and performance
bMemUnordered   = True          # iOrder replaced by potential and group id
bNewKDK         = True          # No accelerations in the particle, dual tree possible
```

### Running

```bash
export OMP_NUM_THREADS=4
mpirun -n 32 /root/main/pkdgrav3/build/pkdgrav3 nb-pkdgrav3.par
```

## H200

### 32 tasks, 4 threads per task

- 100 steps
   - CPU + GPU: ~1 hour


## 3090

### 32 tasks, 4 threads per task

- 100 steps
   - CPU + GPU: 113 mins
   - CPU only: 143m32.479s

- 1000 steps
   - CPU + GPU: 233m25.109s

## 海光 cpu  

- 1000 steps
  - CPU only: real	28:23:08  (user	2241504.51  sys	1028060.48)


# CUBE

## installation

### pre-requests

- intel compilers (note that from oneapi 2025, `ifort` is replaced by `ifx`, to be safe we use the conventional version)
   - OneAPI base toolkit: https://registrationcenter-download.intel.com/akdlm/IRC_NAS/163da6e4-56eb-4948-aba3-debcec61c064/l_BaseKit_p_2024.0.1.46_offline.sh
   - OneAPI HPC toolkit: https://registrationcenter-download.intel.com/akdlm/IRC_NAS/67c08c98-f311-4068-8b85-15d79c4f277a/l_HPCKit_p_2024.0.1.38_offline.sh
   - Environmental settings with `source /opt/intel/oneapi/2024.0/oneapi-vars.sh`
   - But then `icc` is already replaced by `icx` in oneapi 2024. Consider installing the 2023 version if need, see https://stackoverflow.com/questions/77618190/how-to-use-icc-if-i-only-installed-the-latest-intel-hpc-toolkit

### compile

Add the following lines to the head of Makefile:

```makefile
FC = ifort
XFLAG = -O3 -fpp -qopenmp -coarray=distributed -mcmodel=large -coarray-config-file=cafconfig.txt
OFLAG = $(XFLAG) -c
FFTFLAG = -I/opt/intel/oneapi/2024.0/include/fftw -mkl
```

