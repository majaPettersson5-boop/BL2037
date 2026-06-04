import os
import pandas as pd
from Bio.PDB import PDBList, PDBParser, MMCIFParser, Select, PDBIO

base_dir = "."
pdb_dir = os.path.join(base_dir, "pdb_files")
clean_dir = os.path.join(base_dir, "clean_pdb_files")

os.makedirs(pdb_dir, exist_ok=True)
os.makedirs(clean_dir, exist_ok=True)

csv_path = os.path.join(base_dir, "inputs_finalproject.csv")

try:
    df = pd.read_csv(csv_path)
    raw_pdb_ids = df.iloc[:, 0].dropna().unique()
    print(f"Hittade {len(raw_pdb_ids)} unika rader i CSV-filen.")
except Exception as e:
    print(f"Kunde inte läsa CSV-filen. Fel: {e}")
    raw_pdb_ids = []

pdbl = PDBList()

class CleanAndChainSelect(Select):
    def __init__(self, target_chain):
        # Om målkedjan är t.ex. 'BC', letar vi efter den omdöpta kedjan 'X'
        if target_chain and len(target_chain) > 1:
            self.target_chain = "X"
        else:
            self.target_chain = target_chain

    def accept_chain(self, chain):
        if self.target_chain and chain.id.upper() != self.target_chain.upper():
            return 0
        return 1

    def accept_residue(self, residue):
        if residue.get_resname() == "HOH":
            return 0
        if residue.id[0].startswith("H_"):
            return 0
        return 1

pdb_parser = PDBParser(QUIET=True)
cif_parser = MMCIFParser(QUIET=True)
io = PDBIO()

sequences_dict = {}

for raw_id in raw_pdb_ids:
    raw_id = raw_id.strip()
    print(f"\nBearbetar: {raw_id}")
    
    if "_" in raw_id:
        pdb_code, target_chain = raw_id.split("_")
    else:
        pdb_code, target_chain = raw_id, None
        
    pdb_code = pdb_code.lower()
    
    # 1. Försök först ladda ner som klassisk .pdb
    file_path = pdbl.retrieve_pdb_file(pdb_code, pdir=pdb_dir, file_format="pdb")
    current_parser = pdb_parser
    
    # 2. Om det misslyckas, testa mmCIF
    if not file_path or not os.path.exists(file_path):
        print(f"-> Testar mmCIF-format för {pdb_code.upper()}...")
        file_path = pdbl.retrieve_pdb_file(pdb_code, pdir=pdb_dir, file_format="mmCif")
        current_parser = cif_parser
    
    if file_path and os.path.exists(file_path):
        structure = current_parser.get_structure(pdb_code, file_path)
        
        # --- FIX FÖR LÅNGA KEDJENAMN (t.ex. BC) ---
        # Om kedjenamnet är längre än 1 bokstav, döp om det till 'X' i minnet
        if target_chain and len(target_chain) > 1:
            for model in structure:
                for chain in model:
                    if chain.id.upper() == target_chain.upper():
                        chain.id = "X"
        
        clean_file_path = os.path.join(clean_dir, f"{raw_id.lower()}_clean.pdb")
        io.set_structure(structure)
        io.save(clean_file_path, CleanAndChainSelect(target_chain))
        print(f"-> Klart! Rensad fil sparad till: {clean_file_path}")
        
        # Extrahera aminosyror
        from Bio.SeqUtils import seq1
        amino_acids = []
        for model in structure:
            for chain in model:
                # Kolla mot den omdöpta kedjan om det behövs
                check_chain = "X" if (target_chain and len(target_chain) > 1) else target_chain
                if check_chain and chain.id.upper() != check_chain.upper():
                    continue
                for residue in chain:
                    if residue.id[0] == " " and residue.get_resname() != "HOH":
                        try:
                            amino_acids.append(seq1(residue.get_resname()))
                        except:
                            pass
        
        sequence = "".join(amino_acids)
        if sequence:
            sequences_dict[raw_id] = sequence
            print(f"-> Extraherade sekvens ({len(sequence)} aa): {sequence[:20]}...")
    else:
        print(f"-> FEL: Kunde inte ladda ner {pdb_code.upper()} i något format.")

# Spara alla sekvenser till en FASTA-fil [cite: 41]
fasta_path = os.path.join(base_dir, "sequences.fasta")
with open(fasta_path, "w") as f:
    for header, seq in sequences_dict.items():
        f.write(f">{header}\n{seq}\n")

print(f"\n--- Steg 1 helt klart! Alla sekvenser sparade till: {fasta_path} ---")