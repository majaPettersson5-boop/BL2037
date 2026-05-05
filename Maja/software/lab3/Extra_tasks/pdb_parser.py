from Bio.PDB import PDBParser, PPBuilder
import os

# --- SÖKVÄGAR ---
input_path = '../../../data/lab3/1ssc.pdb'
output_path = '../../../results/lab3/pdb_sequence.txt'
structure_id = "1ssc"

# --- STEG 1: LADDA STRUKTUREN ---
parser = PDBParser(QUIET=True)

try:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Hittade inte: {input_path}")

    structure = parser.get_structure(structure_id, input_path)
    ppb = PPBuilder()

    # --- STEG 2: EXTRAHERA OCH SPARA ---
    # Vi öppnar resultatfilen i skrivläge ('w')
    with open(output_path, 'w') as f:
        f.write(f"# Sequence extracted from {structure_id}\n")
        
        print(f"--- Amino Acid Sequence for {structure_id} Chain A ---")
        
        for model in structure:
            if 'A' in model:
                chain = model['A']
                for pp in ppb.build_peptides(chain):
                    seq = str(pp.get_sequence())
                    
                    # Skriv ut i terminalen
                    print(seq)
                    
                    # Spara i filen
                    f.write(f"Chain A: {seq}\n")
    
    print(f"\n✅ Sekvensen har sparats i: {output_path}")

except Exception as e:
    print(f"❌ Ett fel uppstod: {e}")