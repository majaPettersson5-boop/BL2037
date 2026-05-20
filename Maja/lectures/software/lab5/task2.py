import subprocess
import os
from Bio import SeqIO, Phylo

# --- SÖKVÄGAR ---
# Sökväg till dina PDB-filer (relativ till där du kör scriptet)
BASE_PATH = "../../data/lab5/structures_R/"

# Din specifika resultatmapp i "Maja"-mappen
OUTPUT_DIR = "/Users/majaalm/Desktop/GitHub/BL2037/Maja/results/lab5/"

# Filnamn baserat på den nya resultatmappen
INPUT_FASTA = os.path.join(OUTPUT_DIR, "receptors.fasta")
ALIGNED_FASTA = os.path.join(OUTPUT_DIR, "aligned_receptors.fasta")
TREE_FILE = os.path.join(OUTPUT_DIR, "tree_receptors.nwk")

# Proteinerna vi ska analysera
PDB_FILES = ["8JIQ_R.pdb", "8E3Y_R.pdb", "6WI9_R.pdb", "6X18_R.pdb", "7VQX_R.pdb", "7YON_R.pdb"]

def extract_sequences():
    """Extraherar sekvenser från PDB-filer och sparar i en FASTA-fil."""
    print(f"1. Extraherar sekvenser till: {INPUT_FASTA}")
    
    with open(INPUT_FASTA, "w") as f:
        for pdb_name in PDB_FILES:
            path = os.path.join(BASE_PATH, pdb_name)
            
            if not os.path.exists(path):
                print(f"   ⚠️ Varning: Hittade inte filen {path}")
                continue

            # Extrahera sekvensen (kedja R)
            for record in SeqIO.parse(path, "pdb-atom"):
                if record.id.endswith(":R"):
                    pdb_id = pdb_name.replace(".pdb", "")
                    f.write(f">{pdb_id}\n{record.seq}\n")
                    print(f"   ✅ Hittade sekvens för {pdb_id}")
                    break

def run_clustal():
    """Kör Clustal Omega via subprocess."""
    print("\n2. Startar Clustal Omega alignment...")
    clustal_command = [
        "clustalo", 
        "-i", INPUT_FASTA, 
        "-o", ALIGNED_FASTA, 
        "--outfmt=fasta", 
        "--guidetree-out", TREE_FILE, 
        "--force"
    ]
    
    try:
        subprocess.run(clustal_command, check=True)
        print(f"   ✅ Alignment klar! Fil sparat i: {ALIGNED_FASTA}")
        print(f"   ✅ Träd sparat i: {TREE_FILE}")
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Fel vid körning av Clustal Omega: {e}")
    except FileNotFoundError:
        print("   ❌ Fel: 'clustalo' hittades inte. Installera med: brew install clustal-omega")

def display_tree():
    """Läser och ritar upp trädet i terminalen."""
    if os.path.exists(TREE_FILE):
        print("\n3. --- Fylogenetiskt träd (Sekvenslikhet) ---")
        tree = Phylo.read(TREE_FILE, "newick")
        Phylo.draw_ascii(tree)
    else:
        print("\n   ❌ Kunde inte visa trädet eftersom filen saknas.")

def main():
    # Skapa resultatmappen om den inte finns
    if not os.path.exists(OUTPUT_DIR):
        print(f"Skapar ny mapp: {OUTPUT_DIR}")
        os.makedirs(OUTPUT_DIR)

    # Kör stegen
    extract_sequences()
    run_clustal()
    display_tree()

if __name__ == "__main__":
    main()