#!/bin/bash -l
#SBATCH --job-name=hypoxiaCTLA4TreatmentEval
#SBATCH --nodes=6
#SBATCH --tasks-per-node=10
#SBATCH --cpus-per-task=10
#SBATCH --time=00:01:00
#SBATCH --mail-user=23303755@student.uwa.edu.au
#SBATCH --mail-type=ALL
# load modules
module load python/3.11.6
module load py-numpy/1.26.1
module load py-matplotlib/3.8.1
module load py-pandas/2.1.2
# launch serial python script
srun python3 CTLA4TreatmentEvalHypoxia.py
