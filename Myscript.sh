#!/bin/bash
#SBATCH --job-name=network_analysis  # Job name
#SBATCH --ntasks=2                   # Run on a single CPU
#SBATCH --output=network_analysis_%j.log  # Standard output and error log

# Load the module for Anaconda3 or your specific Python version if required
# module load anaconda3/2020.02

# Activate your conda environment
source /anaconda3/etc/profile.d/conda.sh
conda activate h3-1  # Replace "myenv" with the name of your conda environment

# Execute the Python script
python main.py  # Replace with your Python script filename

# After the script finishes, deactivate the conda environment
conda deactivate
