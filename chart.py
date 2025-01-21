import matplotlib.pyplot as plt
import pandas as pd

# Data
df = pd.read_csv('bit_position_impact.csv')
# Convert error_ratio from percentage string to float
df['error_ratio'] = df['error_ratio'].str.rstrip('%').astype(float)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df["bit_position"], df["error_ratio"], color="#DAF7A6", edgecolor="black")

# Add value annotations on bars
for bar, ratio in zip(bars, df["error_ratio"]):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.001,  # Offset to place above the bar
        f"{ratio:.4f}%",
        ha="center",
        fontsize=10,
    )

# Customize Chart
plt.xlabel("Bit Position", fontsize=14)
plt.ylabel("Error Ratio (%)", fontsize=14)
plt.title("Impact of Bit Position on Error Ratio", fontsize=16)
plt.xticks(df["bit_position"], fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0, 0.5)  # Set y-axis maximum to 1% for consistency
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save with high resolution
plt.savefig("bit_position_impact_chart_consistent.png", dpi=300)
plt.show()
