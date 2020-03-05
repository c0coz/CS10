import pandas as pd

NegCount = 0
PosCount = 0
NeuCount = 0
df = pd.read_csv('SetData.csv', sep=',', usecols=[2])
for x in df.values:
    if "Negitive" in x:
        NegCount = NegCount + 1
    elif "Positive" in x:
        PosCount = PosCount + 1
    elif "Netural" in x:
        NeuCount = NeuCount + 1

print("Negitive: " + str(NegCount))
print("Positive: " + str(PosCount))
print("Netural: " + str(NeuCount))