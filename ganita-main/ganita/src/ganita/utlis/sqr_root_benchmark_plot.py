import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('benchmarking/square_root.csv')
df['Time'] = pd.to_numeric(df['Time'])
methods = df['Method'].unique()

plt.figure()
for method in methods:
    data = df[df['Method'] == method]
    plt.plot(data['Digits'], data['Time'], label=method)

plt.xlabel('# of Digits')
plt.ylabel('Time Elapsed')
plt.legend()
plt.show()