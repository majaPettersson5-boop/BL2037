import os
import matplotlib.pyplot as plt
from Bio import Phylo

# --- KONFIGURATION ---
TREE_IN = "../results/receptor_tree.dnd"
PLOT_OUT = "../results/protein_clustering_tree.png"

def plot_phylogenetic_tree():
    print("🌳 --- Steg 1: Läser in Clustal Omega-trädet (.dnd) ---")
    
    if not os.path.exists(TREE_IN):
        print(f"❌ Hittade inte trädfilen '{TREE_IN}'. Kör script 2 först!")
        return

    # Läs in trädet (Clustal Omega sparar i Newick-format)
    tree = Phylo.read(TREE_IN, "newick")
    
    print("📈 --- Steg 2: Skapar och anpassar trädfiguren ---")
    
    # Skapa en figur med bra storlek så att alla 25 proteinnamn syns tydligt
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Sätt lite designparametrar för trädet
    Phylo.draw(
        tree, 
        do_show=False, 
        axes=ax, 
        branch_labels=None # Döljer grenlängdssiffror för en renare bild
    )
    
    # Snygga till titlar och axlar
    plt.title("Sekvensbaserad klustring (Dendrogram) av 25 proteiner", fontsize=14, fontweight='bold', pad=20)
    plt.xlabel("Evolutionärt avstånd / Sekvensdiversitet", fontsize=11, labelpad=10)
    plt.ylabel("Proteiner (PDB ID + Kedja)", fontsize=11)
    
    # Justera marginaler så att namnen inte klipps bort till höger
    plt.tight_layout()
    
    # Spara figuren i results-mappen
    plt.savefig(PLOT_OUT, dpi=300)
    print(f"🎉 KLART! Klustringsträdet har sparats i: {PLOT_OUT}")
    plt.show()

if __name__ == "__main__":
    plot_phylogenetic_tree()