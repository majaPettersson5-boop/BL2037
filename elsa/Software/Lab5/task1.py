# Import modules
import subprocess
import re
import csv
# Reference protein, chain R
reference_file = "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/8JIQ_R.pdb"

# Target proteins, chain R
target_files = [
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/8E3Y_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/6WI9_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/6X18_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/7VQX_R.pdb",
    "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab5/7YON_R.pdb"
]
# Function to extract TM-score and RMSD from TMalign output
def parse_tmalign_output(output_text):
    tm_match = re.search(r"TM-score\s*=\s*(\d\.\d+)", output_text)
    rmsd_match = re.search(r"RMSD\s*=\s*(\d\.\d+)", output_text)

    tm_score = tm_match.group(1) if tm_match else "NA"
    rmsd = rmsd_match.group(1) if rmsd_match else "NA"

    return tm_score, rmsd
results = []
# Run TM-align for each target protein
for target_file in target_files:

    pdb_id = target_file.split("/")[-1].replace("_R.pdb", "")

    output_prefix = "/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Results/Lab5/" + pdb_id + "_alignment"

    command = [
        "TMalign",
        reference_file,
        target_file,
        "-o",
        output_prefix
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    tm_score, rmsd = parse_tmalign_output(result.stdout)

    results.append([pdb_id, tm_score, rmsd])

    print(f"{pdb_id}: TM-score = {tm_score}, RMSD = {rmsd}")
# Save results to csv file
with open("/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Results/Lab5/tmalign_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["PDB_ID", "TM_score", "RMSD"])
    writer.writerows(results)
print("Results saved to Results/Lab5/tmalign_results.csv")