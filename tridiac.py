import gzip
import networkx as nx

# Load the Twitter data from the gzipped file as a directed graph
with gzip.open('twitter_combined.txt.gz', 'rt') as f:
    G_directed = nx.parse_edgelist(f, nodetype=int, create_using=nx.DiGraph())

# Conduct the triadic census
triadic_census = nx.algorithms.triads.triadic_census(G_directed)

# Output the results
for triad_type, count in triadic_census.items():
    print(f"{triad_type}: {count}")