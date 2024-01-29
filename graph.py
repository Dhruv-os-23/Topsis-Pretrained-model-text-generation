import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset from CSV
df = pd.read_csv('data.csv')

# Set the model names as the index
df.set_index('Model', inplace=True)

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
fig.suptitle('Model Performance Comparison')

# Perplexity (Lower is better, so we invert the y-axis)
df['Perplexity'].plot(ax=axes[0,0], kind='bar', color='skyblue', title='Perplexity (Lower is Better)')
axes[0,0].invert_yaxis()

# BLEU Score
df['BLEU Score'].plot(ax=axes[0,1], kind='bar', color='lightgreen', title='BLEU Score (Higher is Better)')

# Latency
df['Latency (s)'].plot(ax=axes[1,0], kind='bar', color='salmon', title='Latency (s) (Lower is Better)')
axes[1,0].invert_yaxis()

# ROUGE Score
df['ROUGE Score'].plot(ax=axes[1,1], kind='bar', color='orchid', title='ROUGE Score (Higher is Better)')


plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Save the plot as an image file
plt.savefig('model_performance_comparison.png', dpi=300)

# Optionally, display the plot as well
plt.show()
