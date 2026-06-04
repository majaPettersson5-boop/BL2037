#!/bin/bash

echo "Startar parallella analyser..."

# Kör analys för fil 1
python software/lab4/lab4_1.py \
    --input_csv ./data/lab3/gene_expression.csv \
    --output_dir ./results/lab4/hist_1.png &

# Kör analys för fil 2
python software/lab4/lab4_1.py \
    --input_csv ./data/lab3/gene_expression2.csv \
    --output_dir ./results/lab4/hist_2.png &

# Vänta på att båda bakgrundsprocesserna ska bli klara
wait

echo "Båda histogrammen är klara!"