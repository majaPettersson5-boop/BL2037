import pandas as pd
import matplotlib.pyplot as plt
import os

# --- INSTÄLLNINGAR ---
input_path = '../../../data/lab3/gene_expression.csv'
output_path = '../../../results/lab3/hist.png'

# --- STEG 1: LADDA DATA ---
try:
    df = pd.read_csv(input_path)
    print("✅ Filen hittades och laddades in!")
    
    # --- STEG 2: SKAPA HISTOGRAM ---
    plt.figure(figsize=(10, 6))
    plt.hist(df['expression_level'], bins=10, color='skyblue', edgecolor='black')

    # --- STEG 3: TITEL OCH ETIKETTER ---
    plt.title('Gene Expression Distribution')
    plt.xlabel('expression_level')
    plt.ylabel('Frequency')

    # --- STEG 4: SPARA BILDEN ---
    # Kontrollera att mappen finns, annars skapa den
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path, dpi=600)
    print(f"✅ Grafen har sparats i: {output_path}")

except FileNotFoundError:
    print(f"❌ Fel: Kunde inte hitta filen på {input_path}")
    print("Kontrollera att du står i rätt mapp i terminalen!")
except Exception as e:
    print(f"❌ Ett oväntat fel uppstod: {e}")