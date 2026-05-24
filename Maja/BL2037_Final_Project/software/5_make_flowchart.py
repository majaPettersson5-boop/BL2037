import matplotlib.pyplot as plt

# Skapa en tom figur med bra storlek
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')

# Textinnehåll för flödesschemat
flowchart_text = """
       [ RCSB PDB Server ]
                │
                ▼ (Download)
┌────────────────────────────────────────────────────────┐
│ STEP 1: 1_data_download.py                             │
│ ───► Uses Bio.PDB to fetch raw .cif files              │
│ ───► Cleans structures (removes water & HETATMs)       │
└────────────────────────────────────────────────────────┘
                │
                ├─► Saves sequences ──► [ receptors_25.fasta ]
                │
                └─► Saves 3D shapes ──► [ results/clean_structures/ ]
                                                 │
         ┌───────────────────────────────────────┴───────────────────────────────────────┐
         ▼ (Sequence Path)                                                               ▼ (Structure Path)
┌─────────────────────────────────────────┐                     ┌─────────────────────────────────────────┐
│ STEP 2: 2_sequence_alignment.py         │                     │ STEP 4: 4_structural_analysis.py        │
│ ───► Runs Clustal Omega                 │                     │ ───► Performs 3D superimposition        │
│ ───► Calculates % identity matrix       │                     │ ───► Calculates pairwise RMSD matrix    │
└─────────────────────────────────────────┘                     └─────────────────────────────────────────┘
       │                 │                                                             │                 │
       ▼ (Saves)         ▼ (Saves)                                                     ▼ (Saves)         ▼ (Saves)
[aligned_receptors.fasta] [alignment_similarity_heatmap.png]         [structural_rmsd_heatmap.png] [structural_clustering_tree.png]
       │
       ▼ (Automatic output)
[ receptor_tree.dnd ]
       │
       ▼ (Input for next step)
┌─────────────────────────────────────────┐
│ STEP 3: 3_clustering_tree.py            │
│ ───► Reads Newick tree with Phylo       │
│ ───► Plots sequence relationships       │
└─────────────────────────────────────────┘
       │
       ▼ (Saves)
[protein_clustering_tree.png]
"""

# Rita ut texten i figuren med ett monospace-teckensnitt så linjerna passar ihop
plt.text(0.01, 0.99, flowchart_text, fontfamily='monospace', fontsize=9, va='top', ha='left')

# Spara som en snygg PNG-bild
plt.tight_layout()
plt.savefig('../results/pipeline_flowchart.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ Flödesschemat har sparats som 'pipeline_flowchart.png' i din results-mapp!")