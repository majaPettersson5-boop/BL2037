import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_dir = "."
matrix_file = os.path.join(base_dir, "dist_matrix.txt")
output_heatmap = os.path.join(base_dir, "sequence_heatmap.png")

print("Genererar sequence similarity heatmap...")

# 1. Läs in avståndsmatrisen från Clustal Omega
with open(matrix_file, "r") as f:
    lines = f.readlines()

protein_names = []
matrix_data = []

for line in lines[1:]:
    parts = line.strip().split()
    if parts:
        protein_names.append(parts[0])
        matrix_data.append([float(x) for x in parts[1:]])

# 2. Skapa en DataFrame
df_distance = pd.DataFrame(matrix_data, index=protein_names, columns=protein_names)

# 3. Gör om avstånd till procentuell likhet (0% till 100%)
df_similarity = (1 - df_distance) * 100

# 4. Rita färgkartan (Heatmap)
plt.figure(figsize=(12, 10))
sns.heatmap(
    df_similarity, 
    cmap="YlGnBu",      # Gul-Grön-Blå färgskala
    annot=False,        # Sätt till True om du vill ha siffror i rutorna
    cbar_kws={'label': 'Sequence Similarity (%)'}
)

# Ren rubrik utan "Phase B"
plt.title("Sequence Similarity Between the 25 Proteins", fontsize=14, pad=15)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()

# 5. Spara bilden
plt.savefig(output_heatmap, dpi=300)
print(f"-> Klart! Heatmap sparades som: {output_heatmap}")