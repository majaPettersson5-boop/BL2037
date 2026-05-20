#!/bin/bash

# --- INSTÄLLNINGAR ---
# Eftersom allt ligger i samma mapp använder vi "." för att säga "denna mapp"
data_dir="." 
order_file="./order.txt"
python_script="./read_pdb_argparsed.py"

# --- KÖR PROCESSEN ---
echo "Startar processen baserat på ordningen i $order_file..."

# 1. Kontrollera att order.txt finns
if [ ! -f "$order_file" ]; then
    echo "❌ Fel: Hittade inte filen $order_file i denna mapp."
    exit 1
fi

# 2. Läs order.txt rad för rad
while IFS= read -r filename || [ -n "$filename" ]; do
    # Ta bort eventuella osynliga tecken (som Windows-radbrytningar) och hoppa över tomma rader
    filename=$(echo "$filename" | tr -d '\r' | xargs)
    [ -z "$filename" ] && continue
    
    # Skapa den fullständiga sökvägen till PDB-filen
    full_path="$data_dir/$filename"
    
    # 3. Kontrollera om PDB-filen faktiskt finns
    if [ -f "$full_path" ]; then
        echo "--------------------------------------------------"
        echo "Processing PDB file: $filename"
        # Kör python-skriptet med filen som argument
        python "$python_script" "$full_path"
    else
        echo "⚠️  Varning: Hittade inte filen '$filename' i mappen, hoppar över..."
    fi

done < "$order_file"

echo "--------------------------------------------------"
echo "Klart! Alla listade filer har processats."