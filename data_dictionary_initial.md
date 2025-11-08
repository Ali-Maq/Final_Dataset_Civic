# CIViC Evidence Export Data Dictionary (Initial Pass)

## Evidence Item Core Fields

| Column | Description | Documentation |
| --- | --- | --- |
| evidence_id | Numeric identifier for a CIViC Evidence Item (EID), the fundamental curated unit. | docs.md:291 |
| evidence_name | Human-readable label (`EID####`) used throughout CIViC examples. | docs.md:1712 |
| evidence_description | Free-text Evidence Statement summarizing the clinical finding. | docs.md:994 |
| evidence_level | Study strength classification (A–E) for the evidence item. | docs.md:1015 |
| evidence_type | Evidence category (Predictive, Prognostic, Diagnostic, Predisposing, Oncogenic, Functional). | docs.md:896 |
| evidence_direction | Whether the cited study supports or refutes the stated significance. | docs.md:904 |
| evidence_rating | Five-star curator trust rating for the specific evidence statement. | docs.md:984 |
| evidence_significance | Controlled term describing the clinical effect tied to the evidence type. | docs.md:912 |
| evidence_status | Moderation state (submitted, accepted, rejected) in the CIViC workflow. | docs.md:296 |
| therapy_interaction_type | Relationship among multiple therapies (combination, sequential, substitutes). | docs.md:952 |
| variant_origin | Classification of variant origin (somatic, germline, mixed, etc.). | docs.md:1529 |

## Molecular Profile Fields

| Column | Description | Documentation |
| --- | --- | --- |
| molecular_profile_id | Internal ID for the Molecular Profile (MP), the curated combination of variants. | docs.md:243 |
| molecular_profile_name | Standardized MP name assembled from component gene/variant names. | docs.md:1925 |
| molecular_profile_score | Automatically calculated evidence score aggregating level × rating values. | docs.md:1949 |
| molecular_profile_is_complex | True when the MP contains two or more variants (complex MP). | docs.md:246 |
| molecular_profile_is_multi_variant | Flags MPs that include multiple constituent variants per definition. | docs.md:1895 |
| molecular_profile_raw_name | Original name string prior to CIViC formatting conventions. | docs.md:253 |
| molecular_profile_description | Curator-authored summary of the MP’s clinical relevance. | docs.md:1931 |
| molecular_profile_aliases | Alternate MP names maintained alongside the primary name. | docs.md:1937 |

## Variant Fields

| Column | Description | Documentation |
| --- | --- | --- |
| variant_ids | Internal identifiers for CIViC variant entities. | docs.md:1970 |
| variant_names | Canonical variant names used for clinical interpretation. | docs.md:1983 |
| variant_aliases | Alternative variant designations/synonyms captured for searchability. | docs.md:1989 |
| variant_links | Relative link to the variant page (export metadata; not detailed in docs.md). | — |
| variant_single_mp_ids | ID of the simple MP comprised solely of this variant. | docs.md:246 |
| variant_hgvs_descriptions | HGVS expressions curators record for the variant. | docs.md:1995 |
| variant_clinvar_ids | ClinVar identifiers associated with the variant. | docs.md:2001 |
| variant_allele_registry_ids | ClinGen Allele Registry CA IDs generated from curated coordinates. | docs.md:2007 |
| variant_open_cravat_urls | OpenCRAVAT report links derived from representative coordinates. | docs.md:2013 |
| variant_mane_select_transcripts | MANE Select transcript identifiers recommended for annotation. | docs.md:2864 |

## Gene / Feature Fields

| Column | Description | Documentation |
| --- | --- | --- |
| feature_ids | Gene record identifiers tied to the Evidence Item. | docs.md:231 |
| feature_names | Entrez-approved gene symbols used in CIViC. | docs.md:235 |
| feature_full_names | Full gene names retrieved via linked gene resources. | docs.md:235 |
| feature_types | Entity type for the feature (e.g., GENE). | docs.md:231 |
| feature_aliases | Gene synonyms surfaced from linked Entrez/mygene resources. | docs.md:235 |
| feature_descriptions | Curated gene-level clinical summaries. | docs.md:237 |
| feature_deprecated | Flag for retired gene records (export metadata; not detailed in docs.md). | — |
| gene_entrez_ids | Entrez Gene IDs that anchor CIViC gene records. | docs.md:235 |
| factor_ncit_ids | NCIt factor identifiers captured during export (not described in docs.md). | — |

