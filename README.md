# 📊 Matplotlib Mastery & Asian Security Dashboard (2000–2017)

This repository contains my complete hands-on learning project for **Matplotlib**, combined with **Pandas** and **NumPy** for real-world data processing. 

It includes both my curriculum learning milestones and an end-to-end data analytics dashboard analyzing over 111,000 incident records from the **Global Terrorism Database (GTD)**.

---

## 📚 Curriculum & Topics Mastered

| Topic | Key Concepts Learned |
| :--- | :--- |
| **Introduction to Data Visualisation** | Principles of graphical communication, selecting plot types based on continuous vs. discrete variables. |
| **Introduction to Matplotlib** | Library setup, Matplotlib environment architecture, integration with Pandas & NumPy arrays. |
| **Terms You Should Know** | Anatomy of a plot: `Figure`, `Axes`, `Axis`, `Ticks`, `Spines`, `Grid`, and `Legend`. |
| **Understanding Pyplot** | State-based plotting syntax via `import matplotlib.pyplot as plt`. |
| **Pyplot Functions** | Manipulating active figures using `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.xlim()`, `plt.ylim()`, `plt.xticks()`. |
| **Core Chart Types** | Building Bar Charts (`plt.bar`/`plt.barh`), Pie Charts (`plt.pie` with `autopct`), Histograms (`plt.hist`), and Scatter Plots (`plt.scatter`). |
| **Subplots & Layout Adjustments** | Object-Oriented Approach (OOA) with `fig, ax = plt.subplots(r, c)`, 2D grid indexing, label rotation, and `tight_layout()`. |
| **Saving Figures** | Exporting figures to `.png`, `.jpg`, and `.pdf` formats using `plt.savefig()` with resolution control (`dpi=300`). |

---

## 🎯 Capstone Project: Asian Conflict & Security Dashboard

Using the concepts learned above, I built a 4-panel dashboard to analyze security trends across the top 10 most impacted Asian nations using raw GTD data.

### ⚙️ Data Pipeline & Architecture

1. **Data Ingestion & Cleaning (`Pandas`)**
   * Loaded raw dataset (`global_terrorism_2000_2017_subset.csv`) containing 111,855 rows.
   * Filtered regional targets for South Asia, Southeast Asia, East Asia, Central Asia, and MENA.
   * Cleaned missing numeric values in `nkill` (Fatalities) using zero-fill strategies.

2. **Numerical Processing & Analytics (`NumPy` & `Pandas`)**
   * Computed total incident counts, total fatalities, success/failure ratios, and suicide tactic counts.
   * Derived outcome vectors using NumPy array offsets (`np.arange()`) for grouped bar charts.

3. **Multi-Plot Object-Oriented Layout (`Matplotlib`)**
   * Created a 2x2 grid using `plt.subplots(2, 2, figsize=(15, 11))`.
   * **Plot 1:** Horizontal Bar Chart ranking total attack volumes.
   * **Plot 2:** Horizontal Bar Chart comparing total fatalities recorded.
   * **Plot 3:** Grouped Bar Chart contrasting successful vs. failed/prevented attacks.
   * **Plot 4:** Lollipop / Scatter plot illustrating total suicide attacks per country.

4. **Export Systems**
   * Exported publication-ready 300 DPI graphics before rendering using `plt.savefig("asian_conflict_dashboard.png", dpi=300, bbox_inches="tight")`.

---

## 🚀 Quickstart

### 1. Clone Repository
```bash
git clone [https://github.com/YOUR_USERNAME/matplotlib-mastery-asian-dashboard.git](https://github.com/YOUR_USERNAME/matplotlib-mastery-asian-dashboard.git)
cd matplotlib-mastery-asian-dashboard
