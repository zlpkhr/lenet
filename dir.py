import pandas as pd

# Load the fault injection results
df_rand = pd.read_csv("results.csv")

# Group by flip direction and calculate samples, errors, and error ratio
flip_direction_table = (
    df_rand.groupby(["original_bit", "flipped_bit"])
    .agg(
        samples=("original_output", "count"),  # Total bit flips for each direction
        errors=(
            "original_output",
            lambda x: (x != df_rand.loc[x.index, "flipped_output"]).sum(),
        ),  # Total errors for each direction
    )
    .reset_index()
)

# Create a new column for flip direction as a string (e.g., "0 to 1", "1 to 0")
flip_direction_table["flip_direction"] = (
    flip_direction_table["original_bit"].astype(str)
    + " to "
    + flip_direction_table["flipped_bit"].astype(str)
)

# Calculate error ratio as a percentage and format
flip_direction_table["error_ratio"] = (
    (flip_direction_table["errors"] / flip_direction_table["samples"]) * 100
).round(4).astype(str) + "%"

# Drop the original_bit and flipped_bit columns for cleaner display
flip_direction_table = flip_direction_table[["flip_direction", "samples", "errors", "error_ratio"]]

# Save or display the results
flip_direction_table.to_csv("flip_direction_table.csv", index=False)
print("Flip direction table saved as 'flip_direction_table.csv'.")
