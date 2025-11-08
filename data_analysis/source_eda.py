import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

sns.set_theme(style="whitegrid", context="talk")

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT.parent / "all_combined_extracted_data_with_source_counts.xlsx"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FIG_KWARGS = dict(dpi=350, bbox_inches="tight")

def save_figure(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUTPUT_DIR / filename, **FIG_KWARGS)
    plt.close(fig)

def main() -> None:
    df = pd.read_excel(DATA_FILE)
    df.columns = [c.strip() for c in df.columns]
    df = df.dropna(subset=["source_id"]).copy()

    numeric_year = pd.to_numeric(df["source_publication_year"], errors="coerce")
    df["source_publication_year"] = numeric_year.astype("Int64")

    sources = (
        df.groupby("source_id")
        .agg(
            evidence_count=("evidence_id", "count"),
            source_title=("source_title", "first"),
            source_type=("source_type", "first"),
            publication_year=("source_publication_year", "first"),
            journal=("source_journal", "first"),
            evidence_types=("evidence_type", lambda x: ", ".join(sorted(x.dropna().unique()))),
        )
        .sort_values("evidence_count", ascending=False)
    )

    total_sources = sources.shape[0]
    total_evidence = int(sources["evidence_count"].sum())

    summary = {
        "total_sources": total_sources,
        "total_evidence_items": total_evidence,
        "median_evidence_per_source": float(sources["evidence_count"].median()),
        "mean_evidence_per_source": float(sources["evidence_count"].mean()),
        "p90_evidence_per_source": float(sources["evidence_count"].quantile(0.9)),
        "max_evidence_per_source": int(sources["evidence_count"].max()),
        "top1_share_percent": float(sources["evidence_count"].iloc[0] / total_evidence * 100),
        "top10_share_percent": float(sources["evidence_count"].head(10).sum() / total_evidence * 100),
        "top100_share_percent": float(sources["evidence_count"].head(100).sum() / total_evidence * 100),
    }
    pd.DataFrame([summary]).to_csv(OUTPUT_DIR / "source_contribution_summary.csv", index=False)

    sources_with_share = sources.assign(
        evidence_share_percent=lambda x: (x["evidence_count"] / total_evidence) * 100
    )
    sources_with_share.reset_index().to_csv(
        OUTPUT_DIR / "source_counts_detailed.csv", index=False
    )

    # Histogram of evidence items per source
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.histplot(
        data=sources,
        x="evidence_count",
        bins=40,
        ax=ax,
        color="#4C72B0",
    )
    ax.set_xscale("log")
    ax.set_xlabel("Evidence Items per Source (log scale)")
    ax.set_ylabel("Number of Sources")
    ax.set_title("Distribution of Evidence Contributions per Source")
    ax.grid(True, which="both", axis="x", linestyle="--", alpha=0.4)
    save_figure(fig, "hist_evidence_per_source.png")

    # Cumulative coverage plot
    counts_sorted = sources["evidence_count"].to_numpy()
    cumsum_evidence = np.cumsum(counts_sorted)
    cumulative_evidence = cumsum_evidence / total_evidence
    cumulative_sources = np.arange(1, total_sources + 1) / total_sources

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.plot(
        cumulative_sources * 100,
        cumulative_evidence * 100,
        color="#1B9E77",
        linewidth=2.5,
        label="Cumulative evidence coverage",
    )
    ax.fill_between(
        cumulative_sources * 100,
        cumulative_evidence * 100,
        color="#1B9E77",
        alpha=0.2,
    )
    ax.axline((0, 0), slope=1, color="gray", linestyle="--", linewidth=1)
    ax.set_xlabel("Percent of sources (sorted by evidence volume)")
    ax.set_ylabel("Percent of evidence items covered")
    ax.set_title("Pareto Coverage of Evidence by Source")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.legend()
    save_figure(fig, "cumulative_evidence_coverage.png")

    # Top sources by evidence type composition
    top_n = 20
    top_source_ids = sources.head(top_n).index
    top_df = df[df["source_id"].isin(top_source_ids)].copy()
    type_counts = (
        top_df.groupby(["source_id", "evidence_type"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    type_counts = type_counts.loc[top_source_ids]
    type_counts.to_csv(OUTPUT_DIR / "top_sources_evidence_type_counts.csv")

    fig, ax = plt.subplots(figsize=(15, 10))
    bottom = np.zeros(len(type_counts))
    y_pos = np.arange(len(type_counts))
    type_order = ["PREDICTIVE", "DIAGNOSTIC", "PROGNOSTIC", "PREDISPOSING", "ONCOGENIC", "FUNCTIONAL"]
    palette = sns.color_palette("Set2", len(type_order))
    for idx, ev_type in enumerate(type_order):
        values = type_counts.get(ev_type, 0).values
        ax.barh(
            y_pos,
            values,
            left=bottom,
            label=ev_type,
            color=palette[idx],
        )
        bottom += values
    labels = [f"{sources.loc[s_id, 'source_title'][:60]}…" if len(str(sources.loc[s_id, 'source_title'])) > 60 else str(sources.loc[s_id, 'source_title']) for s_id in top_source_ids]
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Evidence Items")
    ax.set_title("Top Sources by Evidence Volume and Type Composition")
    ax.legend(title="Evidence Type", bbox_to_anchor=(1.02, 1), loc="upper left")
    save_figure(fig, "stackedbar_top_sources_by_type.png")

    # Evidence level mix per top sources (heatmap)
    level_counts = (
        top_df.groupby(["source_id", "evidence_level"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    level_counts = level_counts.loc[top_source_ids]
    level_counts = level_counts[[c for c in ["A", "B", "C", "D", "E"] if c in level_counts.columns]]
    level_counts.to_csv(OUTPUT_DIR / "top_sources_evidence_level_counts.csv")

    level_pct = level_counts.div(level_counts.sum(axis=1), axis=0) * 100
    fig, ax = plt.subplots(figsize=(12, 9))
    sns.heatmap(
        level_pct,
        annot=True,
        fmt=".1f",
        cmap="YlGnBu",
        ax=ax,
        cbar_kws={"label": "Percent within source"},
    )
    ax.set_xlabel("Evidence Level")
    ax.set_ylabel("Source (top 20)")
    ax.set_title("Evidence Level Mix for Most Prolific Sources")
    save_figure(fig, "heatmap_top_sources_by_level.png")

    # Source productivity by publication year
    year_counts = (
        df.dropna(subset=["source_publication_year"])
        .groupby("source_publication_year")
        .agg(
            sources=("source_id", "nunique"),
            evidence_items=("evidence_id", "count"),
        )
        .reset_index()
        .sort_values("source_publication_year")
    )
    year_counts.to_csv(OUTPUT_DIR / "sources_by_publication_year.csv", index=False)

    fig, ax1 = plt.subplots(figsize=(12, 7))
    ax1.plot(
        year_counts["source_publication_year"],
        year_counts["evidence_items"],
        color="#4C72B0",
        marker="o",
        label="Evidence items",
    )
    ax1.set_xlabel("Publication Year")
    ax1.set_ylabel("Evidence Items", color="#4C72B0")
    ax1.tick_params(axis="y", labelcolor="#4C72B0")

    ax2 = ax1.twinx()
    ax2.bar(
        year_counts["source_publication_year"],
        year_counts["sources"],
        color="#DD8452",
        alpha=0.3,
        label="Unique sources",
    )
    ax2.set_ylabel("Unique Sources", color="#DD8452")
    ax2.tick_params(axis="y", labelcolor="#DD8452")

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc="upper left")
    ax1.set_title("Evidence Production by Publication Year")
    save_figure(fig, "dualaxis_sources_by_year.png")

if __name__ == "__main__":
    main()
