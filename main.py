import gzip
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Load the Twitter data from the gzipped file
with gzip.open('twitter_combined.txt.gz', 'rt') as f:
    # Creating a directed graph from the edgelist
    G_directed = nx.parse_edgelist(f, create_using=nx.DiGraph())

# Convert the directed graph to an undirected graph
G_undirected = G_directed.to_undirected()

# Calculate centrality measures for the undirected graph
degree_centrality = nx.degree_centrality(G_undirected)
closeness_centrality = nx.closeness_centrality(G_undirected)
betweenness_centrality = nx.betweenness_centrality(G_undirected, normalized=True)

# Generate histograms for each centrality measure
plt.figure(figsize=(20, 5))

plt.subplot(1, 3, 1)
plt.hist(degree_centrality.values(), bins=100)
plt.title('Degree Centrality')

plt.subplot(1, 3, 2)
plt.hist(closeness_centrality.values(), bins=100)
plt.title('Closeness Centrality')

plt.subplot(1, 3, 3)
plt.hist(betweenness_centrality.values(), bins=100)
plt.title('Betweenness Centrality')

plt.show()

# Identify the top 200 nodes with the highest degree centrality
top_degree_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:200]

# For the top nodes, calculate the mean, median, and standard deviation of closeness and betweenness
top_closeness_values = [closeness_centrality[node] for node in top_degree_nodes]
top_betweenness_values = [betweenness_centrality[node] for node in top_degree_nodes]

mean_closeness = np.mean(top_closeness_values)
median_closeness = np.median(top_closeness_values)
std_closeness = np.std(top_closeness_values)

mean_betweenness = np.mean(top_betweenness_values)
median_betweenness = np.median(top_betweenness_values)
std_betweenness = np.std(top_betweenness_values)

(mean_closeness, median_closeness, std_closeness), (mean_betweenness, median_betweenness, std_betweenness)
