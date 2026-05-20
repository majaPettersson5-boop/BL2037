#!/bin/bash

# --- KONFIGURATION ---
TARGET_WORD="Apollo"
INPUT_DIR="../../../results/lab1/core_task1"

# 1. Skapa en variabel för summan (börja på noll)
TOTAL_COUNT=0

echo "Kör Core Task 2: Sökning pågår..."
echo "------------------------------------------------"

# --- SÖKNINGEN ---
for file in "$INPUT_DIR"/del_*.txt; do
    if [ -f "$file" ]; then
        
        # Räkna ord i den aktuella filen
        count=$(grep -ci "$TARGET_WORD" "$file")
        
        
        
        # 2. PLUSSA IHOP: Lägg till filens antal till den totala summan
        TOTAL_COUNT=$((TOTAL_COUNT + count))
        
        echo "Fil: $(basename "$file") | Datum: $current_date | Antal: $count"
    fi
done

# --- RESULTAT ---
echo "------------------------------------------------"
echo "TOTALT ANTAL FÖREKOMSTER AV '$TARGET_WORD': $TOTAL_COUNT"
echo "------------------------------------------------"



