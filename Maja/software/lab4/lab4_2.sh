#!/bin/bash

# 1. Definiera variabler för sökvägarna
# Eftersom vi kör skriptet inifrån software/lab4 måste vi backa (../..) 
# för att nå data- och results-mapparna.
INPUT_FILE="../../data/lab3/gene_expression.csv"
OUTPUT_FILE="../../results/lab4/hist.png"

# 2. Kör python-skriptet med variablerna som argument
echo "Startar lab4_1.py..."
python lab4_1.py "$INPUT_FILE" "$OUTPUT_FILE"

echo "Bash-skriptet är klart!"