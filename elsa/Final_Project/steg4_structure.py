import os
import glob
import subprocess
import numpy as np
import pandas as pd

base_dir = "."
clean_dir = os.path.join(base_dir, "clean_pdb_files")
output_csv = os.path.join(base_dir, "tm_rmsd_matrix.csv")

# Hitta alla sparade PDB-filer
pdb_files = sorted(glob.glob(os.path.join(clean_dir, "*_clean.pdb")))
protein_names = [os.path.basename(f).replace("_clean.pdb", "").upper() for f in pdb_files]
num_proteins = len(pdb_files)

rmsd_matrix = np.zeros((num_proteins, num_proteins))

print(f"Kör TM-align via Python subprocess för {num_proteins} proteiner...")

for i in range(num_proteins):
    for j in range(num_proteins):
        if i == j:
            rmsd_matrix[i, j] = 0.0
            continue
            
        # Kör externa programmet TMalign via subprocess enligt lärarens krav
        cmd = ["TMalign", pdb_files[i], pdb_files[j]]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            
            # Sätt ett standardavstånd (t.ex. 6.0 Å) om proteiner är helt olika och saknar RMSD
            rmsd_val = 6.0 
            
            # Letar efter raden där RMSD står i programmets text
            for line in result.stdout.split('\n'):
                if "RMSD=" in line:
                    # TM-align output ser ofta ut så här: "Aligned length=  123, RMSD=   2.45, Seq_ID=n.nnn"
                    parts = line.split(',')
                    for part in parts:
                        if "RMSD=" in part:
                            rmsd_val = float(part.split('=')[1].strip())
                            break
                    break
            rmsd_matrix[i, j] = rmsd_val
        except Exception as e:
            rmsd_matrix[i, j] = 6.0

# Spara strukturmatrisen till en CSV-fil
df = pd.DataFrame(rmsd_matrix, index=protein_names, columns=protein_names)
df.to_csv(output_csv)

print("-> Klar med TM-align!")
print(f"-> RMSD-matrisen sparades till: {output_csv}")