import pandas as pd
import matplotlib.pyplot as plt
# Ladda data
input_path = '/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Data/Lab3/gene_expression.csv'
df = pd.read_csv(input_path)
# Skapa histogram
plt.figure()
plt.hist(df['expression_level'])

plt.title("Gene Expression Distribution")
plt.xlabel("expression_level")
plt.ylabel("Frequency")
# Spara bilden
output_path = '/mnt/c/Users/Thinkpad/OneDrive/Universitetet/Programmering/BL2037/elsa/Results/Lab3/hist.png'
plt.savefig(output_path, dpi=600)
#plt.show()