## Fusion-Specific Fields

| Column | Description | Documentation |
| --- | --- | --- |
| fusion_five_prime_gene_names | Named 5′ fusion partners recorded per CIViC fusion conventions. | docs.md:2890 |
| fusion_three_prime_gene_names | Named 3′ fusion partners recorded per CIViC fusion conventions. | docs.md:2890 |
| fusion_five_prime_partner_statuses | Status metadata for 5′ partners (export-only; not covered in docs.md). | — |
| fusion_three_prime_partner_statuses | Status metadata for 3′ partners (export-only; not covered in docs.md). | — |

## Variant Type & Coordinate Fields

| Column | Description | Documentation |
| --- | --- | --- |
| variant_type_names | Sequence Ontology terms describing the variant class. | docs.md:2019 |
| variant_type_soids | Sequence Ontology identifiers linked to the variant type. | docs.md:2019 |
| variant_type_descriptions | Definitions supplied for each Sequence Ontology term. | docs.md:2019 |
| variant_type_links | Links to CIViC/Sequence Ontology records for the variant type. | docs.md:2019 |
| chromosome | Chromosome containing the representative variant. | docs.md:2039 |
| start_position | 1-based genomic start position for the representative alteration. | docs.md:2045 |
| stop_position | 1-based genomic end position for the representative alteration. | docs.md:2045 |
| coordinate_type | Indicates primary vs. secondary coordinate sets for the variant. | docs.md:2025 |
| reference_build | Human reference assembly used for coordinates (e.g., GRCh37). | docs.md:2027 |
| representative_transcript | Ensembl transcript ID used to express the alteration. | docs.md:2057 |
| reference_bases | Reference allele sequence at the curated locus. | docs.md:2051 |
| variant_bases | Alternate allele sequence at the curated locus. | docs.md:2051 |

## Disease Fields

| Column | Description | Documentation |
| --- | --- | --- |
| disease_id | Internal identifier for the linked Disease Ontology term. | docs.md:1607 |
| disease_name | Disease Ontology name associated with the evidence item. | docs.md:1607 |
| disease_display_name | Preferred display label for the disease term. | docs.md:1607 |
| disease_doid | Disease Ontology ID (DOID) for the condition. | docs.md:1607 |
| disease_aliases | Synonyms from the Disease Ontology entry. | docs.md:1607 |
| disease_url | Link to the Disease Ontology record used in CIViC. | docs.md:1607 |
| disease_deprecated | Flag for deprecated disease terms (export metadata; not in docs.md). | — |

## Source Fields

| Column | Description | Documentation |
| --- | --- | --- |
| source_id | Identifier (PubMed ID, ASCO Web ID, ASH DOI) for the evidence source. | docs.md:1656 |
| source_citation | Abbreviated citation generated from the source record. | docs.md:1656 |
| source_citation_id | Same identifier stored separately for lookups. | docs.md:1656 |
| source_type | Source class (PubMed, ASCO, ASH). | docs.md:1656 |
| source_title | Title of the cited publication or abstract. | docs.md:650 |
| source_authors | Author list captured within the source record. | docs.md:650 |
| source_publication_year | Publication year provided by the source metadata. | docs.md:650 |
| source_publication_month | Publication month from the source metadata. | docs.md:650 |
| source_publication_day | Publication day from the source metadata. | docs.md:650 |
| source_journal | Abbreviated journal name recorded with the source. | docs.md:650 |
| source_full_journal | Full journal title retained for completeness. | docs.md:650 |
| source_pmcid | PubMed Central ID (when available); part of export metadata. | — |
| source_abstract | Abstract text stored with the source record. | docs.md:650 |
| source_asco_abstract_id | ASCO meeting abstract identifier when source_type = ASCO. | docs.md:1656 |
| source_open_access | Flag indicating open-access availability (export metadata). | — |
| source_retracted | Flag noting source retraction status (export metadata). | — |
| source_fully_curated | Indicates that all source suggestions have been curated. | docs.md:652 |
| source_url | Link to the external record (PubMed/ASCO/ASH) for the source. | docs.md:1656 |

## Submission & Moderation Fields

