import pandas as pd

# --- STEG 1: LADDA DATA ---
# Vi backar 3 steg: core_task2 -> lab3 -> software -> huvudmapp
# Sen går vi in i data -> lab3
try:
    input_path = '../../../data/lab3/gene_expression.csv'
    df = pd.read_csv(input_path)
    
    # --- STEG 2: STATISTISK ANALYS ---
    print("--- Summary Statistics ---")
    # describe() ger oss count, mean, std, min, 25%, 50%, 75%, max
    print(df.describe())

    # --- STEG 3: FILTRERING ---
    # Vi skapar en ny DataFrame med endast gener där TPM > 100
    filtered_df = df[df['TPM'] > 100]
    
    print("\n--- Genes with TPM > 100 ---")
    print(filtered_df)

    # --- STEG 4: SPARA RESULTATET ---
    # Vi sparar den filtrerade listan som en ny CSV-fil
    # Sökvägen går till din resultat/lab3 mapp
    output_path = '../../../results/lab3/filtered_results.csv'
    filtered_df.to_csv(output_path, index=False)
    
    print(f"\n✅ Klart! Resultatet har sparats i: {output_path}")

except FileNotFoundError:
    print("❌ Fel: Kunde inte hitta filen. Kontrollera att dina mappar ligger där de ska!")
except Exception as e:
    print(f"❌ Ett oväntat fel uppstod: {e}")