#!/bin/bash

for file in ./Examples/gene_expression*.csv
do
    name=$(basename "$file" .csv)

    python ./Software/Lab4/lab4_1.py \
    "$file" \
    "./Results/Lab4/${name}_hist.png"

done
echo "Histograms saved to ./Results/Lab4/"