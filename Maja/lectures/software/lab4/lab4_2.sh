#!/bin/bash

# Definiera variabler för att göra det lättläst
INPUT="./data/lab3/gene_expression.csv"
OUTPUT="./results/lab4/hist.png"

echo "Startar analys av $INPUT..."

# Här använder vi de nya flaggorna --input_csv och --output_dir
python software/lab4/lab4_1.py --input_csv "$INPUT" --output_dir "$OUTPUT"

echo "Histogrammet har skapats i $OUTPUT"