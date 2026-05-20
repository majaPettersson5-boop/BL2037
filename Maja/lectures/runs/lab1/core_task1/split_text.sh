#!/bin/bash

# 1. Inställningar (Sökvägar)
INPUT="../../../Data/lab1/core_task1/text_file.txt"
OUT_DIR="../../../results/lab1/core_task1"
count=0

# 2. Skapa resultatmappen om den inte finns
mkdir -p "$OUT_DIR"

# 3. Läs filen rad för rad
while IFS= read -r line; do
    # Om raden börjar med #
    if [[ $line == "#"* ]]; then
        # Öka numret för den nya filen
        count=$((count + 1))
        # Skapa ett snyggt filnamn (t.ex. del_01.txt)
        current_file="$OUT_DIR/deal_$(printf "%02d" $count).txt"
    fi

    # Skriv raden till den aktuella filen (om vi har hittat ett # än)
    if [ $count -gt 0 ]; then
        echo "$line" >> "$current_file"
    fi
done < "$INPUT"
