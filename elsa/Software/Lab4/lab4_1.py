import argparse
import pandas as pd
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()

parser.add_argument("input_csv", help="Path to the input CSV file")
parser.add_argument("output_png", help="Path to the output PNG file")

args = parser.parse_args()
# Ladda data
input_path = args.input_csv
df = pd.read_csv(input_path, sep=None, engine="python")
# Skapa histogram
plt.figure()
plt.hist(df['expression_level'])

plt.title("Gene Expression Distribution")
plt.xlabel("expression_level")
plt.ylabel("Frequency")
# Spara bilden
output_path = args.output_png
plt.savefig(output_path, dpi=600)
#plt.show()