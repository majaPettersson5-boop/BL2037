#!/bin/bash

# Definiera sökvägar till de två olika filerna i examples-mappen
# (Justera sökvägen beroende på exakt var din 'examples'-mapp ligger)
IN1="../../examples/gene_expression.csv"
IN2="../../examples/gene_expression2.csv"

# Definiera var de två olika bilderna ska sparas
OUT1="../../results/lab4/hist_1.png"
OUT2="../../results/lab4/hist_2.png"

echo "Startar bearbetning av båda filerna samtidigt..."

# Kör första körningen i bakgrunden (&)
python lab4_1.py "$IN1" "$OUT1" &

# Kör andra körningen i bakgrunden (&)
python lab4_1.py "$IN2" "$OUT2" &

# 'wait' säger till bash-skriptet att inte avslutas förrän båda python-jobben är klara
wait

echo "Båda histogrammen har genererats!"