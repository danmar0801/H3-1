# Twitter Network Analysis

This repository contains the necessary scripts for conducting a network analysis on a Twitter dataset.

## Files

- `main.py`: Python script for calculating various centrality measures on the Twitter network.
- `Myscript.sh`: SLURM batch script to submit `main.py` for execution on an HPC cluster.
- `README.md`: This file, providing an overview and instructions for the repository.
- `Traidiac.sh`: SLURM batch script to submit `triadic.py` for a triadic census on an HPC cluster.
- `triadic.py`: Python script for performing a triadic census on the Twitter dataset.
- `twitter_combined.txt.gz`: The compressed Twitter dataset to be analyzed.

## Usage

Submit the SLURM batch scripts to an HPC cluster after setting the appropriate job configurations:

```bash
sbatch Myscript.sh   # For centrality measures
sbatch Traidiac.sh   # For triadic census
```

Ensure you are in the directory containing these files when submitting the job. Modify the SLURM scripts if needed to suit your HPC environment and policies.