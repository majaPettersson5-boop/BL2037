import os
import subprocess

# Sökvägar baserat på mappen du står i (Final_Project)
base_dir = "."
fasta_input = os.path.join(base_dir, "sequences.fasta")
alignment_output = os.path.join(base_dir, "aligned_sequences.fasta")
matrix_output = os.path.join(base_dir, "dist_matrix.txt")

print("Startar sekvensjämförelse (Alignment) med Clustal Omega...")

# Detta är kommandot vi skickar till datorn för att köra Clustal Omega
# --distmat-out skapar en matris som visar hur lika/olika sekvenserna är
cmd = [
    "clustalo",
    "-i", fasta_input,
    "-o", alignment_output,
    "--distmat-out=" + matrix_output,
    "--full",
    "--force"
]

try:
    # Kör Clustal Omega inifrån Python
    subprocess.run(cmd, check=True)
    print("-> Klart! Sekvenserna har lagts linjärt mot varandra.")
    print(f"-> Resultatet sparades till: {alignment_output}")
    print(f"-> Jämförelsematrisen sparades till: {matrix_output}")
except FileNotFoundError:
    print("FEL: Clustal Omega hittades inte. Kontrollera att installationen med micromamba gick bra.")
except subprocess.CalledProcessError as e:
    print(f"FEL under körning: {e}")

print("\n--- Steg 2: Alignment körd! ---")