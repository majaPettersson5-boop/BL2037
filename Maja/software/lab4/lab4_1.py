import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def main():
    # Skapa argument-hanteraren
    parser = argparse.ArgumentParser(description="Skapar ett histogram med keyword-argument (--flags).")

    # Genom att lägga till '--' framför namnet blir argumentet ett keyword-argument.
    # 'required=True' säkerställer att skriptet inte körs utan dessa.
    parser.add_argument("--input_csv", help="Sökväg till indata-filen (CSV)", required=True)
    parser.add_argument("--output_dir", help="Sökväg till resultatbilden (PNG)", required=True)

    args = parser.parse_args()

    # Skapa mappen för utdata om den inte finns
    output_folder = os.path.dirname(args.output_dir)
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        # Läs in data (med automatisk detektering av separator för att klara icke-standard filer)
        print(f"Läser in fil: {args.input_csv}")
        df = pd.read_csv(args.input_csv, sep=None, engine='python')

        target_column = 'expression_level'

        if target_column in df.columns:
            plt.figure(figsize=(10, 6))
            plt.hist(df[target_column], bins=25, color='teal', edgecolor='black')
            
            plt.title(f'Gene Expression Distribution: {os.path.basename(args.input_csv)}')
            plt.xlabel('Expression Level')
            plt.ylabel('Frequency')

            # Spara till sökvägen angiven i --output_dir
            plt.savefig(args.output_dir)
            plt.close()
            print(f"✅ Success! Bilden sparad som: {args.output_dir}")
        else:
            print(f"❌ Fel: Kolumnen '{target_column}' saknas.")

    except Exception as e:
        print(f"❌ Ett fel uppstod: {e}")

if __name__ == "__main__":
    main()