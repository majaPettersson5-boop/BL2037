#!/bin/bash

# --- 1. INSTÄLLNINGAR ---
SEARCH_WORD="Apollo"
RESULT_DIR="../../../results/lab1/core_task1"
OUTPUT_CSV="../../../results/lab1/core_task1/word_occurrence_report.csv"

# Skapa headern i CSV-filen (skriver över gammal fil om den finns)
echo "Date,Word,Count" > "$OUTPUT_CSV"

echo "Analyserar filer i $RESULT_DIR..."

# --- 2. LOOPEN ---
for file in "$RESULT_DIR"/del_*.txt; do
    if [ -f "$file" ]; then
        
        # Hämta datumet från första raden (ta bort # och mellanslag)
        # 'head -n 1' läser första raden, 'tr' städar bort tecken
        date_label=$(head -n 1 "$file" | tr -d '# ' )
        
        # Räkna ordet (case-insensitive)
        count=$(grep -ci "$SEARCH_WORD" "$file")
        
        # Skriv ut i terminalen så du ser att det händer nåt
        filename=$(basename "$file")
        echo "Hittade $count stycken $SEARCH_WORD i $filename"
        
        # Spara till CSV-filen i rätt format: Date,Word,Count
        echo "$date_label,$SEARCH_WORD,$count" >> "$OUTPUT_CSV"
    fi
done

echo "------------------------------------------"
echo "Klar! Resultatet har sparats i: $OUTPUT_CSV"
