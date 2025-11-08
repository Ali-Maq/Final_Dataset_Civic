import math
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

sns.set_theme(style="whitegrid", context="talk")

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT.parent / "all_combined_extracted_data_from_civic.xlsx"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FIG_KWARGS = dict(dpi=350, bbox_inches="tight")


def save_figure(fig: plt.Figure, filename: str) -> None:
    target = OUTPUT_DIR / filename
    fig.savefig(target, **FIG_KWARGS)
    plt.close(fig)


def main() -> None:
    df = pd.read_excel(DATA_FILE)

    # Normalize column names used repeatedly
    df.columns = [c.strip() for c in df.columns]

    date_cols = [
        "submission_date",
        "acceptance_date",
        "rejection_date",
        "last_submitted_revision_date",
        "last_accepted_revision_date",
        "last_comment_date",
    ]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce", utc=True)

    if "evidence_rating" in df.columns:
        df["evidence_rating"] = pd.to_numeric(df["evidence_rating"], errors="coerce")

    # ------------------------------------------------------------------
    # Evidence Level vs Type heatmap
    # ------------------------------------------------------------------
    level_order = ["A", "B", "C", "D", "E"]
    type_order = [
        "PREDICTIVE",
        "DIAGNOSTIC",
        "PROGNOSTIC",
        "PREDISPOSING",
        "ONCOGENIC",
        "FUNCTIONAL",
    ]

    level_type = (
        df.assign(
            evidence_level=lambda x: pd.Categorical(
                x["evidence_level"], categories=level_order, ordered=True
            ),
            evidence_type=lambda x: pd.Categorical(
                x["evidence_type"], categories=type_order, ordered=True
            ),
        )
        .groupby(["evidence_type", "evidence_level"], observed=True)
        .size()
        .unstack(fill_value=0)
    )

    level_type.to_csv(OUTPUT_DIR / "evidence_counts_by_type_level.csv")

    pct = level_type.div(level_type.sum(axis=1), axis=0) * 100
    annot = level_type.astype(int).astype(str) + "\n(" + pct.round(1).astype(str) + "%)"

    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(
        pct,
        ax=ax,
        cmap="viridis",
        annot=annot,
        fmt="",
        cbar_kws={"label": "Percent within evidence type"},
    )
    ax.set_xlabel("Evidence Level")
    ax.set_ylabel("Evidence Type")
    ax.set_title("Evidence Level Distribution by Evidence Type")
    save_figure(fig, "heatmap_evidence_type_vs_level.png")

    # ------------------------------------------------------------------
    # Evidence Ratings by Level
    # ------------------------------------------------------------------
    rating_df = df.dropna(subset=["evidence_rating", "evidence_level"]).copy()
    rating_df = rating_df[rating_df["evidence_level"].isin(level_order)]
    rating_df["evidence_level"] = pd.Categorical(
        rating_df["evidence_level"], categories=level_order, ordered=True
    )

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.violinplot(
        data=rating_df,
        x="evidence_level",
        y="evidence_rating",
        inner="quartile",
        ax=ax,
        order=level_order,
        cut=0,
        color="#4C72B0",
    )
    sns.pointplot(
        data=rating_df,
        x="evidence_level",
        y="evidence_rating",
        estimator=np.median,
        errorbar=None,
        color="black",
        markers="D",
        markersize=8,
        ax=ax,
    )
    ax.set_xlabel("Evidence Level")
    ax.set_ylabel("Evidence Rating (Stars)")
    ax.set_title("Evidence Quality (Rating) Across Study Levels")
    ax.set_ylim(0.8, 5.2)
    save_figure(fig, "violin_rating_by_level.png")

    # ------------------------------------------------------------------
    # Evidence Significance profiles by type
    # ------------------------------------------------------------------
    sig_df = df.dropna(subset=["evidence_significance", "evidence_type"]).copy()
    sig_counts = (
        sig_df.groupby(["evidence_type", "evidence_significance"], observed=True)
        .size()
        .reset_index(name="count")
    )
    sig_counts["fraction"] = (
        sig_counts.groupby("evidence_type")["count"].transform(lambda x: x / x.sum())
    )

    sig_order = sorted(sig_counts["evidence_significance"].unique())
    g = sns.catplot(
        data=sig_counts,
        x="fraction",
        y="evidence_significance",
        col="evidence_type",
        kind="bar",
        order=sig_order,
        hue="evidence_significance",
        hue_order=sig_order,
        legend=False,
        col_wrap=3,
        height=4.5,
        aspect=1.2,
        palette="crest",
        sharex=False,
    )
    g.set_xlabels("Fraction within evidence type")
    g.set_ylabels("Clinical Significance")
    g.set_titles("{col_name}")
    percent_formatter = FuncFormatter(lambda val, pos: f"{val:.0%}")
    for ax in g.axes.flatten():
        if ax is not None:
            ax.xaxis.set_major_formatter(percent_formatter)
    g.figure.suptitle("Clinical Significance Profile by Evidence Type", y=1.04)
    g.figure.set_size_inches(16, 12)
    g.figure.savefig(OUTPUT_DIR / "significance_profiles_by_type.png", **FIG_KWARGS)
    plt.close(g.figure)

    sig_counts.sort_values(["evidence_type", "count"], ascending=[True, False]).to_csv(
        OUTPUT_DIR / "significance_counts_by_type.csv", index=False
    )

    # ------------------------------------------------------------------
    # Variant Origin vs Evidence Type heatmap
    # ------------------------------------------------------------------
    origin_df = df.copy()
    origin_df["variant_origin"] = origin_df["variant_origin"].fillna("UNKNOWN/NA")
    origin_order = [
        "SOMATIC",
        "RARE_GERMLINE",
        "COMMON_GERMLINE",
        "COMBINED",
        "MIXED",
        "UNKNOWN",
        "UNKNOWN/NA",
    ]
    origin_counts = (
        origin_df.assign(
            variant_origin=lambda x: pd.Categorical(
                x["variant_origin"], categories=origin_order, ordered=True
            ),
            evidence_type=lambda x: pd.Categorical(
                x["evidence_type"], categories=type_order, ordered=True
            ),
        )
        .groupby(["variant_origin", "evidence_type"], observed=True)
        .size()
        .unstack(fill_value=0)
    )
    origin_counts.to_csv(OUTPUT_DIR / "variant_origin_by_type.csv")

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.heatmap(
        origin_counts,
        ax=ax,
        cmap="mako",
        annot=True,
        fmt=",",
        cbar_kws={"label": "Evidence count"},
    )
    ax.set_xlabel("Evidence Type")
    ax.set_ylabel("Variant Origin")
    ax.set_title("Variant Origin Usage Across Evidence Types")
    save_figure(fig, "heatmap_variant_origin_vs_type.png")

    # ------------------------------------------------------------------
    # Top diseases by evidence volume (stacked bar by type)
    # ------------------------------------------------------------------
    top_diseases = (
        df["disease_name"].value_counts().head(15).index.tolist()
    )
    disease_subset = df[df["disease_name"].isin(top_diseases)].copy()
    disease_counts = (
        disease_subset.groupby(["disease_name", "evidence_type"], observed=True)
        .size()
        .reset_index(name="count")
    )
    disease_pivot = disease_counts.pivot(
        index="disease_name", columns="evidence_type", values="count"
    ).fillna(0)
    disease_pivot = disease_pivot.loc[
        disease_subset["disease_name"].value_counts().index
    ]
    disease_pivot.to_csv(OUTPUT_DIR / "top_disease_counts_by_type.csv")

    disease_pivot_plot = disease_pivot[type_order].fillna(0)
    fig, ax = plt.subplots(figsize=(14, 10))
    bottom = np.zeros(len(disease_pivot_plot))
    y_pos = np.arange(len(disease_pivot_plot))
    for evidence_type in type_order:
        values = disease_pivot_plot.get(evidence_type, 0).values
        ax.barh(
            y_pos,
            values,
            left=bottom,
            label=evidence_type,
        )
        bottom += values
    ax.set_yticks(y_pos)
    ax.set_yticklabels(disease_pivot_plot.index)
    ax.invert_yaxis()
    ax.set_xlabel("Number of Evidence Items")
    ax.set_title("Top Diseases by Evidence Volume and Type")
    ax.legend(title="Evidence Type", bbox_to_anchor=(1.02, 1), loc="upper left")
    save_figure(fig, "stackedbar_top_diseases.png")

    # ------------------------------------------------------------------
    # Therapy landscape
    # ------------------------------------------------------------------
    therapy_cols = ["therapy_names", "therapy_ids", "therapy_interaction_type", "evidence_type"]
    therapy_df = df.dropna(subset=["therapy_names"])[therapy_cols].copy()
    therapy_df["therapy_interaction_type"] = therapy_df["therapy_interaction_type"].fillna(
        "SINGLE_AGENT"
    )
    therapy_df["therapy_names"] = therapy_df["therapy_names"].str.split("|")
    therapy_long = therapy_df.explode("therapy_names")
    therapy_long["therapy_names"] = therapy_long["therapy_names"].str.strip()
    therapy_long["therapy_interaction_type"] = therapy_long["therapy_interaction_type"].replace(
        {
            "SINGLE_AGENT": "Single Agent",
            "COMBINATION": "Combination",
            "SEQUENTIAL": "Sequential",
            "SUBSTITUTES": "Substitutes",
        }
    )

    therapy_counts = (
        therapy_long.groupby(["therapy_names", "therapy_interaction_type"], observed=True)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )
    therapy_counts.to_csv(OUTPUT_DIR / "therapy_counts_by_interaction.csv", index=False)

    therapy_totals = (
        therapy_counts.groupby("therapy_names")["count"].sum().sort_values(ascending=False)
    )
    top_order = therapy_totals.head(15).index.tolist()
    top_therapy_df = therapy_long[therapy_long["therapy_names"].isin(top_order)]
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.countplot(
        data=top_therapy_df,
        y="therapy_names",
        hue="therapy_interaction_type",
        order=top_order,
        ax=ax,
    )
    ax.set_xlabel("Number of Evidence Items")
    ax.set_ylabel("Therapy")
    ax.set_title("Most Curated Therapies and Interaction Context")
    ax.legend(title="Interaction Type", bbox_to_anchor=(1.02, 1), loc="upper left")
    save_figure(fig, "bar_top_therapies.png")

    # ------------------------------------------------------------------
    # Gene landscape
    # ------------------------------------------------------------------
    gene_counts = df["feature_names"].dropna().value_counts().head(20)
    gene_counts.to_csv(OUTPUT_DIR / "top_genes.csv")

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(
        x=gene_counts.values,
        y=gene_counts.index,
        color=sns.color_palette("rocket")[2],
        ax=ax,
    )
    ax.set_xlabel("Number of Evidence Items")
    ax.set_ylabel("Gene")
    ax.set_title("Top Genes by Curated Evidence Volume")
    save_figure(fig, "bar_top_genes.png")

    # ------------------------------------------------------------------
    # Temporal dynamics of submissions and acceptances
    # ------------------------------------------------------------------
    timeline_df = df.dropna(subset=["submission_date"]).copy()
    timeline_df["submission_date"] = timeline_df["submission_date"].dt.tz_localize(None)

    submission_counts = (
        timeline_df.set_index("submission_date").resample("QE")
        .size()
        .rename("submissions")
    )
    acceptance_counts = (
        df.dropna(subset=["acceptance_date"])
        .assign(acceptance_date=lambda x: x["acceptance_date"].dt.tz_localize(None))
        .set_index("acceptance_date")
        .resample("QE")
        .size()
        .rename("acceptances")
    )

    timeline = pd.concat([submission_counts, acceptance_counts], axis=1).fillna(0)
    timeline.to_csv(OUTPUT_DIR / "timeline_submissions_acceptances_qtr.csv")

    fig, ax = plt.subplots(figsize=(14, 6))
    if isinstance(timeline.index, pd.PeriodIndex):
        timeline.index = timeline.index.to_timestamp()
    ax.plot(timeline.index, timeline["submissions"], label="Submissions", linewidth=2.5)
    ax.plot(timeline.index, timeline["acceptances"], label="Acceptances", linewidth=2.5)
    ax.fill_between(
        timeline.index,
        timeline["submissions"],
        timeline["acceptances"],
        where=timeline["submissions"] >= timeline["acceptances"],
        color="steelblue",
        alpha=0.2,
    )
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Evidence Items")
    ax.set_title("CIViC Evidence Submission and Acceptance Tempo")
    ax.legend()
    ax.grid(True, which="major", axis="y")
    save_figure(fig, "line_submission_acceptance_timeline.png")

    # ------------------------------------------------------------------
    # Curation latency (acceptance minus submission)
    # ------------------------------------------------------------------
    latency_df = df.dropna(subset=["submission_date", "acceptance_date"]).copy()
    latency_df["submission_date"] = latency_df["submission_date"].dt.tz_convert("UTC")
    latency_df["acceptance_date"] = latency_df["acceptance_date"].dt.tz_convert("UTC")
    latency_df["curation_latency_days"] = (
        (latency_df["acceptance_date"] - latency_df["submission_date"])
        .dt.total_seconds()
        .div(86400)
    )
    latency_df = latency_df[(latency_df["curation_latency_days"].notna()) & (latency_df["curation_latency_days"] >= 0)]

    latency_summary = {
        "count": int(latency_df.shape[0]),
        "median_days": float(latency_df["curation_latency_days"].median()),
        "iqr_days": float(latency_df["curation_latency_days"].quantile(0.75) - latency_df["curation_latency_days"].quantile(0.25)),
        "p90_days": float(latency_df["curation_latency_days"].quantile(0.90)),
    }
    pd.DataFrame([latency_summary]).to_csv(OUTPUT_DIR / "curation_latency_summary.csv", index=False)

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.histplot(
        data=latency_df,
        x="curation_latency_days",
        bins=60,
        kde=True,
        ax=ax,
        color="#4C72B0",
    )
    ax.set_xlim(0, min(latency_df["curation_latency_days"].max(), 365 * 3))
    ax.set_xlabel("Days from Submission to Acceptance")
    ax.set_ylabel("Number of Evidence Items")
    ax.set_title("Distribution of Curation Latency")
    ax.axvline(latency_summary["median_days"], color="crimson", linestyle="--", label=f"Median = {latency_summary['median_days']:.1f} d")
    ax.legend()
    save_figure(fig, "hist_curation_latency.png")

    # ------------------------------------------------------------------
    # Save core descriptive stats table for key categorical fields
    # ------------------------------------------------------------------
    summary_tables = {}
    for col in [
        "evidence_type",
        "evidence_level",
        "evidence_significance",
        "variant_origin",
        "therapy_interaction_type",
    ]:
        vc = df[col].fillna("<missing>").value_counts()
        summary_tables[col] = vc
        vc.to_csv(OUTPUT_DIR / f"value_counts_{col}.csv")

    # Save a quick numeric summary for evidence ratings by type
    rating_summary = (
        df.groupby("evidence_type")["evidence_rating"]
        .agg(["count", "mean", "median", "std"])
        .round(2)
    )
    rating_summary.to_csv(OUTPUT_DIR / "evidence_rating_summary_by_type.csv")

    # ------------------------------------------------------------------
    # Conflicting evidence (supports vs does not support)
    # ------------------------------------------------------------------
    conflict_cols = [
        "molecular_profile_name",
        "disease_name",
        "evidence_type",
        "evidence_direction",
        "evidence_level",
        "evidence_id",
    ]
    conflict_df = df.dropna(
        subset=["molecular_profile_name", "disease_name", "evidence_type", "evidence_direction"]
    )[conflict_cols].copy()
    conflict_df["evidence_direction_norm"] = (
        conflict_df["evidence_direction"].str.upper().str.replace(" ", "_")
    )

    conflict_records = []
    grouped = conflict_df.groupby([
        "molecular_profile_name",
        "disease_name",
        "evidence_type",
    ])
    for (mp, disease, etype), group in grouped:
        dirs = set(group["evidence_direction_norm"].unique())
        if len(dirs) > 1:
            conflict_records.append(
                {
                    "molecular_profile_name": mp,
                    "disease_name": disease,
                    "evidence_type": etype,
                    "supports": (group["evidence_direction_norm"] == "SUPPORTS").sum(),
                    "does_not_support": (
                        group["evidence_direction_norm"] == "DOES_NOT_SUPPORT"
                    ).sum(),
                    "evidence_items": len(group),
                }
            )

    conflict_summary = pd.DataFrame(conflict_records)
    conflict_summary.to_csv(
        OUTPUT_DIR / "conflicting_evidence_summary.csv", index=False
    )

    if not conflict_summary.empty:
        top_conflicts = conflict_summary.sort_values(
            by=["does_not_support", "supports"], ascending=False
        ).head(15)

        fig, ax = plt.subplots(figsize=(14, 9))
        y_pos = np.arange(len(top_conflicts))
        ax.barh(
            y_pos,
            top_conflicts["supports"],
            color="#2b8a3e",
            label="Supports",
        )
        ax.barh(
            y_pos,
            top_conflicts["does_not_support"],
            left=top_conflicts["supports"],
            color="#c92a2a",
            label="Does Not Support",
        )
        labels = [
            f"{row.molecular_profile_name} | {row.disease_name} ({row.evidence_type})"
            for row in top_conflicts.itertuples()
        ]
        ax.set_yticks(y_pos)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()
        ax.set_xlabel("Evidence Items")
        ax.set_title("Top Conflicting Clinical Interpretations")
        ax.legend()
        save_figure(fig, "bar_conflicting_evidence.png")


if __name__ == "__main__":
    main()
