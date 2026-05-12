import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def main():
    # 1. Hantera argument från kommandoraden
    parser = argparse.ArgumentParser(description="Skapar ett histogram från genuttrycksdata.")
    parser.add_argument("input_csv", help="Sökväg till indata-filen (CSV)")
    parser.add_argument("output_png", help="Sökväg där bilden ska sparas (PNG)")

    args = parser.parse_args()

    # Skapa utdatamappen om den saknas
    output_dir = os.path.dirname(args.output_png)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # 2. Ladda datan med automatisk avkänning av separator (komma, semikolon, etc.)
        # sep=None gör att pandas gissar separatorn själv
        print(f"Analyserar och läser: {args.input_csv}")
        df = pd.read_csv(args.input_csv, sep=None, engine='python')

        # 3. Definiera den kolumn vi letar efter
        target_column = 'expression_level'

        if target_column in df.columns:
            # 4. Skapa histogrammet
            plt.figure(figsize=(10, 6))
            plt.hist(df[target_column], bins=25, color='teal', edgecolor='black')
            
            plt.title(f'Gene Expression Distribution ({os.path.basename(args.input_csv)})')
            plt.xlabel('Expression Level')
            plt.ylabel('Frequency')

            # 5. Spara bilden
            plt.savefig(args.output_png)
            plt.close()
            print(f"✅ Klart! Sparade histogram till: {args.output_png}")
        else:
            print(f"❌ Fel: Kunde inte hitta kolumnen '{target_column}'.")
            print(f"Tillgängliga kolumner i filen är: {list(df.columns)}")

    except Exception as e:
        print(f"❌ Ett oväntat fel uppstod vid körning av {args.input_csv}:")
        print(f"   {e}")

if __name__ == "__main__":
    main()