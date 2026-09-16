import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. LOAD & CLEAN DATASET (Pandas)
# ---------------------------------------------------------
df = pd.read_csv("global_terrorism_2000_2017_subset.csv")

# Clean missing numerical values in Fatalities
df["nkill"] = df["nkill"].fillna(0)

# Filter for Asian / Middle Eastern regions
asian_regions = [
    'South Asia', 'Southeast Asia', 'East Asia',
    'Central Asia', 'Middle East & North Africa'
]
asia_df = df[df['region_txt'].isin(asian_regions)].copy()

# ---------------------------------------------------------
# 2. AGGREGATION & ANALYTICS (Pandas & NumPy)
# ---------------------------------------------------------
summary_df = asia_df.groupby('country_txt').agg(
    Total_Attacks=('iyear', 'count'),
    Total_Fatalities=('nkill', 'sum'),
    Suicide_Attacks=('suicide', 'sum'),
    Successful_Attacks=('success', 'sum')
).reset_index()

# Extract top 10 most impacted countries
top10_df = summary_df.sort_values(by='Total_Attacks', ascending=False).head(10)
top_asia_sorted = top10_df.sort_values(by='Total_Attacks', ascending=True)

# ---------------------------------------------------------
# 3. 2x2 DASHBOARD CREATION (Matplotlib OOA)
# ---------------------------------------------------------
fig, ax = plt.subplots(2, 2, figsize=(15, 11))
fig.suptitle("Asian Security & Conflict Dashboard (2000–2017 GTD Dataset)", fontsize=16, fontweight='bold')

# Plot 1: Total Incident Volume (Horizontal Bar Chart)
ax[0, 0].barh(top_asia_sorted['country_txt'], top_asia_sorted['Total_Attacks'], color='#1f77b4', edgecolor='black')
ax[0, 0].set_title("1. Total Attack Incidents", fontweight='bold')
ax[0, 0].set_xlabel("Incident Count")
ax[0, 0].grid(axis='x', linestyle='--', alpha=0.6)

# Plot 2: Total Fatalities Recorded (Horizontal Bar Chart)
top_fat_sorted = summary_df.sort_values(by='Total_Fatalities', ascending=True).tail(10)
ax[0, 1].barh(top_fat_sorted['country_txt'], top_fat_sorted['Total_Fatalities'], color='crimson', edgecolor='black')
ax[0, 1].set_title("2. Total Fatalities Recorded", fontweight='bold')
ax[0, 1].set_xlabel("Fatalities Count")
ax[0, 1].grid(axis='x', linestyle='--', alpha=0.6)

# Plot 3: Success vs. Failed Attacks (Grouped Bar Chart)
x = np.arange(len(top10_df['country_txt']))
width = 0.35
failed_attacks = top10_df['Total_Attacks'].to_numpy() - top10_df['Successful_Attacks'].to_numpy()

ax[1, 0].bar(x - width/2, top10_df['Successful_Attacks'], width, label='Successful', color='darkgreen')
ax[1, 0].bar(x + width/2, failed_attacks, width, label='Failed/Prevented', color='darkorange')
ax[1, 0].set_title("3. Attack Outcomes: Successful vs. Failed", fontweight='bold')
ax[1, 0].set_xticks(x)
ax[1, 0].set_xticklabels(top10_df['country_txt'], rotation=45, ha='right')
ax[1, 0].set_ylabel("Count")
ax[1, 0].legend()
ax[1, 0].grid(axis='y', linestyle='--', alpha=0.6)

# Plot 4: Suicide Tactics Frequency (Lollipop Plot)
ax[1, 1].scatter(top10_df['country_txt'], top10_df['Suicide_Attacks'], color='purple', s=120, zorder=3)
ax[1, 1].vlines(x=top10_df['country_txt'], ymin=0, ymax=top10_df['Suicide_Attacks'], color='purple', linewidth=1.5)
ax[1, 1].set_title("4. Total Suicide Incidents Executed", fontweight='bold')
ax[1, 1].set_xticks(x)
ax[1, 1].set_xticklabels(top10_df['country_txt'], rotation=45, ha='right')
ax[1, 1].set_ylabel("Count")
ax[1, 1].grid(axis='y', linestyle='--', alpha=0.6)

# ---------------------------------------------------------
# 4. EXPORT & DISPLAY
# ---------------------------------------------------------
plt.tight_layout()
plt.savefig("asian_conflict_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()