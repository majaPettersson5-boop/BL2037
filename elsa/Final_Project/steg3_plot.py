import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

base_dir = "."
matrix_file = os.path.join(base_dir, "dist_matrix.txt")
output_tree = os.path.join(base_dir, "functional_clustering_tree.png")

print("Generating functional clustering tree for steg 3...")

# Läs in avståndsmatrisen från Clustal Omega (genererad i steg 2)
with open(matrix_file, "r") as f:
    lines = f.readlines()

protein_names = []
matrix_data = []

for line in lines[1:]:
    parts = line.strip().split()
    if parts:
        protein_names.append(parts[0])
        matrix_data.append([float(x) for x in parts[1:]])

df = pd.DataFrame(matrix_data, index=protein_names, columns=protein_names)

# Skapa den hierarkiska klustringen (Average linkage)
linked = linkage(df, method='average')

plt.figure(figsize=(12, 6))
dendrogram(linked,
            labels=protein_names,
            orientation='top',
            distance_sort='descending',
            show_leaf_counts=True)

# Ren och professionell engelsk rubrik anpassad för funktionsanalysen i steg 3
plt.title("Functional Grouping and Sequence Clustering Tree", fontsize=14, pad=15)
plt.xlabel("Protein ID")
plt.ylabel("Sequence Distance")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(output_tree, dpi=300)
print(f"-> Done! Saved tree as: {output_tree}")