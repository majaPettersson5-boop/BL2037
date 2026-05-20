import os

# --- SÖKVÄGAR ---
# Vi utgår från att du står i: software/lab3/extra_tasks/
# 1. Indata: Backa 3 steg till huvudmapp, sen data/lab3/
input_path = '../../../data/lab3/raw_sequences.txt'

# 2. Utdata: Backa 3 steg till huvudmapp, sen results/lab3/
output_path = '../../../results/lab3/clean_sequences.txt'

# --- KÖR PROCESSEN ---
try:
    # Kontrollera att mappen vi ska spara i faktiskt finns
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 1. Öppna raw_sequences.txt i Read mode ('r')
    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    # 2. Öppna clean_sequences.txt i Write mode ('w') i results-mappen
    with open(output_path, 'w') as outfile:
        for line in lines:
            sequence = line.strip()
            if sequence:
                outfile.write(f"Processed: {sequence}\n")
    
    print(f"✅ Succé!")
    print(f"Hämtade från: {input_path}")
    print(f"Sparade till:  {output_path}")

except FileNotFoundError:
    print(f"❌ Fel: Hittade inte filen på {input_path}")
except Exception as e:
    print(f"❌ Ett fel uppstod: {e}")