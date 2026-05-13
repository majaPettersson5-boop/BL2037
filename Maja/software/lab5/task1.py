import subprocess
import re
import csv
import os  # Ny import för att hantera mappar

# --- Configuration ---
BASE_PATH = "./data/lab5/structures_R/"
# Här definierar vi var CSV-filen ska hamna
OUTPUT_DIR = "./results/lab5/"
output_csv = os.path.join(OUTPUT_DIR, "tmalign_results.csv")

TARGETS = [
    BASE_PATH + "8E3Y_R.pdb", 
    BASE_PATH + "6WI9_R.pdb", 
    BASE_PATH + "6X18_R.pdb", 
    BASE_PATH + "7VQX_R.pdb", 
    BASE_PATH + "7YON_R.pdb"
]
REFERENCE = BASE_PATH + "8JIQ_R.pdb"

def parse_tmalign_output(output_text):
    """Använder regex för att hitta TM-score och RMSD."""
    tm_match = re.search(r"TM-score\s*=\s*(\d\.\d+)", output_text)
    rmsd_match = re.search(r"RMSD\s*=\s*(\d\.\d+)", output_text)
    
    tm_score = tm_match.group(1) if tm_match else "N/A"
    rmsd = rmsd_match.group(1) if rmsd_match else "N/A"
    return tm_score, rmsd

def main():
    # Skapa results-mappen om den inte finns
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Skapade mappen: {OUTPUT_DIR}")

    results = []
    print("--- Startar TM-align batch-analys ---")

    for target_file in TARGETS:
        # Prefix för alignment-filer (sparar dem också i results/lab5/)
        pdb_id = target_file.split("/")[-1].replace(".pdb", "")
        output_prefix = os.path.join(OUTPUT_DIR, f"{pdb_id}_superposed")
        
        command = ["TMalign", REFERENCE, target_file, "-o", output_prefix]
        
        try:
            print(f"Analyserar {pdb_id}...")
            process = subprocess.run(command, capture_output=True, text=True, check=True)
            
            tm_score, rmsd = parse_tmalign_output(process.stdout)
            
            results.append({
                "PDB_ID": pdb_id,
                "TM-score": tm_score,
                "RMSD": rmsd
            })

        except subprocess.CalledProcessError:
            print(f"❌ Fel vid körning av {pdb_id}")

    # Spara till CSV i results/lab5/
    with open(output_csv, "w", newline="") as csvfile:
        fieldnames = ["PDB_ID", "TM-score", "RMSD"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Klart! Sammanfattningen sparades i: {output_csv}")

if __name__ == "__main__":
    main()