import gzip
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Load the Twitter data and create a directed graph
with gzip.open('twitter_combined.txt.gz', 'rt') as f:
    G_directed = nx.parse_edgelist(f, create_using=nx.DiGraph())

# Use only the largest connected component for faster processing
largest_cc = max(nx.connected_components(G_directed.to_undirected()), key=len)
G_undirected = G_directed.subgraph(largest_cc).to_undirected()

# Calculate degree centrality on the undirected graph
degree_centrality = nx.degree_centrality(G_undirected)

# Calculate closeness centrality only for the largest connected component
closeness_centrality = nx.closeness_centrality(G_undirected)

# Use approximate betweenness centrality for efficiency
betweenness_centrality = nx.betweenness_centrality(G_undirected, k=100, normalized=True, seed=7)  # k is the number of nodes to use in the approximation

# Generate histograms for each centrality measure in a batch
plt.figure(figsize=(20, 5))
for centrality, title in zip(centrality_measures, titles):
    plt.figure(figsize=(10, 4))
    plt.hist(centrality.values(), bins=100)
    plt.title(title)
    plt.savefig(f"{title.replace(' ', '_')}.png")
    plt.close()

# Identify the top 200 nodes with the highest degree centrality
top_degree_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:200]

# Efficiently compute the mean, median, and standard deviation for closeness and betweenness
top_closeness_values = np.fromiter((closeness_centrality[node] for node in top_degree_nodes), float)
top_betweenness_values = np.fromiter((betweenness_centrality[node] for node in top_degree_nodes), float)

mean_closeness = np.mean(top_closeness_values)
median_closeness = np.median(top_closeness_values)
std_closeness = np.std(top_closeness_values)

mean_betweenness = np.mean(top_betweenness_values)
median_betweenness = np.median(top_betweenness_values)
std_betweenness = np.std(top_betweenness_values)

# Print the results
print((mean_closeness, median_closeness, std_closeness), (mean_betweenness, median_betweenness, std_betweenness))