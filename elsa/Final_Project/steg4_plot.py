import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform

base_dir = "."
csv_file = os.path.join(base_dir, "tm_rmsd_matrix.csv")
output_tree = os.path.join(base_dir, "structural_clustering_tree.png")

print("Genererar ett strukturträd baserat på TM-align...")

# 1. Läs in vår nya CSV-matris
df = pd.read_csv(csv_file, index_col=0)

# 2. Tvinga matrisen att bli perfekt symmetrisk för att ta bort små avrundningsfel
df_symmetric = (df + df.T) / 2

# 3. Konvertera matrisen till ett kondenserat format så att scipy förstår avstånden
condensed_matrix = squareform(df_symmetric)

# 4. Skapa klustringen baserat på de korrekta RMSD-avstånden
linked = linkage(condensed_matrix, method='average')

plt.figure(figsize=(12, 6))
dendrogram(linked,
            labels=df.index,
            orientation='top',
            distance_sort='descending',
            show_leaf_counts=True)

# Ren och snygg engelsk rubrik för sista steget
plt.title("Structural Similarity Clustering Tree", fontsize=14, pad=15)
plt.xlabel("Protein ID")
plt.ylabel("RMSD (Angstrom)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(output_tree, dpi=300)
print(f"-> Klart! Sparade strukturträdet som: {output_tree}")