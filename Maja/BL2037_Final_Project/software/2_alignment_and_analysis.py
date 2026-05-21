import os
import subprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Bio import AlignIO

# --- KONFIGURATION (Sökvägar anpassade för software/) ---
INPUT_FASTA = "../results/receptors_25.fasta"
ALIGNMENT_OUT = "../results/aligned_receptors.fasta"
TREE_OUT = "../results/receptor_tree.dnd"
PLOT_OUT = "../results/alignment_similarity_heatmap.png"

def run_clustal_omega():
    """
    Kör Clustal Omega via subprocess för att göra en Multiple Sequence Alignment
    och generera ett guideträd (clustering).
    """
    print("🧬 --- Steg 1: Kör Clustal Omega (MSA) via Subprocess ---")
    
    # Kontrollera om Clustal Omega är installerat på systemet
    # Standardnamn är oftast 'clustalo' (eller 'clustalw' om man använder det, men vi kör clustalo här)
    clustal_command = [
        "clustalo", 
        "-i", INPUT_FASTA, 
        "-o", ALIGNMENT_OUT, 
        "--guidetree-out=" + TREE_OUT, 
        "--force"
    ]
    
    try:
        # Kör kommandot i bakgrunden
        result = subprocess.run(clustal_command, capture_output=True, text=True, check=True)
        print("✅ MSA och klustringsträd har genererats framgångsrikt!")
        print(f"   Injusterad FASTA sparad i: {ALIGNMENT_OUT}")
        print(f"   Trädfil (.dnd) sparad i: {TREE_OUT}")
    except FileNotFoundError:
        print("❌ Fel: Kommandot 'clustalo' hittades inte på ditt system.")
        print("   Se till att Clustal Omega är installerat och tillagt i din PATH.")
        print("   Alternativt, ändra namnet på körfilen i skriptet om det heter t.ex. 'clustal-omega'.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Fel vid körning av Clustal Omega: {e.stderr}")
        return False
    return True

def calculate_pairwise_similarity():
    """
    Läser in den injusterade FASTA-filen, beräknar global parvis identitet (%)
    mellan alla 25 sekvenser över hela deras längd (Global Alignment).
    """
    print("\n📊 --- Steg 2: Beräknar parvis global sekvensidentitet ---")
    
    # Läs in alignment-filen
    alignment = AlignIO.read(ALIGNMENT_OUT, "fasta")
    num_seqs = len(alignment)
    seq_length = alignment.get_alignment_length()
    
    # Hämta namnen på alla sekvenser
    seq_names = [record.id for record in alignment]
    
    # Initiera en tom matris för identitetspoäng
    similarity_matrix = np.zeros((num_seqs, num_seqs))
    
    # Jämför sekvenserna parvis (Global positionsjämförelse)
    for i in range(num_seqs):
        for j in range(num_seqs):
            if i == j:
                similarity_matrix[i, j] = 100.0  # Identisk med sig själv
                continue
                
            matches = 0
            valid_positions = 0
            
            # Gå igenom varje position i den globala injusteringen
            for pos in range(seq_length):
                res1 = alignment[i][pos]
                res2 = alignment[j][pos]
                
                # Räkna bara positioner där båda sekvenserna har aminosyror (inte dubbla gaps)
                if res1 != '-' or res2 != '-':
                    valid_positions += 1
                    if res1 == res2:
                        matches += 1
            
            # Beräkna procentuell identitet över hela längden
            if valid_positions > 0:
                similarity_matrix[i, j] = (matches / valid_positions) * 100
            else:
                similarity_matrix[i, j] = 0.0
                
    return similarity_matrix, seq_names

def plot_similarity_heatmap(matrix, names):
    """
    Skapar en snygg heatmap av matrisen och sparar den i mappen results/.
    """
    print("\n📈 --- Steg 3: Skapar och sparar Heatmap-figur ---")
    
    # Skapa en Pandas DataFrame för snyggare hantering i Seaborn
    df = pd.DataFrame(matrix, index=names, columns=names)
    
    # Sätt upp storleken på figuren (eftersom det är 25x25 proteiner behövs lite utrymme)
    plt.figure(figsize=(14, 11))
    
    # Rita heatmapen
    sns.heatmap(
        df, 
        cmap="YlGnBu",      # Färgskala: Gul -> Grön -> Blå (Mörkt = hög likhet)
        annot=True,         # Skriv ut procenttalet i varje ruta
        fmt=".1f",          # En decimal
        annot_kws={"size": 7}, # Storlek på siffrorna i rutorna
        cbar_kws={'label': 'Sekvensidentitet (%)'}
    )
    
    plt.title("Global Parvis Sekvensidentitet (%) efter MSA (Clustal Omega)", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha='right', fontsize=9)
    plt.yticks(fontsize=9)
    plt.tight_layout()
    
    # Spara figuren
    plt.savefig(PLOT_OUT, dpi=300)
    print(f"🎉 KLART! Heatmap-grafen har sparats i: {PLOT_OUT}")
    plt.show()

def main():
    if not os.path.exists(INPUT_FASTA):
        print(f"❌ Hittade inte '{INPUT_FASTA}'. Kör script 1 först!")
        return
        
    # 1. Kör Clustal Omega
    success = run_clustal_omega()
    if not success:
        return
        
    # 2. Beräkna matrisen
    matrix, names = calculate_pairwise_similarity()
    
    # 3. Plotta och spara figuren
    plot_similarity_heatmap(matrix, names)

if __name__ == "__main__":
    main()