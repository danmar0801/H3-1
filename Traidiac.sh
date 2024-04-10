#!/bin/bash
#SBATCH --job-name=triadic_census     # Job name
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --output=triadic_census_%j.log  # Standard output log
#SBATCH --error=triadic_census_%j.err   # Standard error log

# Activate your conda environment
source /anaconda3/etc/profile.d/conda.sh
conda activate h3-1  # Replace "myenv" with the name of your conda environment

# Execute the Python script
python triadic.py  # Assuming your script is named 'triadic_census.py'

# Deactivate the conda environment if used
conda deactivate
