import pandas as pd

# Ladda data (OBS: stor/liten bokstav på Data!)
df = pd.read_csv("../../../Data/Lab3/gene_expression.csv")

# --- Statistik ---
print("\n--- Summary Statistics ---")
print("Mean:\n", df.mean(numeric_only=True))
print("Max:\n", df.max(numeric_only=True))
print("Min:\n", df.min(numeric_only=True))

# --- Filtrering ---
filtered_df = df[df["TPM"] > 100]

print("\n--- Genes with TPM > 100 ---")
print(filtered_df)