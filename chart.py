import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "bit_position": [0, 1, 2, 3, 4, 5, 6, 7],
    "samples": [12410, 12586, 12622, 12375, 12492, 12617, 12435, 12463],
    "errors": [4, 7, 5, 13, 8, 16, 20, 48],
    "error_ratio": [0.0322, 0.0556, 0.0396, 0.1051, 0.0640, 0.1268, 0.1608, 0.3851],
}
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(df["bit_position"], df["error_ratio"], color="steelblue", edgecolor="black")

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
plt.ylim(0, 1.0)  # Set y-axis maximum to 1% for consistency
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()

# Save with high resolution
plt.savefig("bit_position_impact_chart_consistent.png", dpi=300)
plt.show()
