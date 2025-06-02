## Tested on ShuGuang xahctest partition

The following two tests were run on the ShuGuang xahctest partition, which is a test partition with limited resources. The tests are done by the engineering team of ShuGuang.

### 128 processors

- job ID: 32911125
- 2 nodes, 128 processors
- Elapsed: 09:11:39
  - Start On: Fri May 30 10:15:09 CST 2025
  - End On: Fri May 30 19:26:48 CST 2025

### 64 processors

- job ID: 32910887
- 1 node, 64 processors
- Elapsed: 15:24:41
  - Start On: Fri May 30 10:09:27 CST 2025
  - End On: Fri May 31 01:35:08 CST 2025

## Tested on LianTai's computer 

To compare with the tests on ShuGuang, we also ran a "CPU-only" test on LianTai's computer.

**Since they setting OMP_NUM_THREADS=8 and using 128 MPI processes, the total number of threads is 1024. So the Comparison can not be fair, we stop here.**