| Column | Description | Documentation |
| --- | --- | --- |
| submission_event_id | Audit event ID for the original evidence submission. | docs.md:296 |
| submission_date | Timestamp of the initial submission event. | docs.md:296 |
| submitter_user_id | CIViC user ID of the submitting curator. | docs.md:8 |
| submitter_username | CIViC username of the submitting curator. | docs.md:8 |
| submitter_display_name | Display name presented for the submitter. | docs.md:8 |
| submitter_role | Role at submission time (e.g., Curator, Editor). | docs.md:8 |
| submitter_organization_id | Organization metadata captured during export (not in docs.md). | — |
| submitter_organization_name | Organization name metadata (not in docs.md). | — |
| acceptance_event_id | Audit event ID for acceptance of the evidence item. | docs.md:296 |
| acceptance_date | Timestamp when the item was accepted. | docs.md:296 |
| acceptor_username | Username of the accepting editor. | docs.md:8 |
| acceptor_user_id | CIViC user ID for the accepting editor. | docs.md:8 |
| acceptor_role | Role of the reviewer (Editor or higher). | docs.md:8 |
| rejection_event_id | Audit event ID if the item was rejected. | docs.md:296 |
| rejection_date | Timestamp for rejection (if applicable). | docs.md:296 |
| rejector_username | Username of the rejecting moderator. | docs.md:8 |
| rejector_user_id | User ID of the rejecting moderator. | docs.md:8 |
| rejector_role | Role of the rejecting moderator. | docs.md:8 |
| is_flagged | Indicates that the item has been flagged for editor attention. | docs.md:44 |
| flag_count | Number of active flags associated with the item. | docs.md:44 |
| comment_count | Count of discussion comments on the evidence item. | docs.md:721 |
| event_count | Number of activity log events tied to the item. | docs.md:759 |
| open_revision_count | Count of pending revisions awaiting review. | docs.md:296 |
| last_submitted_revision_date | Timestamp of the most recent submitted revision. | docs.md:296 |
| last_accepted_revision_date | Timestamp of the most recent accepted revision. | docs.md:296 |
| last_comment_date | Timestamp of the latest comment on the item. | docs.md:721 |

## Therapy Fields

| Column | Description | Documentation |
| --- | --- | --- |
| therapy_ids | Internal IDs for therapies linked to the evidence. | docs.md:1621 |
| therapy_names | Preferred therapy names curated for predictive evidence. | docs.md:944 |
| therapy_ncit_ids | NCI Thesaurus identifiers captured for therapies. | docs.md:1621 |
| therapy_aliases | Additional therapy synonyms from NCIt (export metadata beyond docs.md). | — |
| therapy_urls | Links to NCIt entries surfaced in the therapy popover. | docs.md:1627 |
| therapy_deprecated_flags | Flags marking retired therapy records (export metadata). | — |

## Clinical Trial & Assertion Fields

| Column | Description | Documentation |
| --- | --- | --- |
| clinical_trial_nct_ids | Linked ClinicalTrials.gov identifier(s) for the source. | docs.md:976 |
| clinical_trial_names | Study titles imported with the clinical trial link. | docs.md:976 |
| assertion_ids | IDs of Assertions (AIDs) that cite this evidence item. | docs.md:1760 |
| assertion_names | Display labels for linked Assertions. | docs.md:1760 |
| assertion_summaries | Assertion summaries tailored for clinical reporting. | docs.md:1852 |
| assertion_types | Assertion categories (predictive, diagnostic, etc.). | docs.md:1768 |
| assertion_amp_levels | AMP/ASCO/CAP tiering level recorded on Assertions. | docs.md:610 |

## Phenotype Fields

| Column | Description | Documentation |
| --- | --- | --- |
| phenotype_ids | Internal IDs for associated Human Phenotype Ontology terms. | docs.md:936 |
| phenotype_names | HPO term names linked to the evidence item. | docs.md:936 |
| phenotype_hpo_ids | Human Phenotype Ontology identifiers for recorded phenotypes. | docs.md:936 |

## Links & Export Utilities

| Column | Description | Documentation |
| --- | --- | --- |
| civic_url | Direct link to the CIViC web view of the evidence item. | docs.md:18 |
| pdf_path | Local file path captured during export (not part of docs.md). | — |
| pdf_available | Indicator that a PDF was archived with the export (not in docs.md). | — |
