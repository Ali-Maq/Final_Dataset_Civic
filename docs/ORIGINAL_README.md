# CIViC Evidence Export – Clinically Oriented EDA

`run_eda.py` loads the bundled CIViC evidence extract (`../all_combined_extracted_data_from_civic.xlsx`), harmonises date and categorical fields, and generates a suite of research-grade figures and tables focused on questions that matter for downstream clinical interpretation:

- **Evidence quality** – heatmap of evidence level by evidence type, violin plot of trust ratings per level, curation latency histogram.
- **Clinical context** – clinical-significance profiles per evidence type, variant origin versus evidence type, temporal trajectory of submissions/acceptances.
- **Disease, therapy and gene landscapes** – stacked bar for top diseases, therapy usage stratified by interaction type, top curated genes.
- **Evidence concordance** – automatic detection of variant/disease contexts with conflicting clinical directions, plus a high-DPI bar chart spotlighting the most contested scenarios.

Outputs are written to `data_analysis/outputs/` (CSV summaries for further analysis and 350 dpi PNGs for publication-ready graphics). Re-run or update the analysis with:

```bash
cd data_analysis
python run_eda.py
```

For source-centric questions (e.g., how heavily individual publications contribute to the knowledgebase) use:

```bash
python source_eda.py
```

This script adds distribution plots, cumulative coverage curves, and top-source composition tables/heatmaps alongside year-by-year productivity summaries.

Dependencies: pandas, seaborn, matplotlib, numpy (all available in the project environment).
