# Import subprocess to run Clustal Omega from Python
import subprocess

# List of pdb files, chain R
pdb_files = [
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/8JIQ_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/8E3Y_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/6WI9_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/6X18_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/7VQX_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/7YON_R.pdb"
]

# Define output folder
results_folder = "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Results/Lab5"

# Define input and output filenames
input_fasta = results_folder + "/receptors.fasta"
aligned_output = results_folder + "/aligned_receptors.fasta"
tree_output = results_folder + "/tree_receptors.nwk"


# Function to extract chain R sequence from pdb file
def extract_sequence_from_pdb(pdb_file):

    # Dictionary converting 3-letter amino acid codes to 1-letter codes
    aa_dict = {
        "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D",
        "CYS": "C", "GLU": "E", "GLN": "Q", "GLY": "G",
        "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
        "MET": "M", "PHE": "F", "PRO": "P", "SER": "S",
        "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"
    }

    sequence = ""
    seen_residues = set()

    # Open pdb file and read line by line
    with open(pdb_file, "r") as file:

        for line in file:

            # Only use ATOM lines from chain R
            if line.startswith("ATOM") and line[21] == "R":

                residue_name = line[17:20].strip()
                residue_number = line[22:26].strip()

                # Avoid duplicates from same residue
                if residue_number not in seen_residues:

                    seen_residues.add(residue_number)

                    # Convert residue to 1-letter amino acid
                    if residue_name in aa_dict:
                        sequence += aa_dict[residue_name]

    return sequence


# Create fasta file with all receptor sequences
with open(input_fasta, "w") as fasta_file:

    for pdb_file in pdb_files:

        # Extract only the file name and remove .pdb
        pdb_id = pdb_file.split("/")[-1].replace(".pdb", "")

        sequence = extract_sequence_from_pdb(pdb_file)

        # Write fasta header, for example >8JIQ_R
        fasta_file.write(f">{pdb_id}\n")

        # Write amino acid sequence
        fasta_file.write(sequence + "\n")


# Build Clustal Omega command
clustal_command = [
    "clustalo",
    "-i", input_fasta,
    "-o", aligned_output,
    "--outfmt=fasta",
    "--guidetree-out", tree_output,
    "--force"
]


# Run Clustal Omega
subprocess.run(clustal_command)


# Print confirmation message
print("Sequence alignment completed")
print(f"FASTA file: {input_fasta}")
print(f"Aligned fasta file: {aligned_output}")
print(f"Guide tree file: {tree_output}")