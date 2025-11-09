About CIViC
Advancing Cancer Precision Medicine with Community Collaboration

Precision medicine refers to the use of prevention and treatment strategies that are tailored to the unique features of each individual and their disease. In the context of cancer this might involve the identification of specific variants shown to predict response to a targeted therapy. The biomedical literature describing associations between genetic variants and clinically relevant outcomes is large and growing rapidly. Currently variant interpretations exist largely in siloed private or otherwise encumbered databases resulting in extensive repetition of effort. Effective precision medicine requires this information to be centralized, debated, and interpreted for application in a clinical setting. CIViC is an open access, open source, community-driven web resource for Clinical Interpretation of Variants in Cancer, available online at civicdb.org. Our goal is to enable precision medicine by providing an educational forum for dissemination of knowledge and active discussion of the clinical significance of cancer genome alterations. For more details and to cite CIViC please refer to the CIViC publication in Nature Genetics.

How our Collaborative Process is Different

All content created in CIViC is, and will continue to be, freely available, without restriction under a Public Domain Attribution. Anyone can contribute to CIViC by simply registering for an account. Users join the community with “Curator” level privileges that allow them to comment or propose additions or revisions on any knowledge in CIViC. Proposed additions and revisions are then reviewed by users with “Editor” level privileges before gaining “Accepted” status. Content that has been Submitted but not yet Accepted should be interpreted and used with caution. Community Curators work together with Editors towards comprehensive and accurate interpretations of the clinical relevance of variants in cancer.

Contributing to CIViC

CIViC provides an open forum for community contributions. Anyone can create an account to flag problems, add comments, propose revisions to existing content, or submit new evidence, assertions, or summaries. All proposed additions/revisions enter a pending state until considered for acceptance by a CIViC editor. All content contributed is immediately considered public domain knowledge. For more details on how to contribute please read our curating docs.

Using CIViC Data

CIViC provides an educational resource to support better understanding of the current state of precision oncology. It may also provide useful summaries and links to relevant published evidence for the clinical relevance of specific variants. With appropriate validation (e.g., in a CLIA certified, CAP accredited environment) it may also be used to develop panels or software for variant interpretation in a clinical diagnostic setting. However, direct use of the CIViC application and website is intended for purely research and development purposes. It should not be used for emergencies or taken as medical or professional advice.

We provide CIViC data freely to all under the Creative Commons Public Domain Dedication, CC0 1.0 Universal License. Data can be downloaded in bulk as tab-separated files, VCF files, or accessed through our fully open and documented API.

Participating
CIViC Principles
Community consensus. The interpretations of clinical actionability required to enable precision medicine should be freely available and openly discussed across a diverse community. To facilitate consensus building, the interface must support direct contribution and discussion from members of the community.

Interdisciplinary. An interdisciplinary approach is needed to combine the expertise of genomic scientists, health care providers, industry partners, and other stakeholders whose efforts are often isolated. CIViC is open to curation and use by all. Expert Editors represent diverse scientific and clinical backgrounds.

Transparency. Content should be created with transparency, kept current, be comprehensive, track provenance, and acknowledge the efforts of creators.

Computationally accessible. The interface should be both structured enough to allow computational data mining (via APIs) and agile enough to handle the product of openly debated human interpretation.

Freely accessible. CIViC is committed to providing unencumbered and efficient access to community-driven curation and interpretation of cancer variants. Curated knowledge will remain free and can be accessed anonymously without login unless the user wishes to contribute to content. No fees will be introduced.

Open license. CIViC will encourage both academic and commercial engagement through flexible licensing. CIViC is released with minimal restrictions under a Creative Commons Public Domain Dedication, CC0 1.0 Universal License. While sharing improvements is strongly encouraged, the data can be adopted and used for nearly any purpose including the creation of commercial applications derived from the knowledge.

Depiction of CIViC Principles: community consensus, transparency, computationally accessible, freely accessible, open license, and interdisciplenary
CIViC Principles

How to Contribute
There are several ways you can make a contribution to this important cause:

View: Make use of the community-created content in your own research by browsing, searching, and examining detailed evidence items. All CIViC data and source code are provided freely.

Discuss: Participate in an ongoing discussion in an effort to reach community consensus on the appropriate clinical action(s) for a genomic event via comments.

Flag: Call Editor attention to Entities (Genes, Variants, Molecular Profiles, Evidence, Assertions) that contain inaccuracies or inconsistencies.

Suggest Revisions (Edit): Submit a correction or addition to any details about a Gene, Variant, Evidence Statement, or Assertion.

Add: Add evidence statements that support clinical actions associated with genomic variants (e.g., single nucleotide substitution, structural variant, gene fusion, etc.), summarize the corpus of evidence for a variant, suggest publications for curation, or create a ‘state of the field’ interpretation (i.e., Assertion) of the evidence supporting a variant in the context of a disease and its clinical implications.

Approve/Reject: Editors may approve or reject submitted Evidence, Assertions, and Revisions made by other community members, after taking into account community discussions and opinion.

Before commenting, correcting, or creating, please visit the Curating, Knowledge Model, and FAQ pages to learn more about the CIViC data model and browse the existing content for Genes, Molecular Profiles (Variants), Cancer Types, or Therapies for examples. Understand the data model but unsure of where to start? Check out our list of high-priority gene for inspiration.

Figure depicting the CIViC collaboration process for an Evidence Item
The CIViC collaboration process for an Evidence Item

What are the characteristics of an ‘ideal’ CIViC curator/editor?
CIViC curators and editors should express a strong interest in clinical cancer genomics. Curators/editors should have expertise in relevant academic fields including basic cancer biology, oncology, genomics, clinical informatics, etc and ideally are training for or have already obtained a medical degree (e.g. PhD or MD). Additionally, we expect curators/editors to be open to sharing information with the community, be respectful of other contributors, professional, truthful, ethical, and unbiased. There is sometimes pressure in academia to present one’s research findings in a clinically relevant context. When CIViC evidence statements are created, the curator/editor should conduct an objective assessment of how well the data supports any assertion of clinical relevance. All aspects of the CIViC project are open to debate and amendment, including these guidelines. In addition to adhering to the guiding principles of CIViC, a CIViC editor must also declare any conflicts of interest.

What is a Variant?
A genetic variant is a non-exact copy of a biological sequence. This includes single nucleotide variants (SNVs), insertion/deletion events (indels), copy number alterations (CNVs), structural variants (SVs), transcript fusions, and other genomic/molecular events with cancer associations. The vast majority of variants described in CIViC represent mutations at the DNA level, however, alterations that manifest at the RNA, protein, or epigenetic level are also accepted so as long as there is a demonstrated clinical relevance. In general, the concept of a variant in CIViC is very flexible, but it is highly preferred that the variant be something that could be measured with some quantitative assay (NGS sequencing, qPCR, etc.). Combinations of one or more variants comprise a Molecular Profile.

What is a Molecular Profile?
There is a growing need for clinical annotation of combinations of variants from different genes. For example, double hit lymphoma is characterized by combinations of mutations in MYC, BCL2, or BCL6. In another example, PIK3CA mutation is thought to induce trastuzumab resistance in the context of HER2 overexpressing breast cancer. CIViC addresses this need via use of the Molecular Profile. Molecular Profiles (MPs) are comprised of one or more variants. A simple Molecular Profile is comprised of a single variant. A complex MP is comprised of a combination of two or more variants. The addition of MPs to CIViC V2 involved an essential change to the data model, in that CIViC Evidence Items (EIDs) are now associated to Molecular Profliles instead of directly to variants. This enables clinical annotation of combinations of variants which may not apply to the individual variants in isolation. Annotation of a single variant is accomplished by creating Evidence Items (EIDs) for simple molecular profiles (e.g. curation of a clinical trial showing BRAF V600E sensitivity of vemurafenib in melanoma). Now, annotation of multi variant combinations can be accomplished by creating EIDs for complex Molecular Profiles (e.g. Osimertinib resistance in “EGFR L858R and EGFR T790M and BRAF V600E positive” lung adenocarcinoma). Each MP in CIViC has an associated Molecular Profile page in the user interface containing a curator summary of the MP’s role in cancer, aliases, links to pages for the individual variants that comprise the MP, and a list of all of the curated Evidence Items which are uniquely associated to the MP.

What kinds of Variants belong in CIViC? What does not?
Variants, or combinations of variants, are accepted into CIViC provided there is evidence linking them to cancer with some clinical or functional relevance. Relevance to cancer biology alone is NOT sufficient unless there is also some documented relationship between the variants and diagnosis, predisposition, prognosis, functional or oncogenic relevance, or predictive value for a specific treatment. Variants related to diseases other than cancer should not be entered (there is some grey area for cancer-like conditions). CIViC accepts somatic, rare germline, and common germline variants related to cancer (as long as they have clinical or functional relevance), however, most variants in CIViC are somatic mutations. Variants are related to clinical evidence via Molecular Profiles (MPs), which are comprised of combinations of one or more variant, and Evidence Items (EIDs) are curated from literature and abstracts, and associated to MPs. The quality of evidence suggesting clinical relevance of a variant or combination of variants may vary considerably. Before contributing to CIViC please review the curation documentation and familiarize yourself with the CIViC knowledge model.

What is an Evidence Statement?
An evidence statement is a brief description of the clinical relevance of a simple or complex Molecular Profile that has been determined by an experiment, trial, or study from a published literature source. It captures a Molecular Profile’s impact on clinical action, which can be predictive of therapy, correlated with prognostic outcome, inform disease diagnosis (i.e. cancer type or subtype), predict predisposition to cancer in the first place, or relate to the functional impact of the variant. A single citation can be the source of multiple evidence statments, but each evidence statement has only one source. A single evidence statement should correspond to only one clinical interpretation and disease. For example, if a paper describes both predictive and prognostic relevance for a variant or combination of variants, two evidence statements should be created. If two publications draw the same conclusions about the clinical relevance of a Molecular Profile, these should also be entered as two evidence statements. Functional evidence may be less strictly related to a specific cancer subtype but curation of such evidence should still prioritize Molecular Profiles or genes whose functional significance are in some way relevant to clinical interpretation. As one example, a variant of unknown clinical significance, in proximity to another clinically relevant variant, might have some clinical significance if shown to have a similar functional effect as the variant with established clinical significance.

How is this information organized?
An in-depth description of the knowledge model behind CIViC can be found here.

What information is currently in CIViC?
CIViC currently houses thousands of evidence statements, variants and genes across multiple cancer types and these numbers are growing rapidly with your help! Refer to the CIViC Home page for more detailed information.

How do I contribute information?
The curation pages detail the curation and editing process, and includes instructions on how to curate CIViC and apply for editorship.

My favorite Gene or Molecular Profile is not in CIViC?!?
The extensive manual curation required to add evidence statements means that there might not yet be an evidence statement for every Molecular Profile or Gene of interest. This is precisely why we need community-driven efforts to grow this database. For a Gene or Molecular Profile to appear in CIViC, it must have an evidence statement associated with it. To add evidence statements and begin the discussion about your gene/variant/combination of variants of interest, go here!

May I enter unpublished results from n-of-1 observations?
At this time, a publication or abstract is considered a minimum requirement for all evidence statements in CIViC. N-of-1 results from early stage clinical trials or patients treated under compassionate use doctrines are allowed, but only if a case report has been published in a peer reviewed journal. We are considering options for centers that wish to use a local instance of CIViC to capture unpublished individual patient observations. We are also considering other source types including clinical trial records, and ClinVar records.

Why must my contributions be approved by an Editor?
In an effort to ensure quality (and prevent automated spam), we require that edits be submitted to the review queue before they are shown as accepted. Editors are used for this review step to protect the CIViC resource and will approve your revisions as soon as possible. An Editor may comment on your proposed addition or revision. You will be able to see your new content in a pending state while it awaits review. To expedite the review process, we encourage you to submit high quality evidence (evidence level of validated or clinical) as the top priority. Similarly, proposing evidence statements for a new variant or gene may take longer for the community to review.

What is a Disease Ontology ID (DOID)?
To provide a structured representation of the diseases associated with evidence statements, we ask that you use disease names as they exist in the Disease Ontology from disease-ontology.org. This allows for consistent representation and minimized ambiguity when referring to diseases. Such ontologies also support more flexible data queries that allow disease groupings ranging from generic terms to highly specific subtypes. If the disease ontology is missing an important recognized sub-type of disease, we will try to work with them to update their resource. Please contact us if you find such cases.

Where does this information come from? Can I submit my abstract?
The information in CIViC is derived from peer-reviewed, published literature. Every evidence item currently requires a citation from PubMed, ASCO Meetings or ASH Meetings. This means that abstracts are not supported until they are peer-reviewed, published, and a PubMed or ASCO/ASH ID is assigned.

What if a drug is shown to have a negative effect on patients with a variant? Or the study was inconclusive?
The knowledge model, specifically the Evidence Direction field, is used to indicate whether the study supports or refutes (including inconclusive determinations) any interaction between the Molecular Profile and a clinical action or result. The Clinical Significance field indicates the type of effect the Molecular Profile is determined to have on clinical results, for example, having a positive, negative or neutral/no impact. These descriptions provide human readable interpretations of evidence statements that either support or refute sensitivity or resistance predictions to therapeutics (or other clinical outcomes). For more detailed definitions and specific examples, please review the knowledge model here.

My evidence statement disagrees with evidence from another source, should I still add it?
Absolutely. CIViC is a forum for discussion of disagreements in the field or literature. Simply log in, go to the Comment tab found on the Evidence, Variant, Molecular Profile, or Gene pages, and discuss this disagreement with the community.

I don’t want to add evidence statements, can I still contribute?
Yes. Evaluation of the literature is a collaborative effort. If you don’t want to add new evidence, you can edit or discuss existing evidence. You can also help to make sure the Molecular Profile Summary is an effective, concise, and accurate summary of the current set of evidence statements and state of knowledge in the field for the Molecular Profile. You can also add promising publications to the source suggestion queue.

What is MyGene.info?
MyGene.info is a web service that allows simple query and retrieval of gene annotation data. We use it in CIViC to automatically import gene details from Entrez Gene such as gene name, synonyms, protein domains and pathways.

Is there an API that I can access?
Yes! Please review the API documentation for more details.

What is the difference between “Supports a Negative association” and “Does not support a Positive association”?
This can be confusing. We have reserved “Does not support - Sensitivity” for statements that contradict previous statements that are supporting sensitivity associations. For example, they would read “Contrary to the previous study which found this mutation sensitive to drug X, this study reported no effect.” The information that this study “Does not support” the prior study’s conclusion is what we are trying to capture with these classifications.

Where do I begin to curate evidence statements? Are certain evidence types or genes a priority?
The evidence statements that make up CIViC are generated from peer-reviewed, published literature. Our top priority is high quality (4+ star rating) Evidence Level A and B statements that associate specific variants with clinical outcomes using well powered patient cohorts. To help direct users towards genes known to be associated with clinical outcomes, we have compiled a list of high priority genes which you can download here. This list is based on a survey of 90 commerically available clinical gene panels developed by 40 distinct institutes and companies. If many independent groups feel that a gene is important to profile on their assay, it might be important. CIViC aims to spell out, with complete provenance, the evidence that each of these genes really is clinically important and why/how.

Can I use a review article to create an evidence statement?
Yes, but we urge caution when using such sources. It is generally preferable to find the primary source articles cited by the review article instead. Particularly, when a review article is describing contradictory findings from multiple studies. Individual evidence items created from each study should be created to capture this debate. The Molecular Profile Description might be a better place to cite relevant review articles.

How is CIViC licensed?
The content of CIViC, hosted by Washington University School of Medicine is released under the Creative Commons Public Domain Dedication (CC0 1.0 Universal) and the source code for the CIViC application is licensed under the MIT License.

Curating CIViC
Introduction to CIViC Curation

With the recent advent of rapid and affordable tumor genome sequencing, interpreting the clinical significance of cancer variants from the wealth of existing and rapidly evolving medical literature has become a major bottleneck to realizing the potential of precision cancer medicine.

Associating cancer variants with concrete clinical actions by manual curation of high quality evidence is a great challenge. Creating useful interpretations requires integrating complex information from diverse sources ranging from preclinical lab experiments to clinical trial results. Creating and maintaining such interpretations will require the concerted effort of many experts at a large scale.

CIViC curators are a community of such experts dedicated to creating and maintaining a knowledgebase clinical interpretations for cancer variants.

Although curators are not required to have any specific training, background or skill set, curator-generated content can only be “Accepted” once it is reviewed by a CIViC Editor. Editors are experts in cancer genomics, oncology, pathology and other relevant fields. This gate-keeper model allows significant contributions from curators with any level of experience while maintaining the quality of an expert-driven resource. Curators can be promoted to Editors once they have demonstrated sufficient understanding of the CIViC data model and requirements for cancer variant interpretation.

CIViC curation involves documenting the published evidence for the clinical relevance of cancer variants. This includes creation of structured CIViC evidence statements for cancer variants, curation of variant coordinates, integration of multiple evidence statements into CIViC assertions, and creation of molecular profile-, variant- and gene-level summaries.

However, even small contributions can make a big impact on how up-to-date and comprehensive the CIViC resource is. Examples of small curation activities include: commenting on existing entries, identifying additional literature sources, improving the wording of a variant interpretation, adding variant IDs or aliases, etc.

Curation Prerequisites

Create an account. Creating an account requires only that you have login credentials for one of our supported Open Authorization (OAuth) providers (currently Google, ORCiD, or GitHub).

For a primer on the fundamentals of cancer variant interpretation, we suggest that new users start by reading the CIViC paper, several recently published Standards and Guidelines that CIViC adheres to wherever possible, and other recommended reading as described below.

Required reading for curators

CIViC is a community knowledgebase for expert crowdsourcing the clinical interpretation of variants in cancer.

CIVIC curation standard operating procedure.

ACMG/AMP - Standards and guidelines for the interpretation of sequence variants.

ClinGen - Somatic cancer variant curation and harmonization through consensus minimum variant level data (MVLD).

AMP/ASCO/CAP - Standards and guidelines for the interpretation and reporting of sequence variants in cancer.

Standards for the classification of pathogenicity of somatic variants in cancer (oncogenicity): Joint recommendations of Clinical Genome Resource (ClinGen), Cancer Genomics Consortium (CGC), and Variant Interpretation for Cancer Consortium (VICC).

Other recommended reading

Standardized decision support in next generation sequencing reports of somatic cancer variants

Adapting crowdsourced clinical cancer curation in CIViC to the ClinGen minimum variant level data community‐driven standards

Evaluating the Clinical Validity of Gene-Disease Associations: An Evidence-Based Framework Developed by the Clinical Genome Resource

Organizing knowledge to enable personalization of medicine in cancer

More information

For further information on curation with the CIViC platform we provide General Curation Practices, and documentation for Curating Molecular Profiles, Curating Variants, Curating Genes, Curating Evidence, Curating Assertions, and Suggesting Sources. For examples and ideas on how to get started, visit our Curation Ideas and Monitoring Curation Activity pages. Finally, if you are interested in Becoming An Editor we provide details on the criteria for promotion.

Contents:

General Curation Practices
Curating Variants
Curating Genes
Curating Molecular Profiles
Curating Evidence
General Evidence Item Curation Practices
Predictive Evidence
Predictive Evidence Curation Practices
Diagnostic Evidence
Diagnostic Evidence Curation Practices
Prognostic Evidence
Prognostic Evidence Curation Practices
Predisposing Evidence
Predisposing Evidence Curation Practices
Oncogenic Evidence Type
Oncogenic Evidence Curation Practices
Functional Evidence Type
Functional Evidence Curation Practices
Curation Scenarios
Curating Evidence from Clinical Trials
Complex Molecular Profiles in comparison to Categorical (Bucket) MPs
Curating Assertions
Predictive Assertions
Prognostic Assertions
Diagnostic Assertions
Predisposing Assertions
Oncogenic Assertions
Citing EIDs in Assertions
Curating and Suggesting Sources
Prioritizing Curation Effort
Example Curation Activities
Monitoring
Becoming an Editor


General Curation Practices
The goal of CIViC is to provide current, comprehensive and accurate knowledge to aid in the clinical interpretation of cancer variants. A strong emphasis for curation should be placed on genes, molecular therapies (targeted to variants or ensembles of variants which we call Molecular Profiles), evidence and assertions of greatest potential clinical relevance to cancer. In addition to predictive (theranostic), prognostic, diagnostic and prediposing evidence, CIViC supports curation of evidence supporting the oncogenicity or functional impact of variants, though again the emphasis of this effort is on such evidence that may ultimately support clinical relevance for cancer.

CIViC curators should avoid directly copying phrases from original sources (including abstracts) for summaries, statements, and comments. This practice prevents plagiarism and copyright infringement for articles with limited public access.

Suggested revisions should always include a comment, providing rationale for the change. This allows editors to better understand the changes being proposed and facilitates acceptance or further modification.

If a curator finds inaccuracies or inconsistencies in the database, they should flag such entities to assist editors in rectifying cuCurating Variants
A CIViC Variant represents any molecular alteration with evidence for clinical relevance in cancer. CIViC Molecular Profiles (MPs) are comprised of one or more CIViC Variants. Simple MPs are comprised of one variant, and complex MPs are comprised of combinations of two or more variants. A new variant is added to the CIViC database during Evidence Item creation. For a simple MP, when the first Evidence Item containing clinically relevant information for a new variant is submitted then that variant is added to the database. Variants can also be added to the database during the creation of complex Molecular Profiles. When a complex MP contains a variant not yet in CIViC, then when the first Evidence Item is curated for this MP, new variants will be added to the database during the curation process.

Once a variant exists in the database, then variant coordinates and other variant-level data can also be curated in the user interface. The CIViC definition of a variant is intentionally broad to encompass not only simple variation (e.g., SNVs and indels), but also regional/categorical variation (e.g., exon mutation), or other types of variation (e.g., expression, fusions).

Features within the Variant knowledge model include: Aliases, HGVS expressions, ClinVar IDs, Variant Type, representative Variant Coordinates and Transcript.

Additional instruction on curating individual components of variants are provided in the Knowledge Model docs for Variants.

ration issues.




Curating Genes
The CIViC Gene knowledge model provides summarized gene-level context for all CIViC variants contained by the gene.

For a gene record to become visible, it must be associated with at least one Evidence Item that describes a Molecular Profile (MP) consisting of one or a combination of multiple variants, where one of the MP variants is contained by the gene.

Genes are identified within CIViC using Entrez Gene names and IDs. Once a gene record exists it is automatically linked (via Entrez Gene) to additional gene-level details using the mygene.info resource and to the Drug Gene Interaction Database.

Finally, a high-level summary of the clinical relevance of the gene (as described by curated evidence/variants) can be curated along with supporting references (e.g., relevant reviews). Additional instruction on curating individual components of genes are provided in the Knowledge Model docs for Genes docs.

Genes are displayed on a page with a list of gene associated Molecular Profiles below the curator written gene Description. The page also contains a tab to see all of the gene associated variants (Figure 1).



Curating Molecular Profiles
The Molecular Profile (MP) data model is described in the Understanding MPs section. A curator adding Evidence Items (EIDs) to CIViC will utilize Molecular Profiles for curation of either a single or combination of variants. In the new workflow model (Figure 1), a curator will choose from two MP types:

Simple Molecular Profile: A simple Molecular Profile (MP) is comprised of a single variant. The simple MP replaces the CIViC Variant in the old curation workflow of CIViC, where each EID described a single variant associated with a single gene (Figure 1).

Complex Molecular Profile: A complex Molecular Profile (MP) is comprised of two or more variants. In the new CIViC workflow model, evidence for complex combinations of variants may be curated and different variants in a complex MP may be associated with different genes (Figure 1).

Figure depicting the old, single variant workflow model and new Molecular Profile based CIViC workflow model for curation
Figure 1: Old, single variant workflow model and new Molecular Profile based CIViC workflow model for curation

Molecular Profiles are named with the gene first, and then the specific variant name (Figure 2). This convention is followed for both simple and complex MPs. Thus in the Molecular Profile “EGFR L858R OR BRAF V600E” the user and curator knows which gene each variant in the MP is associated with.

Figure depicting the difference between a CIViC Variant compared to simple and complex CIViC Molecular Profiles
Figure 2: CIViC Variant versus a simple and a complex Molecular Profile

An important thing for curators to note is the difference in the CIViC workflow and UI between variants and MPs. When going to a gene page such as EGFR, the MPs associated with the gene are shown by default (Figure 3). There is also a tab called Variants on this page that will allow the user or curator to view the collection of individual variants associated with the gene.

Figure depicting how CIViC Molecular Profiles are associated to a gene and are displayed on the gene page in the user interface
Figure 3: Molecular Profiles associated to a gene are displayed on the gene page in the user interface

In the old CIViC workflow model (Figure 1), a user might search for a gene of interest, landing at the CIViC page for that gene. This page contained all of the variants which had curated information for that gene of interest. The user or curator could then select an individual variant of interest, each of which had their own page, and then see all of the Evidence Items (EIDs) curated for that variant at the bottom of the variant page. In the new workflow model, things are very similar, in that a user can go to the gene page, but now they see a list of Molecular Profiles that contain a at least one variant of that gene. The majority of MPs on a gene page will usually be simple MPs containing variants for the gene as in Figure 3, where MPs such as EGFR L858R, EGFR T790M, and other familiar simple MPs are seen. At the end of the collection of simple MPs the user will find complex MPs which contain at least one variant from the gene of interest. These complex MPs can also contain variants associated with genes other than that of the gene page. Thus on the EGFR gene page, one finds the complex Molecular Profile BRAF V600E AND EGFR L858R AND EGFR T790M. So, to find a specific complex MP, a user can go to any gene page that has a variant that is part of the complex MP and find the MP there.

Figure depicting the CIViC browse view for Molecular Profiles
Figure 4: Browse Molecular Profile functionality

Another approach for a user or curator to locate MPs of interest is to use the Browse functionality (Figure 4), which can be used for all top level entities in CIViC including Molecular Profiles, found at the left of the user interface. If the user wants to see all MPs which contain a variant called V600E, then as in Figure 4, the user can type that into the Variants field, and all MPs containing a variant named V600E will be shown, and in this case all V600E variants are associated to the gene BRAF. Both simple and complex MPs are shown. Note if a user were interested in all MPs containing a bucket variant such as EGFR Mutation, then the user could type Mutation into the Variants field, and then EGFR into the Genes field, in order to narrow down the display to MPs containing only EGFR Mutation, instead of seeing all MPs containing the variant named Mutation associated to any gene.

On the gene page, the user can also choose a Variants tab (Figure 3), and see all of the variants associated to the gene, such as L858R or T790M for EGFR. Clicking on one of these will take the user to a variant page, and on the variant oage are listed variant related information such as coordinates, and also a list of all simple and complex MPs that contain the variant.

Creation of new complex Molecular Profiles when adding Evidence Items

All Evidence Items (EIDs) in CIViC are associated with either a simple or complex Molecular Profile (MP). When adding new Evidence Items to CIViC, the curator can choose either a simple MP or a complex MP in the Molecular Profile field of the Add Evidence Item Form (Figure 5).

Figure depicting how a CIViC user can choose to add a simple or complex Molecular Profile
Figure 5: Choosing to add an Evidence Item for a simple or complex Molecular Profile

Adding a simple MP in the Add Evidence Form requires the curator to first specify a gene, and then specify a variant associated with that gene. As with simple MPs, new complex Molecular Profiles are added to CIViC during the process of adding the first EID specific to that complex MP. The Process by which a new complex MP is created in the Add Evidence Form is outlined in the workflow figures below (Figure 6).

Figure depicting the selection of a Gene for a Molecular Profile
Figure 6a: Workflow for creation of new complex Molecular Profiles in the Add Evidence Form - Selecting a Gene

Figure depicting the selection of a Variant and boolean operator for a Molecular Profile
Figure 6b: Workflow for creation of new complex Molecular Profiles in the Add Evidence Form - Selecting a Variant and boolean operator

Figure depicting the selection of additional variant(s) to create a complex Molecular Profile
Figure 6c: Workflow for creation of new complex Molecular Profiles in the Add Evidence Form - Selection additional variant(s)

Curating Evidence
Evidence Items (EIDs) are the fundamental unit of the CIViC knowledgebase. EIDs derive structured clinical statements from peer reviewed, PubMed-indexed publications and American Society of Clinical Oncology (ASCO) or American Society of Hematology (ASH) abstracts, which act as primary Sources for Evidence Items. EIDs link back to their sources. EIDs are hand-curated units of knowledge, and one evidence source may supply enough data to create multiple EIDs. EIDs are displayed throughout the CIViC application, for example as a summary (Figure 1) and as a data table row (Figure 3).

Screenshot of an Evidence Item
Figure 1: Screenshot of an Evidence Item

CIViC Evidence is added and curated via a moderation process that includes submitting, evaluating, accepting (or rejecting), and suggesting changes (Figure 2). CIViC Curators may add or suggest revisions to curated content at each step. Adding content involves submitting new Evidence Items or Assertions that subsequently undergo revision and Editor review. Revision of content involves adding or revising the clinical summary and/or its associated features. Once changes are made within the CIViC database, the additions/revisions become visible directly or on a separate revision page depending on the type of submission. Curation is listed as a “Submitted” (i.e., pending) until it is accepted by an Editor, who have the power to accept or reject Curator submissions. Curators may reject (but not accept) their own submissions/revisions. This is useful when a curator realizes they have made an error they wish to correct.

Overview of CIViC content creation process
Figure 2: Overview of CIViC content creation process

It is important to note that once evidence is submitted into CIViC as a new Evidence Item, then the EID is visible to the community in the unmoderated/non-reviewed state, and these EIDs are labeled in yellow (Figure 3). This enables the public to comment or create moderations on the submitted evidence. It is also important to note that yellow Evidence Items may be incomplete, not accurately fit into the CIViC data model, or contain problems which the moderation process is designed to capture and fix. Once a CIViC EID has been reviewed by editors, and all revisions reviewed and accepted, then the EID is accepted by an editor, and its label changes to green. Mousing over an EID brings up additional details, including whether the EID has any flags, pending revisions or comments. Note that revisions can be pending for EIDs that are in both the Submitted/Unreviewed Status (yellow) and the Accepted Status (green). In other words, even once accepted, evidence may still be improved further.

Evidence Item data grid features
Figure 3: Evidence Item data grid features

General Evidence Item Curation Practices
Evidence Items should generally be prepared from primary literature rather than from review articles. It is recommended that curators use reviews to identify potential primary literature referenced in the review and to curate individual Evidence Items based on these cited articles. Review articles can also be used to develop Gene and Variant summaries. Similarly, evidence should not be created from introduction or discussion content in articles that are just restating previous findings of other works. Instead the curator should always try to find the primary/original source of information.

When curating new evidence, the curator should review the existing evidence already curated into CIViC for that Variant to look for the following issues:

For clinical trials and case reports (Levels A, B, and C), overlapping patient populations (i.e. the same patient treatment and outcome described in multiple reports) should be avoided, or carefully noted to alert users of this nuance and avoid conclusions that mistake these studies as independent. Note also that reports describing different phases of the same patient treatment (i.e. erlotinib and subsequently afatinib), or different clinically relevant conclusions (i.e. predictive evidence and simultaneous diagnostic evidence) are independent/non-overlapping entities.

For Predisposing EIDs, which generally describe germline molecular profiles (variants), the same patient may appear in multiple studies. Curators should be careful to note these cases and review existing germline EIDs for the same molecular profile in CIViC.

Disease stage, prior treatments, and other experimental details influencing evidence interpretation should be captured within the Evidence Statement to maximize user comprehension of the underlying study and the appropriate context in which it is relevant. Such details are critical parts of clinical guidelines and can impact which clinical guidelines should be used as well as interpretion of types of therapy response (see for example EID1008 and EID1009).

Six types of EID exist in CIViC (Figure 4), each giving structured clinical annotation to a Molecular Profile (Variant). Four types of clinical statements, Predictive/Therapeutic, Prognostic, Diagnostic and Oncogenic Evidence Types are usually associated with somatic molecular profiles (variants), while Predisposing evidence is generally linked to germline variation. Functional studies are often performed in vitro, so associated EIDs may often have the Unknown field selected for Molecular Profile (Variant) Origin.

Structured annotation comprising the five types of CIViC Evidence Item
Figure 4: Structured annotation comprising the six types of CIViC Evidence Item

Predictive Evidence
Predictive/Therapeutic Evidence Items (EIDs) capture evidence supporting or refuting the role of a molecular profile (variant) in conferring drug sensitivity, resistance or adverse response in the context of a specific disease.

Below is an example of an EID that illustrates the Predictive Evidence Type (Figure 5). This example describes the CLEOPATRA trial (NCT00567190), which evaluated 808 patients with HER2-positive metastatic breast cancer. These patients demonstrated significant sensitivity/response when treated with combination therapy of docetaxel, pertuzumab and trastuzumab.

Screenshot of a Predictive Evidence Item summary
Figure 5: Screenshot of a Predictive Evidence Item summary

Predictive Evidence Curation Practices
Predictive Evidence Items should include the Therapy (Drug) Name(s) and Therapy Interaction Type (for multiple therapies used in some kind of combination).

The most current name of the Drug (excluding trade names) should be used in the Therapy field to reduce duplication. The Evidence Statement should contain the therapy name used in the study with the current name in brackets, when applicable.

Therapy Interaction Types are required anytime more than one drug is mentioned for a given study. If multiple therapy interaction types are at play (e.g., combinations and substitutes), consider separating these concepts into more than one Evidence Item.

If applicable, the Clinical Trial name should be included in the Evidence Statement. Any clinical trial IDs available in PubMed for the Source linked to this Evidence Item will be automatically imported and linked to this Evidence Item when the PubMed Source is imported into CIViC.

The duration of exposure to the therapy and confounding interactions (e.g., wash-out periods, previous treatment, cancer stage) should be listed.

Assigning a Clinical Significance of Sensitivity/Response can depend on factors such as response rate, which will vary significantly with disease and treatment. In some cases a response rate of 15% may represent a significant improvement, and merit a classification of the Sensitivity/Response label. A general guideline for CIViC curation is to follow the author’s published (and peer-reviewed) interpretations and conclusions of the results.

Extensive guidelines, use cases, and examples for curation of predictive evidence are given in Figure 14 and Table 1.

Diagnostic Evidence
Below is an example of an EID that illustrates the Diagnostic Evidence Type. This example describes the World Health Organization guidelines for classifying chronic myelomonocytic leukemia (CMML). Specifically, if a patient has a PCM1-JAK2 fusion or a rearrangement involving PDGFRA, PDGFRB, or FGFR1, especially in the setting of eosinophilia, the patient does not have CMML.

Screenshot of a Diagnostic Evidence Item summary
Figure 6: Screenshot of a Diagnostic Evidence Item summary

Diagnostic Evidence Curation Practices
Diagnostic Evidence Items should only be used if the molecular profile (variant) assists in labeling the patient with a specific disease or disease subtype and should not be used to denote that the particular molecular profile is simply prevalent in a specific disease.

Generally, Diagnostic Evidence Items describe molecular profiles that can help accurately diagnose a cancer type or subtype with high sensitivity and specificity, for which diagnoses may otherwise be challenging.

Diagnostic Evidence Items should be very closely tied to the terms of the Disease Ontology (DO) in CIViC. The Disease Ontology works to actively generate mappings to other highly used ontologies, but the terms in the DO are generally accepted diseases which are part of medical practice. Therefore, literature proposing a novel disease type - for instance studies suggesting a novel cancer subtype defined by the presence of a specific oncogenic variant - are not generally admitted as part of the CIViC data model. Alternatively, if a curator with expertise in the field feels that the novel subtype has met with a sufficient level of acceptance, they may submit this type of Evidence Item using a non-DO term, and suggest that the DO admit this term into the ontology.

Literature describing diagnostic practice guidelines (such as those of the World Health Organization) may be used in curation and submitted as A-level Evidence Items.

Literature describing small numbers of observations in patient samples of a certain molecular profile (variant), where the authors state that the molecular profile may have diagnostic value, may be admitted as lower Evidence Rating (1-2 star), Case Study (C-level) data. Similar literature employing larger numbers could be labeled as Clinical (B-level).

Guidelines and use cases for curation of diagnostic evidence are given in Table 1.

Prognostic Evidence
Below is an example of an Evidence Item that describes a Prognostic Evidence Type. This example describes a 406-patient trial whereby observation of any somatic TP53 mutation in chronic lymphoblastic leukemia conferred poor prognosis relative to wildtype TP53.

Screenshot of a Prognostic Evidence Item summary
Figure 7: Screenshot of a Prognostic Evidence Item summary

Prognostic Evidence Curation Practices
Prognostic Evidence Items should include the measured outcome (e.g., overall survival, complete response, partial response), number of subjects and applicable statistics.

If described in the literature, a definition of the measured outcome should be given.

Prognostic evidence is characterized by either better outcomes for patient subpopulations with the given molecular profile (variant), which are not specific to any particular treatment context, or worse outcomes which are not indicative of resistance to a specific treatment. Instead, the change in outcome should be largely correlated to the presence of the molecular profile.

In some cases, a molecular profile (variant) subpopulation with worse outcome may benefit from subsequent therapy targeted to that molecular profile (e.g., HER2 amplification in breast cancer).

Guidelines, use cases, and examples for curation of prognostic evidence are given in Figure 14 and Table 1.

Predisposing Evidence
Predisposing Evidence Items were first introduced in CIViC v1 to capture the role of a molecular profile (variant) in increasing the likelihood of developing cancer. This is comparable to the concept of heritable genomic variants that increase risk for “cancer predisposition syndromes” or “cancer susceptibility”. In CIViC v2, Predisposing Evidence Items include both this historical clinical significance of “cancer predisposition variants”, as well as evidence items that decrease risk for cancer susceptibility by conferring a protective effect (“cancer protectiveness variants”). The structure of Predisposing Evidence Items (EIDs) mirrors the structure of other EID types in CIViC by having multiple clinical significance classifications under which evidence can be evaluated. (Figure 8). Thus, just as Prognostic EIDs capture better and worse outcomes, and Predictive EIDs include the ability to capture sensitivity and resistance, the Predisposing EID can capture detrimental pathogenic and also beneficial protective qualities. CIViC Predisposing Evidence Items which pertain to the Pathogenic axis in Figure 8 can be aggregated at the CIViC Assertion level for a formal pathogenicity evaluation utilizing ACMG/AMP Codes.

The opposing qualities of Predisposing, Prognostic, Predictive Evidence Items.
Figure 8: The opposing qualities of Predisposing, Prognostic, Predictive Evidence Items.

The Pathogenic axis for Predisposing EIDs (right side in Figure 8) documents evidence which describes either the presence or absence of a pathogenic property for a molecular profile (variant). It is important to realize that evidence supporting both a pathogenic or benign classification are captured using the Predisposition clinical significance, associated with the right (red) axis (labeled Pathogenic) by use of the CIViC Evidence Direction (Supports or Does not support) (Figure 9). To summarize, a CIViC Predisposing EID that Supports clinical significance of Predisposition suggests a potentially pathogenic molecular profile (variant). A Predisposing EID that Does Not Support clinical significance of Predisposition suggests a potentially benign molecular profile (variant). These EIDs do not make any final classification of pathogenicity and may or may not fully support any specific ACMG criteria but point in the direction of such classifications.

Predisposing Evidence Item Clinical Significance relates either to cancer protectiveness or predisposition
Figure 9: The Predisposing Evidence Item (EID) Significance relates either to cancer protectiveness (left/green arrow) or predisposition (right/red arrow). The Evidence direction (Supports or Does Not Support) indicates whether the EID is pointing towards benign or protectiveness/predisposition effect.

As mentioned above, the Predisposing Evidence Type may utilize ACMG/AMP Codes when applicable. If the curator wishes to capture evidence that indicates a molecular profile (variant) may be benign or pathogenic, and this evidence meets one or more of the published criteria from ACMG/AMP guidelines (termed ACMG codes in CIViC), then the curator can indicate the ACMG codes that were met in the body of the EID. The general format for a predisposing EID of this type is a summary of the reported data relevant to the molecular profile (variant) and disease of interest, followed by an enumeration of ACMG Code(s) derived from the reported information with a brief justification for the presence of each code.

Note that currently, ACMG/AMP criteria should be restricted to simple (single variant) Molecular Profiles. Multiple ACMG criteria are not forumlated for groups of co-occuring variants accross different genes. For example PM1 (Located in a mutational hot spot and/or critical and well-established functional domain) is not clear wether this would be required of one or all of the variant members of a complex MP. PP1 (Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease) is also clearly not defined for combinations of varinats.

Below is an example of an Evidence Item (EID5546) that describes a Predisposing Evidence Type (Figure 10) that Supports a Significance of Predisposition. This example describes a study where the VHL - R167Q (c.500G>A) Variant was described in a set of patients and evidence for the PP1 ACMG-AMP criteria was documented. Hemangioblastoma and pheochromocytoma were seen in patients and are reported as Associated Phenotypes, while the Disease is Von Hippel-Lindau Disease.

Predisposing evidence summary.
Figure 10: Screenshot of a Predisposing Evidence Item that supports predisposition, suggesting a potentially pathogenic molecular profile (variant), supported by a specific ACMG pathogenicity criteria/code

Predisposing Evidence Curation Practices
Typically, but not always, Predisposing Evidence Items are written for rare germline variants. In rare circumstances, the patient can have a predisposing variant that develops as a result of a somatic mutation or mosaicism during embryogenesis that is widespread, but not necessarily heritable. Common germline variants may also be associated with predisposition to cancer.

For evidence that indicates the presence or lack of a protective quality for a germline molecular profile (variant), this will be annotated with Supports Protectiveness or Does not support Protectiveness, respectively. Although not yet well-described in cancer predisposition, we anticipate examples will become available with time based on other complex diseases, such as the APOE2 allele which has evidence that it is protective against Alzheimer’s disease.

Evidence supporting pathogenicity will be captured by a curator by selecting Supports, and then Predisposition using the menus available on the Add Evidence form in CIViC. Importantly, evidence supporting a benign annotation will be captured during curation by choosing Does Not Support and then Predisposition in the menus available in the Add Evidence form.

For EIDs that utilize the Significance value Predisposition, ACMG evidence criteria (Richards et al 2015) (termed ACMG codes for short) are derived from the evidence presented in the specific Evidence Source and are listed at the end of the Evidence Statement with a brief justification for each code’s use. ACMG evidence codes that can not be directly derived from the Evidence Source (e.g., population databases for PM2) should be captured in the Molecular Profile Description or at the level of the Assertion. The EID depicted here is part of Assertion number 4 (AID4), where the Evidence Items combine to create a Pathogenic Assertion. Predisposing Evidence Items do not individually determine ACMG/AMP Pathogenicity, but simply show in which direction the evidence derived from the particular publication or abstract is “leaning”, e.g., if it is leaning towards a pathogenic or benign final classification.

Oncogenic Evidence Type
Oncogenic Evidence Items (EIDs) capture clinically relevant information associated with either a somatic molecular profile’s (variant’s) protective qualities or, more commonly, its involvement in tumor pathogenesis as described by the Hallmarks of Cancer. An Evidence Statement for an Oncogenic EID includes a summary of the reported data relevant to the molecular profile and disease of interest by describing assays performed and experimental results. The Evidence Summary for an Oncogenic EID may contain Oncogenicity Codes from the ClinGen/CGC/VICC Standards for the classification of oncogenicity of somatic variants in cancer.

In a system similar to the one described above for Predisposing Evidence Items, the Protective Clinical Significance may be used to capture evidence associated with a somatic variant’s ability to reduce the development or harmful effects of a tumor. For example, the association of enhanced DNA-damage repair with significant TP53 copy number gains (PMID: 27642012).

The Oncogenic Clinical Significance is used to capture evidence supporting an oncogenic or benign final classification of a somatic molecular profile (variant) at the Assertion level. In the case where evidence suggests a Molecular Profile has oncogenic properties, a curator will select Supports, and then Oncogenicity using the menus available on the Add Evidence form in CIViC (Figure 11). Importantly, evidence supporting a benign annotation will be captured during curation by choosing Does not support and then Oncogenicity in the menus available in the Add Evidence form.

The Oncogenic Evidence Item Significance relates either to cancer protectiveness or oncogenicity.
Figure 11: The Oncogenic Evidence Item (EID) Significance relates either to cancer protectiveness (left/green arrow) or oncogenicity (right/red arrow). The Evidence direction (Supports or Does Not Support) indicates whether the EID is pointing towards benign or protectiveness/oncogenicity effect.

Below is an example of an Evidence Item with an Oncogenic Evidence Type (Figure 12). This EID describes a study wherein KRAS Q61H was transfected into cells resulting in multilayered growth indicative of a loss of contact inhibition. Oncogenicity code OS2 is noted in the Evidence Statement, since the EID describes a well established in vitro experiment (focus formation assay), which supports an oncogenic effect for this variant.

Screenshot of an Oncogenic Evidence Item summary with Oncogenicity Code in Comment
Figure 12: Screenshot of an Oncogenic Evidence Item summary with Oncogenicity Code in Comment

Oncogenic Evidence Curation Practices
The Oncogenic Evidence Type describes literature-derived evidence pertaining either to a somatic molecular profile’s (variant’s) protective effects or its role in tumor formation, growth, survival or metastasis, as summarized by Hanahan and Weinberg in Hallmarks of Cancer. Disease type should be specified, as oncogenic effects may depend on cellular context (expression of a gene in a given tissue type, activity of the relevant pathway, etc.). For cases where a disease type is difficult to ascertain, such as experiments in highly de-differentiated cell lines, the Disease Ontology term ‘Cancer’ can be used. The Evidence Statement should contain a summary of the experiments or findings suggesting a protective, oncogenic, or benign effect.

The Oncogenic Evidence Item may be associated with Oncogenicity Codes developed by the Knowledge Curation and Interpretation Standards (KCIS) working group of the GA4GH VICC in collaboration with ClinGen working groups and Cancer Genomics Consortium (CGC) Oncogenicity codes assess oncogenicity of a given somatic variant in a mechanism similar to that used in the 2015 ACMG/AMP Guidelines for germline pathogenicity. Enumeration of Oncogenicity Codes derived from the literature along with a brief justification for the assignment of each code can be included in the Evidence Statement.

Currently application of ClinGen/CGC/VICC guidelines is restricte to Evidence Items associated to simple Molecular Profiles (MPs) which consist of only one variant. Complex MPs comprising more than one variant are out of the guideline scope. For example criteria utilizing cancerhotspots or COSMIC data are not well defined for co-occurring variants, as the variant frequencies are only reported for variants in isolation.

Functional Evidence Type
The Functional Evidence Type describes data from in vivo or in vitro experiments that assess the impact of a molecular profile (variant) at the protein level (often can be thought of a biochemical effect). Functional Evidence should be disease agnostic and if the Evidence being entered relies on disease or cell context, consider another Evidence Type. The Molecular Profile (variant) Origin for this Evidence Type is anticipated to primarily be N/A and entries should be classified under the Evidence Level of D - Preclinical. Variant impact on protein structure, folding, binding, activity, activation, phosphorylation, protein-protein interaction, sub-cellular localizatoin, and downstream pathway signaling are all examples of types of evidence that fall under the Functional Evidence Type. For variants in functional non-coding, impact might relate to things like RNA stability, folding, recognition of binding targets, etc.

Below is an example of a Evidence Item that describes a Functional Evidence Type (Figure 13). The authors performed an experiment to determine the impact of the variant on normal protein function related to cell cycle arrest. Expression of wildtype CDKN2A arrests the cell cycle in CDKN2A deficient cells, whereas expression of CDKN2A D108Y does not impact cell cycle progression in the CDKN2A deficient cells. These results indicate the innate ability of CDKN2A to arrest cell cycle progression has been lost as a result of the presence of the protein variant.

Screenshot of a Functional Evidence Item summary
Figure 13: Screenshot of a Functional Evidence Item summary

Functional Evidence Curation Practices
Functional Evidence Items describe how the molecular profile (variant) alters (or does not alter) biological function from the reference state. The Evidence Statement should include details on the experimental conditions (e.g., specification of cell type and/or model system, expression vector, vector entry system, and selection method) and the results related to the potential impact on function (including statistics, if applicable).

Significance for Functional Evidence Types adhere to the following rules related to Muller’s Morphs:

Gain of Function

A variant whereby enchanced/increased level of function is conferred on the gene product

Loss of Function

A variant whereby the gene product has diminished or abolished function

Unaltered Function

A variant whereby the function of the gene product is unchanged

Neomorphic

A variant whereby the function of the gene product is a new function relative to the wildtype function

Dominant Negative

A variant whereby the function of a wildtype allele gene product is abrogated by the gene product of the allele with the variant

Unknown

A variant that cannot be precisely defined by gain-of-function, loss-of-function, or unaltered function.

Functional Evidence Items may be used to support certain ACMG or Oncogenicity codes (e.g. PS3 or OS2 respectively). In these cases, the ACMG or Oncogenicity code should be listed in the Evidence Statement along with a brief justification for its inclusion. Functional Evidence Items may appear as supporting evidence for Predisposing or Oncogenic Assertions.

Curation Scenarios
The table below (Table 1) gives an in depth set of cases for assigning the Significance to an Evidence Item (EID) where either the “Supports” or “Does Not Support” Evidence Direction is used in combination with a Predictive/Therapeutic, Diagnostic or Prognostic Clinical Significance annotation.

Note that “Reduced Sensitivity” Clinical Significance is used to compare the molecular profile (variant) of interest to a known, sensitizing molecular profile. It is not used to compare the efficacy of one drug for a molecular profile against a different drug for the same molecular profile. In the latter case, the curator may simply make a Predictive evidence item which independently evaluates the efficacy of the drug against the molecular profile of interest.

The “Sensitivity/Response” annotation is used to assess sensitizing molecular profiles (variants), which are usually in the form of a primary sensitizing somatic mutation (e.g SNV, amplification, deletion, etc).

The “Resistance” annotation is used in situations where the molecular profile (variant) of interest has been observed to induce resistance in a context where, in the absence of the molecular profile, the system being assayed would be deemed sensitive which induce resistance to treatment (e.g. T790M mutation in cis with a background variant of EGFR L858R). In cases where a variant fails to induce sensitivity, then that molecular profile is best annotated with “Does not Support Sensitivity”.

Use cases for curation of Predictive, Diagnostic and Prognostic Evidence Items with different Evidence Direction, and in different contexts including primary and secondary mutations
Table 1: Use cases for curation of Predictive, Diagnostic and Prognostic Evidence Items with different Evidence Direction, and in different contexts including primary and secondary mutations.

A more readable version of Table 1 can be downloaded as a PDF here

Both Predictive and Prognostic evidence types may be obtained from the same data set in some cases. Figure 14, displayed below, gives hypothetical examples of predictive and prognostic structured annotation derived from patient data.

Examples for deriving Predictive and Prognostic Evidence Items (EIDs) from hypothetical clinical trial data.
Figure 14: Examples for deriving Predictive and Prognostic Evidence Items from hypothetical clinical trial data.

Curating Evidence from Clinical Trials
When curating evidence obtained from clinical trials performed with groups of patients, where data is pooled by mutation type (e.g. EGFR MUTATION), Level B clinical results may be obtained, which may report a statistically significant difference on a clinically relevant parameter such as partial response (PR) between wildtype vs. mutant patients. In addition, the publication may sometimes give outcomes on important individual patient parameters, such as variant, age, sex, best response, overall survival, etc. In these cases, this aggregate of data may be integrated into multiple Evidence Items in the following manner (The figure below is loosely based on a data set in CIViC obtained from PMID:21531810, which can be seen in CIViC on its Evidence Source page).

Obtaining Clinical and Case Study Evidence Items from clinical trial reports
Figure 15: Obtaining Clinical and Case Study Evidence Items from clinical trial reports

Statistical results may be obtained from the study to annotate a Categorical (sometimes colloquially called bucket) CIViC Molecular Profile (Variant), which pools together a category of sequence variants (for example EGFR MUTATION). Significantly longer progression free survival (PFS) may be observed in the mutant group (grouped under the Categorical CIViC Variant) vs. the wildtype group, when given a certain drug. In this case, this result may be reported in a CIViC Level B Evidence Item under the CIViC Categorical Variant EGFR MUTATION, with Evidence Direction and Clinical Significance “Suggests Sensitivity/Response” to the drug used.

When a sufficient level of individual patient detail is present, including the individual patient variants along with an important clinical parameter such as their best response, then this data set can be used to generate a set of CIViC Level C Evidence Items for the patients, each one associated with the respective CIViC Variant that was observed in the individual patient, along with the outcome. Note that even if the entire group showed statistically significant improvement with the Categorial Variant, this does not mean every patient did better, e.g. if a patient with variant X123Y had progressive disease as best response, then this would result in a Level C EID with Evidence Direction and Clinical Significane of “Does not support Sensitivity” for the CIViC Variant X123Y.

Complex Molecular Profiles in comparison to Categorical (Bucket) MPs
In the above examples, the Bucket MP EGFR Mutation is utilized. Other examples of Categorical (Bucket) MPs are ALK Fusion, or BRAF Amplification. These MP types create a category for, or bucket together a set of variants that is not simply enumerable, since there are in principle an unrestricted number of ways a variant can meet the criteria to be part of the bucket MP. In contrast, an MP such as BRAF V600E OR BRAF V600K can be easily enumerated as a complex MP of two elements. A more nuanced case could be the MP BRAF V600, which allows for any amino acid to occur at this position. While this can be enumerated with a 20 element complex MP, that would clearly be difficult to accommodate with the CIViC user interface, and also would not reflect the shorthand used by the field. Therefore, in cases like this, it is recommended to utilize the compact categorical MP notation, in this case BRAF V600.



Curating Assertions
The CIViC Assertion (AID) functions as a summary of clinical evidence for a Molecular Profile (variant), disease and specific predictive (therapeutic), prognostic, diagnostic or predisposing clinical significance supported by Evidence Items (EIDs) appearing in CIViC, along with evidence drawn from other sources, such as databases of variant population frequency. The Assertion is designed to incorporate information from practice guidelines (e.g., NCCN) and also integrates widely adopted clinical tiering systems into structured fields, including:

AMP-ASCO-CAP guidelines (Li et al. 2017) for clinical tiering of somatic variants (Predictive, Prognostic, Diagnostic assertions).

ClinGen/CGC/VICC SOP (Horak et al. 2022) for classification of somatic variant oncogenicity (Oncogenic assertions).

ACMG-AMP guidelines (Richards et al. 2015) for classification of germline variant pathogenicity (Predisposing assertions).

Overview of an Assertion summary view
Figure 1: The Assertion contains a brief one sentence summary and a longer Assertion Description. It also displays the CIViC Molecular Profile to which it applies. The bottom of the Assertion view shows a list of CIViC Evidence Items (EIDs) which support the Assertion. Selecting any supporting EID opens up that EID page.
Assertion fields
Figure 2: Fields in the Assertion
The Assertion contains a one sentence Assertion Summary which states the specific Molecular Profile (MP), disease, and significance with therapy if applicable (e.g. “Non-small cell lung cancer with EGFR L858R mutation is sensitive to erlotinib or gefitinib” in Figure 1 above).

Beneath the Summary is the Assertion Description, which contains background clinical information specific to the Molecular Profile (MP), disease, and predictive (therapeutic), prognostic, diagnostic or predisposing significance. EIDs supporting the Assertion’s clinical significance may be listed in this description, and referenced using CURIE identifiers (e.g., civic:EID1234). For Assertions with a higher AMP-ASCO-CAP Tier (Li et al. 2017), the Assertion Description section should list major practice guidelines and approvals associated with the clinical significance. For therapies, this may contain a brief restatement of guideline recommended treatment line and cancer stage (e.g. “NCCN guidelines recommend (category 1) erlotinib and gefitinib for NSCLC with sensitizing EGFR mutations, along with afatinib and osimertinib.” in Figure 1)

Add Assertion form screenshot
Figure 3: The Assertion submission form is accessible by selecting the Add button at the upper right corner of the user interface. All editable fields of the Assertion are available in this view. Curators can associate Evidence Items (EIDs) with the Assertion at the bottom of the page, either by adding Evidence Items using the EID number, or by using the Evidence Manager, which can perform filtering on the provided fields (e.g., EID, Therapy, Molecular Profile) and selecting the check box at the left of the Manager window.

The CIViC Assertion is supported by CIViC Evidence Items (EIDs) which describe the same Molecular Profile, disease and significance as the given Assertion. The Assertion may also be supported by EIDs written for a more generalized MP. For example an Assertion regarding erlotinib sensitivity of EGFR L858R lung cancer may be supported in part by EIDs written for a more general MP such as EGFR Mutation which utilizes the categorical/bucket variant “Mutation”. Note that an Assertion for a specific MP such as EGFR L858R cannot be entirely supported by EIDs based on more general variant types such as Mutation, and requires some supporting EIDs Molecular Profiles based on the same specific variant type. Similar principles apply to the Disease, where an Assertion for a specific disease type may in part be supported by EIDs for a more general disease class (e.g. Cancer, DOID 162). Note that cited guidelines should be disease specific.

A sufficient amount of evidence should be added to an Assertion so that the collection of Evidence Items represents the ‘state of the field’ for the Disease, Molecular Profile, and Clinical Significance. As new evidence emerges which is relevant to a CIViC MP with an accepted Assertion, then additional Evidence Items can be curated from this new evidence, and added to the Supporting EIDs for the existing Assertion, potentially changing its ACMG-AMP classification or AMP-ASCO-CAP Tier and Level.

CIViC Assertion curation by Assertion Type
Figure 4: CIViC Assertion curation by Assertion type

CIViC Assertions summarize a collection of Evidence Items, along with certain evidence drawn from sources other than publications or meeting abstracts, which together reflect the state of literature and clinical knowledge for the given Molecular Profile and disease. For Assertion Types dealing with actionable clinical information (Predictive/Therapeutic, Prognostic, or Diagnostic), AMP-ASCO-CAP 2017 guidelines are followed to associate the Assertion with an AMP Tier and Level. For the highest tier Assertions, this involves consideration of practice guidelines as well as regulatory approvals for drug use in the specific context of the variant and disease. In the absence of explicit regulatory or practice guidelines, the supporting clinical and case study Evidence Items should be used to guide application of AMP Tier and Level (Figure 4A).

Lower AMP-ASCO-CAP Tier Assertions can be written for Molecular Profiles that are not supported by practice guidelines or extensive clinical evidence, relying on case study and preclinical data. The supporting EIDs should reflect the state of the field regarding the emerging knowledge in such cases, and AMP Tier should be assigned based on the curator and editor’s overviews of the field. It is recommended to consult recent reviews in this case.

CIViC Predisposing Assertions utilize ACMG-AMP 2015 guidelines to generate a 5-tier pathogenicity valuation for a variant in a given disease context, which is supported by a collection of CIViC Evidence Items, along with other data. ACMG evidence codes for an Assertion are supplied by a collection of supporting CIViC Evidence Items (e.g., PP1 from co-segregation data available in a specific publication), and additionally are derived from variant data (e.g., PM2 from population databases such as gnomAD). ACMG evidence codes are then combined at the Assertion level to generate a disease-specific pathogenicity classification for the Assertion (Figure 4B and Figure 8). CIViC Oncogenic Assertions work in a very analagous way but follow the ClinGen-CGC-VICC 2022 SOP.

Other guidelines that curators should keep in mind include:

While the body of supporting Evidence Items may be derived from studies with differing patient populations with regard to stage and line of treatment, as well as preclinical studies in disease models, the Assertion may describe more specific disease context based on reading of practice guidelines (e.g. NCCN etc), and any such descriptions added to the Assertion should explicitly cite the practice guidelines as the source.

Generally, even when the supporting Evidence Items exactly line up with the treatment context described in the Assertion, practice guidelines may be summarized in the Assertion description, including disease stage, line of treatment (e.g., first line, salvage), and this information should be clearly labeled as being derived from published guidelines, and those guidelines explicitly cited.

Approved companion diagnostics (e.g. Vysis Break-Apart Fish diagnostic for ALK-fusions) may be listed in the Assertion Description.

All Evidence Items relevant to the Assertion should be associated to it, even if they disagree with the Assertion Summary. Disagreements can be discussed in the Assertion Description section and the rationale for discounting discrepant evidence should be recounted.

The CIViC Assertion contains specific Variant Origin fields which are filled out during Assertion creation. It is possible for some EIDs in the supporting evidence to have a different Variant Origin than that in the Assertion, but the Assertion should contain substantial support from Evidence Items with the same Variant Origin as in the Assertion.

Predictive Assertions
The Predictive Assertion screenshot below (Figure 5) describes that BRAF V600E confers sensitivity to combination therapy of dabrafenib and trametinib for patients with melanoma. The AMP-ASCO-CAP Category is Tier I - Level A for this variant, disease and drug sensitivity assertion. The high AMP-ASCO-CAP Tier is a consequence of the presence of this Molecular Profile and treatment in the Melanoma NCCN Guidelines (v2.2018).

Screenshot of AID7, a predictive assertion
Figure 5: Screenshot of a predictive Assertion, AID7.

Curation Practices for Predictive Assertions
Predictive Assertions are generally associated with Molecular Profiles based on somatic variants. Still some germline variants may have pharmacogenomic properties that predict an adverse response to a treatment. In these cases, Predictive Evidence Items and an Assertion can be created for MPs based on these types of germline variants, with the Significance being Supports Adverse Response.

Prognostic Assertions
Figure 6 shows a Prognostic Assertion with an exemplary Assertion Summary and Assertion Description. In this example, the Assertion describes that the BRAF V600E Molecular Profile confers poor outcome for patients with colorectal cancer. This variant is listed in the NCCN Guidelines for colorectal cancer (v2.2017), and falls under the Tier I - Level A AMP category.

Screenshot of AID20, a prognostic assertion
Figure 6: Screenshot of a prognostic Assertion, AID20.

Curation Practices for Prognostic Assertions
Prognostic Evidence Items in CIViC describe a Molecular Profile (MP) being associated with better or worse patient outcome in a general manner, independent of any specific treatment. Evidence should show better or worse outcome in the presence of the MP, ideally under different treatment regimes and also in untreated cases if such data is available. Therefore, a larger collection of evidence showing similar prognostic outcomes under a range of different treatment or untreated regimes creates a stronger Prognostic Assertion.

Diagnostic Assertions
Figure 7 shows an example of a Diagnostic Assertion with an exemplary Assertion Summary and Assertion Description. In this example, the Assertion describes how an in-frame fusion between DNAJB1 and PRKACA can be used to diagnose a specific subtype of hepatocellular carcinoma (HCC). Presence of this fusion can be used to clarify that the patient has fibrolamellar HCC.

Screenshot of AID24, a diagnostic assertion
Figure 7: Screenshot of a diagnostic Assertion, AID24.

Curation Practices for Diagnostic Assertions
All Evidence Items relevant to the Assertion should be associated with it, even if they disagree with the Assertion Summary. Disagreements can be discussed in the Description section and rationale for discounting discrepant evidence should be recounted.

The evidence supporting the Assertion should sufficiently cover what is known regarding the diagnostic power for the Molecular Profile in the specific disease context.

For Tier I Level A Diagnostic Assertions, details from relevant practice guidelines should be given, along with any additional specific information which is applicable (e.g., disease stage).

Lower Tier and Evidence Level Assertions may be created for Diagnostic CIViC Variants not currently in practice guidelines. Molecular Profiles backed by stronger clinical data may be Tier I Level B as above. Variants with smaller amounts of evidence for diagnostic potential will receive lower Tiers and Evidence Levels (Figure 4A).

Predisposing Assertions
Figure 8 shows an example of a Predisposing Assertion. In this example, an inframe deletion repeatedly observed in the literature is considered pathogenic for Von Hippel-Lindau Disease. Utilizing the ACMG/AMP guidelines [8], evidence codes were assembled from the literature (PS2, PP1) and Variant-level information (PM2, PM4) to be categorized as Pathogenic. Specific evidence is associated with codes in the Description and all evidence evaluated when producing the Assertion is associated with the Assertion.

Screenshot of AID17, a predisposing assertion
Figure 8: Screenshot of a predisposing Assertion, AID17.

Curation Practices for Predisposing Assertions
ACMG-AMP codes (Richards et al. 2015) supporting the Predisposing Assertion are derived from supporting Evidence Items, and other sources such as population databases (See Figure 4B). Any evidence codes applied should be explained in the Description section, allowing others to rapidly re-evaluate the evidence used.

All Evidence Items relevant to the Assertion should be associated, even if they disagree with the Assertion Summary. Disagreements can be discussed in the Description section and rationale for discounting discrepant evidence should be recounted.

Thoroughly evaluated Assertions can have a Significance of Variant of Unknown Significance (VUS) using ACMG-AMP criteria. This permits other users to quickly re-evaluate this variant in the context of new evidence, potentially leading to reclassification, but reducing future curation burden if the variant is observed again.

Note that currently ACMG/AMP criteria apply to simple (single variant) Molecular Profiles. Multiple ACMG criteria are not forumlated for groups of co-occuring variants accross different genes. For example PM1 (Located in a mutational hot spot and/or critical and well-established functional domain) is not clear wether this would be required of one or all of the variant members of a complex MP. PP1 (Cosegregation with disease in multiple affected family members in a gene definitively known to cause the disease) is also clearly not defined for combinations of varinats. Therefore, the Predisposing Assertion should only be forumlated for simple Molecular Profiles.

Oncogenic Assertions
The Oncogenic Assertion (Oncogenic AID) summarizes a collection of Evidence Items (EIDs) for a somatic variant, which together should reflect the state of knowledge in the field for this variant to reach a final oncogenic or benign classification. Oncogenic properties are interpreted as effects induced by the collection of variants which make up the Molecular Profile, that in turn promote one or more of the Hallmarks of Cancer. Benign properties indicate a lack of oncogenic effect for a somatic variant, which ideally will be demonstrated in the context of well defined positive controls. This collection of EIDs can then be summarized into a CIViC Oncogenic Assertion (Figure 9).

Oncogenicity Codes classify a variant using a 5-tier evaluation.
Figure 9: Oncogenicity Codes from the ClinGen/CGC/VICC Guidelines may be used to classify a simple Molecular Profile (single variant) using a 5-tier evaluation consisting of Benign, Likely Benign, Variant of Unknown Significance (VUS), Likely Oncogenic, or Oncogenic (Figure 10).

Oncogenic Assertion Clinical Significance Classifications based on score.
Figure 10: Oncogenic Assertion Clinical Significance Classifications based on score.

The selection of Assertion Type in CIViC results in a particular choice of variant classification based on the aggregation of evidence codes (Figure 11). For Oncogenic Assertions, after the Oncogenic AID Type is chosen, the ClinGen/CGC/VICC Oncogenicity Codes can be added to the Assertion (Figure 12). This guideline is based on missense and simple insertion/deletion variants, so when curating, only simple Molecular Profiles are used. In some cases, ClinGen Somatic Variant Curation Expert Panels (SC-VCEPs) may choose N/A for evidence code, and instead utilize an SC-VCEP specific protocol for evaluation of oncogenicity. This protocol should be described in the Assertion Summary.

Five Assertion types are available which are associated with different guidelines.
Figure 11: Five Assertion types are available. AMP/ASCO/CAP Guidelines are used for tiering Predictive, Diagnostic, and Prognostic Assertions. Predisposing Assertions utilize the ACMG/AMP Guidelines. Oncogenic Assertions incorporate the ClinGen/CGC/VICC Guidelines, and users may also choose N/A for evidence code, and then utilize an approved alternate oncogenicity guideline for Assertion creation, such as guidelines for oncogenic tiering of NTRK fusions under development by the ClinGen NTRK somatic cancer variant curation expert panel, or other guidelines under development by ClinGen SC-VCEPs.

Oncogenic Assertions utilize the ClinGen/CGC/VICC 2022 Guideline.
Figure 12: When curating Oncogenic Assertions utilizing the ClinGen/CGC/VICC 2022 Guideline, a menu of ClinGen/CGC/VICC Codes are made available from which the curator may choose one or more codes.

Curation of Oncogenic Assertions requires a brief Summary of the main conclusion of the Assertion. In the Assertion Description the curator should describe generally relevant information about the Molecular Profile’s oncogenic or benign properties, and importantly, describe how the appropriate guideline was used to arrive at the Clinical Significance, which is Likely Benign in the example below (Figure 13). Additionally external information such as population frequencies or data contradictions can be described here. The ClinGen/CGC/VICC Codes are added by the curator in the Add Assertion form, and a brief explanation for each Code used is given in the Assertion Description. For Codes that are derived from Evidence Items, the appropriate Curie link is also added by the curator (e.g., civic.EID:10277). The Disease field is required, and the term Cancer (DOID 162) may be used when the underlying evidence applies more generally.

Example Oncogenic Assertion.
Figure 13: Example Oncogenic Assertion.
Note that currently, ClinGen/CGC/VICC criteria are not well defined for complex Molecular Profiles (MPs), and therefore are restrocted to simple (single variant) Molecular Profiles. For example criteria utilizing cancerhotspots or COSMIC data are not well defined for co-occurring variants, as the variant frequencies are only reported for variants in isolation. Therefore Oncogenicity Assertions based around the ClinGen/CGC/VICC guidelines should only be curated for simple MPs. Future guidelines may allow for Oncogenicity Assertions based around complex MPs.

Curators should take note that the Significance of the Oncogenic Assertion (AID) and that of the Oncogenic Evidence Item (EID) do not overlap and instead consist of partially related but different annotations (Figure 14). This also holds for the Predisposing Evidence Item versus the Predisposing Assertion. EIDs provide discrete evidence from a single source and do not represent a final classification, only supporting evidence. The Assertion Significance provides a final classification as a result of the aggregation of information across studies for the variant (Simple Molecular Profile) (i.e., multiple EIDs and other evidence). The Oncogenic EID is set up on two opposing axes describing Protectiveness and Oncogenicity. The Oncogenic Axis is able to capture evidence supporting either a benign or an oncogenic effect for the Molecular Profile (Simple or Complex), but only in rare cases will a single publication or meeting abstract yield enough evidence to obtain a classification of Oncogenic or Benign utilizing the ClinGen/CGC/VICC Guidelines. Because of this, Single EIDs are tagged with Oncogenicity Codes when appropriate, and used to support an overall Assertion (Figure 9). Importantly, note that an Oncogenic EID that utilizes the Protective Significance will have no analog at the level of Assertion. Also note that, currently, only Simple Molecular Profiles (single Variant) are supported for Oncogenic or Predisposing Assertions as the corresponding guidelines were not designed for Complex MPs.

Oncogenic Evidence in contrast to the Oncogenic Assertion.
Figure 14: Oncogenic Evidence in contrast to the Oncogenic Assertion.
Citing EIDs in Assertions
As described above, EIDs supporting the Assertion’s clinical significance may be listed in Assertion description, and referenced using CURIE identifiers (e.g., civic:EID1234). However, there is no simple/specific answer for how many and which EIDs to cite. It varies with the AID type and complexity. Curators should use their judgement but consider citing EIDs as similar to citing supporting works in a scientific publication. The following suggestions may help:

Do not simply cite all EIDs (they are already associated with the AID). Cite specific EIDs that will help editors or eventual readers of the assertion. Focus on strategic citations that help the end user.

The practice of strategically citing a few EIDs may be more useful where there is a larger number of EIDs associated with an AID, but not as critical if there are only 1-3 EIDs.

Examples of situations where you might want to cite specific EIDs in an AID include:

If certain EIDs support specific aspects of the assertion (particularly when describing support for specific standard evidence codes)

To draw extra attention to EIDs that are considered particularly critical or high quality.

When describing specific nuances, contexts, controversies that might influence interpretation of the EID.

When there is a heterogeneous mix of evidence supporting an overall assertion. For example, there are 10 EIDs. Some correspond to functional data, to case reports, and clinical trials. Maybe cite 1-2 key EIDs for each of these evidence types.

When evaluating evidence in the context of a guidelines (such as oncogenicity SOP or Fusion oncogencity SOP), it is often the case that evidence is found to support 4-5+ distinct evidence lines. If these are drawn from 15-20 evidence items it can be a lot of work for the reviewer to figure out which EIDs support which codes.

From a stylistic perspective, we anticipate that a short assertion will typically refer strategically to at least 1-2 EIDs. A longer assertion might have more.




Curating and Suggesting Sources
All curated CIViC Evidence, Assertions, Molecular Profile Summaries, and Gene Summaries are based on peer-reviewed sources from the biomedical literature, currently limited to those publications indexed in PubMed, the ASCO Meeting Library or ASH Meeting Abstracts in the Journal Blood. As soon as any publication is cited in CIViC, a separate Source Record is created and can be browsed or searched within the CIViC knowledgebase. Each Source Record includes details about the publication such as title, authors, abstract, and journal, as well as a table linking to all CIViC evidence curated for that Source. Comments can be added to any Source Record at any time. Source comments are a useful place to document general or specific notes to aid current and future curation. For example, if a source has an overlapping patient population with another study already curated within CIViC, this can be documented in the comments. In other cases, the reference sequence used for determining variant coordinates might be recorded to help future curators understand variant nomenclature used by that publication.

The direct submission of a “Source Suggestion” for future consideration and curation is an essential, yet simple, curation task. Once a manuscript containing clinically relevant cancer variant data is identified, a curator uses the Add -> Source Suggestion form, selects a Source Type (PubMed, ASCO or ASH) and then enters a PubMed ID, ASCO Web ID or the DOI for the ASH Abstract. A comment must be included describing the relevance of this source to CIViC. The objective of the comment is to aid curators in selecting the suggested source for review and curation. Ideally, the comment will offer a brief summary of general study details and results. Optionally, a curator may also “pre-curate” the Gene Name, Molecular Profile (one or more Variants), and Disease described by the source. More than one Source Suggestion can be made for a single source. For example, multiple lines of evidence might be proposed for curation for multiple genes, molecular profiles (variants), or diseases from the same publication. After submission, a Source Suggestion can be accessed from the Source Suggestion Queue or through the source’s individual Source Record Page. Each Source Suggestion can be curated using the ‘Add Evidence Item’ action, which activates the Add Evidence form and pre-populates with any gene, molecular profile (variant), or disease details pre-curated for the source. After each Source Suggestion has been curated, curators can use the “Mark Suggestion as Curated” action. Once all Source Suggestions for a Source have been marked as curated, the Source itself attains a status of “Fully Curated”. Lastly, if upon review a Source Suggestion is determined to be unsuitable for curation in CIViC, the Source Suggestion is rejected using the “Reject Suggestion” action.


Prioritizing Curation Effort
New CIViC curators, commonly ask where they should focus their efforts and where can they find evidence of the significance of cancer variants. There are many approaches and relevant resources that may help to identify and prioritize such evidence.

Remember that the focus of CIViC is on the clinical relevance of cancer variants, which CIViC describes using Molecular Profiles (MPs) - collections of one or more variants, associated to one or more genes. Before expending the effort to propose an addition to CIViC, ask yourself would a clinician potentially find this information useful in understanding and treating a patient’s cancer? Could an oncologist use this evidence to better understand likely response to therapy (Predictive evidence), or outcome (Prognostic) for their patient? Would a pathologist or genetic laboratory director find knowledge of the Molecular Profile (variant) valuable in classifying (Diagnostic) the tumor into a subtype? Would a medical geneticist or genetic counselor be interested in the causative (Predisposing) significance of this evidence? Does the variant occur in a gene of known significance to cancer (in this case a single variant, simple Molecular Profile)? Will determining the Oncogenic or Functional potential of the Molecular Profile help to interpret its potential clinical relevance?

In addressing these questions, try to think about the distinction between the relevance of a Molecular Profile (MP) to cancer biology and its relevance in a clinical setting. An MP may have great and diverse relevance to the biology of a cancer cell but have limited or no clinical applicability. For example, TP53 mutations are critical in many cancers and hundreds (if not thousands) of papers have been written about their complex roles in cancer biology. However, the scenarios in which TP53 mutations are clinically relevant are much, much narrower. An MP may NOT be clinically relevant despite being characterized as functional (gain or loss of function), a ‘driver’, ‘recurrent’, etc. In some, perhaps most cases, the clinical relevance of these MPs may simply not be established yet. However, CIViC is about the evidence that establishes their clinical relevance. By contrast, in some cases, the biological relevance may be poorly understood while clinical utlity is established. Such evidence does belong in CIViC. A mechanistic understanding is highly desirable, but not strictly required.

The above description is an oversimplification. The concept of clinical utility varies by Evidence type: Predictive, Prognostic, Diagnostic, Predisposing, Oncogenic and Functional. The “ideal” clinical interpretation and definition of clinical utility are open to debate. We welcome this debate and one of the goals of CIViC is to enable and capture it. If you believe some evidence is relevant to CIViC but have some doubts, please submit it so that the community can discuss with you.

The following list is not exhaustive but provides many examples of approaches to identify high quality evidence. If you know of a useful resource that is not listed below, please let us know about it. NOTE: some of these resources are open access, others are not. When entering evidence into CIViC, never copy content or ideas from another resource. Your contributions to CIViC should be based on published evidence, but in your own words.

Example sources of CIViC evidence and high priority variants

Published results from clinical trials involving cancers with specific variants (e.g. HER2 +ve breast cancer)

Published evidence for the arms of basket clinical trials (e.g. NCI-MATCH, ASCO-TAPUR, I-SPY2, BATTLE-1, BATTLE-2, CUSTOM, etc.).

A gene, variant, simple or complex Molecular Profile, or paper, that you are an expert in. For example, this might be work from your own research/practice.

Public discussions on cases submitted to the ASCO Molecular Oncology Tumor Board

The CIViC publication queue, a place were CIViC curators add and discuss papers thought to contain valuable evidence.

We created a ranked list of relevant genes, based on a comprehensive survey of genes that are targeted by dozens of assays in clinical use.

We also created a ranked list of relevant publications by summarizing overlap between the publications used in CIViC and other companion resources.

Our colleagues at the BC Cancer Agency and Glasgow University have developed a natural language processing approach and resulting database of automatically mined CIViC relevant publications called: CIViC-mine.

Treatment guidelines (e.g. NCCN guidelines, ASCO guidelines, ESMO guidelines, etc.).

Molecular Profiles (variants) and papers referenced in other open access databases such as ClinVar and OMIM.

Companion resources of CIViC participating in the GA4GH Variant Interpretation for Cancer Consortium (VICC) or others such as: PMKB, OncoKB, MyCancerGenome, CanDL, BaseSpace KN, Cancer Genome Interpreter, COSMIC, PCT, PharmGKB. A detailed comparison of these resources can be found in the CIViC Related Resources Table. While these resources can be used for inspiration, do not plagiarize/copy any content from these sources that might violate their copyrights.

Papers referenced by the Atlas of Genetics and Cytogenetics in Oncology and Haematology

Keyword searches in PubMed or Google Scholar

Papers from certain topical journals. The most cited journals in CIViC are summarized on the CIViC Source Statistics page

Variants and related papers from the Sarcoma Initiative.

Variants from the LOVD project.

Example Curation Activities
Most of the contents of CIViC are curator generated and edited. Below are a few examples of areas where curators are needed, culminating in a list of bite sized curation tasks that should require less than 3 minutes of your time.

1. Adding Evidence

Evidence records are the heart of the CIViC resource. Each corresponds to evidence for a single clinical assertion about a molecular profile (single variant or combination of variants) in a single cancer type. Each evidence record is based on a single citable source (e.g. a peer-reviewed publication). The evidence record consists of a free-form executive summary describing the assertion and supporting evidence for it, and additional structured fields that describe the evidence (e.g. evidence type, relevant therapy, etc.). To learn more about the elements of an evidence record refer to the Evidence help docs. For suggestions on where to find sources for evidence records, refer to the Source Ideas tab of this section. To add a new evidence record, you must login and hit the “ADD” button at the top of any page throughout the site.

2. Adding or improving Molecular Profile, Variant Group, and Gene Descriptions

Once sufficient evidence accumulates for a molecular profile (single variant or combination of variants), variant group or gene entity, a summary description should be created. The summary should be an overview of the evidence records associated with the entity. The summary should focus on the most clinically actionable evidence and should summarize for each relevant gene what a clinician should be aware of for patients with a particular variant, or variants in a particular gene. Very brief background material may be included. Additional citations beyond those associated with the evidence records can be associated directly with the summary using the “Add Source” option in the edit form. To learn more about each major CIViC entity, refer to the Molecular Profiles, Variant Groups, and Genes sections of the help pages.

3. Adding or improving Assertions

An important final product of the CIViC curation process is the Assertion. Gene and Molecular Profile Summaries (described above) provide an overall summary of the clinical relevance of genes and molecular profiles as documented by the entire body of CIViC evidence. In contrast, Assertions provide a consensus of the significance (and supporting evidence) for a specific gene-molecular profile, in a specific disease context. The assertion should represent the current state of understanding in the field and be associated with the appropriate AMP tier or ACMG codes and assessment for the molecular profile. Once sufficient evidence has been documented, a new assertion can be submitted using the “ADD” button at the top of any page throughout the site. Reviewed and accepted assertions enter the queue for submission to ClinVar. Creating assertions is one of the most advanced curation tasks in CIViC.

4. Editing CIViC Content

CIViC content can be edited by clicking on the “Revise” button in the top right of any editable page. Gene, Molecular Profiles, Variant, Variant Group and Evidence entities can all be edited. These edits may be expansive major updates to incorporate new evidence, error corrections, improvements to readability and style, or minor grammar and typo fixes. All such edits are welcome.

5. Comment on CIViC Content

Throughout the website are “Comment” tabs where users can comment on the current contents of CIViC (specific Evidence, Molecular Profiles, Variants or Genes) or on Revisions. Curators are encouraged to be verbose in their comments on existing content. Critism, clarification, qualification, and questions are all appropriate. Comments from the authors of work being summarized or others with particular expertise in the area are especially desirable. When adding new evidence or summaries, comments may be used to describe the thought process of the curator. Small quotes (as allowed by the Fair Use doctrine) from source publications that support a submission may also be included (but please indicate these with quotes or use the block quote style).

6. Molecular Profile Description

The Molecular Profile (MP) page contains a Description that is written by curators, and should summarize the main ideas from the Evidence Items (EIDs) associated to the MP. The Description also allows for the citing of source publications used to incorporate other relevant information for the role of the MP in cancer.

7. Variant attributes

A Molecular Profile consists of combinations of one or more variants. Each variant also has its own page in CIViC. Variants have several structured values associated with variant records. These include:

Aliases. Alternative names (synonyms) for the variant. For many variants, researchers from different groups may refer to variants by different names. Multiple and varying abbreviations or identifiers exist for most variants. A variant alias is generally any name that might help CIViC users determine the various ways used to indicate the same variant.

HGVS expressions. CIViC supports and promotes variant identification using the Sequence Variant Nomenclature guidelines of the Human Genome Variation Society (HGVS), otherwise known as ‘HGVS strings’. Curators may add one or more valid HGVS values for each variant. These may be entered in protein (p.), cDNA (c.), or genomic (g.) format. A particular CIViC variant (e.g. BRAF V600E) may have multiple valid genomic alterations that could create it, each with a distinct genomic HGVS expression. Similarly, multiple cDNA HGVS strings may correspond to multiple transcript sequences, possibly from various transcript annotation databases (e.g. Ensembl, RefSeq, LRG, etc.) or alternative isoforms of a gene.

Coordinates. For each variant, the goal of CIViC initially is to determine unambiguous genomic coordinates for an example instance of the variant. For instance, if the paper refers to the variant as “V600E”, the curator determines for a particular build of the human genome, the corresponding chromosome, start position, end position, reference base and variant base. Refer to the Variants documentation on the left for more details.

8. Bite-size curation tasks

Only have a few minutes? Tackle one of the tasks below.

Suggest a Source.

Identify a publication containing a variant with clinical relevance.

Visit PubMed to identify the publication’s PubMed ID.

Enter as much information as possible to help curators. This form only requires 2 elements: PubMed ID and a comment to direct curators as to why you believe this publication has clinically-relevant information about a variant.

Your suggested source can be seen in the Source Suggestion Queue or by searching for the publication in the Source Advanced Search to find the dedicated CIViC publication page.

Add a variant Alias.

Browse for variants you are familiar with using our Browse or Advanced Search pages.

Read a summary for your favorite gene/variant and comment on the contents.

Use the Browse or Advanced Search pages to find your variant or gene of interest.

Use the Activity Page to view recent activity. Clicking on any event will direct you to that event.

CIViC Knowledge Model
This section describes the details of the knowledge model that CIViC uses to organize variant interpretations, evidence, assertions and associated information about therapies, disease type, etc. Each major entity is detailed in the sections below, with each attribute of that entity detailed within its own page (roughly).

Contents:

Evidence Items
Evidence Overview
Gene
Molecular Profile
Statement
Evidence Level
Type
Direction
Significance
Origin
Disease
Therapy
Associated Phenotype
Source
Clinical Trial
Evidence Rating
Assertions
Assertions Overview
Fields Shared with Evidence
Associated Phenotypes
NCCN Guideline
FDA Companion Test
Summary and Description
Molecular Profiles
Molecular Profiles Overview
Name
Aliases
Description
Molecular Profile Score
Variants
Variants Overview
Name
Aliases
My Variant Info
Types
Coordinates
HGVS Expressions
ClinVar IDs
Genes
Gene Name
Summary
MyGene.info
Variant Groups
Summary
Sources
Source Types


vidence Items
At the heart of CIViC is the clinical evidence statement. The clinical evidence statement is a piece of information that has been manually curated from trustable medical literature about a molecular profile (variant) or genomic ‘event’ that has implications for protein function, oncogenicity, cancer predisposition, diagnosis (aka molecular classification), prognosis, or predictive response to therapy. For example, “Patients with BRAF V600 mutations respond well to the drug dabrafenib”. A molecular profile is comprised of one or more variant(s) which may be a single nucleotide substitution, a small insertion or deletion, an RNA gene fusion, a chromosomal rearrangement, an RNA expression pattern (e.g. over-expression), etc. Each clinical evidence statement corresponds to a single citable publication.

Evidence Items follow a structured knowledge model with required fields: Molecular Profile Name (Gene/Variant), Source, Variant Origin, Disease, Evidence Statement, Evidence Type, Evidence Level, Evidence Direction, Significance, and Trust Rating) with additional optional fields (Associated Phenotypes, etc). For some Evidence Types, additional required or optional fields become available (e.g., Predictive Evidence Types require a Therapy/Drug Name).

Contents:

Evidence Overview
Gene
Curating Genes
Molecular Profile
Statement
Understanding Evidence Statements
Curating Evidence Statements
Evidence Level
Understanding Evidence Levels
Curating Levels
Type
Understanding Evidence Types
Direction
Understanding Evidence Direction
Curating Evidence Direction
Significance
Understanding Significance
Origin
Understanding Variant Origin
Curating Variant Origin
Disease
Curating Diseases
Therapy
Curating Therapies
Associated Phenotype
Curating Associated Phenotypes
Source
Understanding Source
Curating Source
Clinical Trial
Evidence Rating
Understanding Evidence Ratings
Curating Evidence Ratings

Evidence Overview
The following figure shows the attributes of a CIViC Evidence Item, and the options or values available for each.

Figure depicting the CIViC Evidence Item's attributes and associations
Figure 1: Evidence Item Attributes and Associations
The rows in the following table describe the minimal components of a CIViC Evidence Item. Several Evidence Statements are synthesized at the Molecular Profile (Variant) level into a Molecular Profile Description. However, each Evidence Statement is directly linked to a single article in PubMed or ASCO/ASH abstract. More specific guidelines about Evidence Item components can be found in the additional sections outlined in the table of contents.

Evidence Attributes

Attribute

Description

Example

Source

Molecular Profile

Gene and Genomic event(s)/mutation(s) (e.g., Single nucleotide variant, Insertion/deletion, Gene fusion, Copy number variant, etc.) implicated. May be a simple comprised of a single variant or a more complex combination of variants.

ESR1 Y537S

CIViC

Statement

Human readable interpretation. Free-form text summary of this molecular profile’s potential clinical interpretations. This interpretation is the synthesis of all other information about the alteration(s) and its clinical relevance and should be the living product of active discussion.

In this study of 178 non-small cell lung cancer patients, the appearance of EGFR T790M mutation led to resistance to gefitinib.

CIViC

Evidence Level

The type of experiment from which the evidence is curated. From inferential, to proven association in clinical medicine. Refer to the additional documentation on evidence levels for definitions of the five levels allowed in CIViC: validated, clinical, pre-clinical, case study, and inferential.

Level B - Clinical Evidence.

CIViC

Type

Category of clinical action/relevance implicated by event. Refer to the additional documentation on evidence types for details on how to enter evidence of each of the six types: Predictive, Prognostic, Diagnostic, Predisposing, Oncogenic and Functional. See ‘Evidence Type’ tab for more information.

Predictive - The molecular profile (one or more variants) is predictive of sensitivity or resistance to a therapeutic.

CIViC

Direction

An indicator of whether the evidence statement supports or refutes the significance of an event. See ‘Evidence Type’ tab for more information.

Supports - the evidence supports the significance.

CIViC

Significance

The impact of the molecular profile (one or more variants) for predictive, prognostic, diagnostic, oncogenic or functional evidence types. See ‘Evidence Type’ tab for more information.

Resistant or Non-response - mutation is associated with resistance to therapy.

CIViC

Origin

Presumed cellular origin of the Variant in samples from the literature citation where the effect of this Variant is being evaluated.

Somatic

CIViC

Disease

Specific disease or disease subtype that is associated with this event and its clinical implication. Links directly to Disease Ontology.

Estrogen-receptor positive breast cancer (DOID: 0060075).

CIViC (Disease Ontology)

Associated Phenotype

Specific phenotypes associated with the evidence statement.

Pancreatic cysts (HP:0001737).

The Human Phenotype Ontology (HPO)

Therapy

For predictive evidence, indicates the therapy for which sensitivity or resistance is indicated (With NCIt ID if available).

Tamoxifen, Raloxifene (NCIt IDs: C62078, C62078).

CIViC (NCIt)

Therapy Interaction Type

For predictive evidence involving more than one Therapy, specifies the relationship between the therapies (usually drugs) by indicating whether they are Subtitutes for each other or are used in Sequential or Combination treatments.

Substitutes - The therapies listed are often considered to be of the same family, or behave similarly in a treatment setting.

CIViC

Citation

Publication where the event was described/explored automatically generated from curator-provided PubMed ID and links to internal CIViC publication page showing all Evidence Items from the publication.

Toy et al., 2013, Nat. Genet. (PMID: 24185512)

CIViC (PubMed)

PubMed ID

PubMed ID for publication where the event was described/explored with direct link to PubMed.

24185512

CIViC (PubMed)

Clinical Trial

Clinical trial associated with the evidence item.

NCT01154140

ClinicalTrials.gov

Evidence Rating

A rating on a 5-star scale, portraying the curators trust in the experiments from which the evidence is curated. Refer to the additional documentation on trust ratings for guidance on how to score an evidence item.

5-stars - Strong, well supported evidence from a lab or journal with respected academic standing. Experiments are well controlled, and results are clean and reproducible across multiple replicates.

CIViC



Statement
The Evidence Statement is a brief summary of the clinical relevance of the Molecular Profile (Variant) in the context of a specific Disease, Evidence Type and Significance as described in the cited literature source.

Understanding Evidence Statements
The evidence statement field is a description of evidence from published medical literature detailing the association of or lack of association of a molecular profile (variant) with predictive, diagnostic, prognostic, predisposing, oncogenic or functional relevance to a specific disease (and treatment for predictive evidence). The format used for an evidence statement can vary, but it is recommended that this statement contain the following: a reiteration of the evidence type, molecular profile (variant), gene, and disease, any comparison made or therapeutics used (e.g., arms of clinical trial), the number of individuals (or cell lines) in the study, the conclusion from the study, and statistical comparisons that support the conclusion (e.g., p-values, R2, confidence intervals, etc.). Detailed examples of specific types of evidence statements can be found below. Of note, data constituting protected health information (PHI) should not be entered in the evidence statement field.

Curating Evidence Statements
Evidence Statements should be:

derived from primary literature sources (not review articles) whenever possible.

as concise as possible while providing sufficient experimental detail to interpret and evaluate the evidence (N values, statistics, etc.).

a single Predictive, Diagnostic, Prognostic, Predisposing, Oncogenic or Functional statement, not a combination.

aimed at a general audience, avoiding field-specific acronyms and colloquialisms.

Multiple, separate Evidence Items can be and often are derived from a single publication.

Generally, Evidence Statements involving drugs should be classified as being of the Predictive Evidence Type.

Evidence Level
Understanding Evidence Levels
The evidence level describes the robustness of the study type supporting the evidence item. Five different evidence levels are supported: “A - Validated association”, “B - Clinical evidence”, “C - Case study”, “D - Preclinical evidence”, and “E - Inferential association”. Evidence items with validated associations (A) have a proven or clinical consensus on the molecular profile (variant) relevance in cancer care. Typically these evidence items describe Phase III clinical trials or have associated FDA approved companion diagnostics. Clinical evidence (B) are typically large clinical trials or other primary patient data supporting the clinical association. These Evidence Items usually include more than 5 patients supporting the claim made in the evidence statement. Case studies (C) are individual case reports from clinical journals. Preclinical evidence (D) is derived from in vivo or in vitro experiments (e.g., cell lines or mouse models) that support clinical claims. Finally, inferential associations (E) indirectly associate the molecular profile (variant) to the provided clinical evidence.

Level

Name

Definition

Example and further comments

A

Validated association

Proven/consensus association in human medicine.

“AML with mutated NPM1” is a provisional entity in WHO classification of acute myeloid leukemia (AML). This mutation should be tested for in clinical trials and is recommended for testing in patients with cytogenetically normal AML. Validated associations are often in routine clinical practice already or are the subject of major clinical trial efforts.

B

Clinical evidence

Clinical trial or other primary patient data supports association.

BRAF V600E is correlated with poor prognosis in papillary thyroid cancer in a study of 187 patients with PTC and other thyroid diseases. The evidence should be supported by observations in multiple patients. Additional support from functional data is desirable but not required.

C

Case study

Individual case reports from clinical journals.

A single patient with FLT3 over-expression responded to the FLT3 inhibitor sunitinib. The study may have involved a large number of patients, but the statement was supported by only a single patient. In some cases, observations from just a handful of patients (e.g. 2-3) or a single family may also be considered a case study/report.

D

Preclinical evidence

In vivo or in vitro models support association.

Experiments showed that AG1296 is effective in triggering apoptosis in cells with the FLT3 internal tandem duplication. The study may have involved some patient data, but support for this statement was limited to in vivo or in vitro models (e.g. mouse studies, cell lines, molecular assays, etc.).

E

Inferential association

Indirect evidence.

CD33 and CD123 expression were significantly increased in patients with NPM1 mutation with FLT3-ITD, indicating these patients may respond to combined anti-CD33 and anti-CD123 therapy. The assertion is at least one step removed from a direct association between a molecular profile (variant) and clinical relevance.

Curating Levels
Each evidence statement is the result of an experiment, trial or study in published literature. It is important to capture the nature of these experiments in the evidence entry. Evidence levels allow for the subject of an evidence item to be presented in a simple, standardized fashion. The evidence level is also an indication of how close each assertion is to actual application in the clinic. Please, note that while evidence statements of all levels are acceptable in CIViC, the highest priority are levels A and B, followed by C, D, E. Our top priority is to document the evidence for application of molecular profile (variant) interpretations to real patients in the clinic today. The more time and development needed to determine the relevance of a molecular profile (variant) to real patients in the clinic, the lower the priority for curation. Reviewing and approving evidence items requires a serious time committment by the community. Please keep this in mind and try to direct your efforts to the most immediately clinically relevant evidence first.

A-Level Evidence Example

Below is an example of an A-level (validated) Evidence Item for the BRAF - V600E molecular profile (variant). In this example, the Evidence Item is describing the Phase 3 randomized clinical trial that was submitted to the FDA for therapeutic approval of Vemurafenib with Dacarbazine for treatment of untreated, metastatic melanoma.

Screenshot of an A-level (validated) evidence item summary
Figure 1: Screenshot of an A-level (validated) evidence item summary

A-level Curation Practices

Typically, A-level Validated Evidence Items describe Phase III Clinical Trials (for therapeutics or companion diagnostics), which are subsequently submitted to the FDA for pre-market approval.

In general, Evidence Items derived from any study cited in approvals, established practice guidelines, or considered the definitive practice-changing study, may be labeled Level A. In some cases Phase I trials can meet this requirement with sufficient justification (see EID1187).

Evidence Statements should include the gene/variant (molecular profile) being evaluated, the study population, disease state, study size, statistical significance (e.g., p-value, confidence interval), duration of the study, and other relevant information that is required to assess the evidence for interpretation.

Evidence Items derived from publications describing practice guidelines (e.g. WHO diagnostic criteria) are labeled A-Validated Evidence Level.

B-Level Evidence Example

Below is an example of a B-level (clinical) Evidence Item for the BRAF - V600E molecular profile (variant). In this example, the Evidence Item is describing a Phase 2 randomized clinical trial that was used to assess preliminary efficacy of the use of Vemurafenib for treatment of patients with previously treated skin melanoma.

Screenshot of an B-level (clinical) evidence item summary
Figure 2: Screenshot of an B-level (clinical) evidence item summary

B-Level Curation Practices

B-level Evidence Items can describe trials submitted to the FDA during the approval process; however, relative to A-level Evidence Items, B-level Evidence Items typically have a smaller sample size or assess less definitive outcomes (e.g., response rate instead of overall survival).

Phase I, II, and III clinical trials make up a significant percentage of Level B Evidence Items.

For curation of Phase I evidence, notes on treatment related adverse events may be added to the main evidence statement describing the variant-positive patient subgroup response to treatment, as dosing and adverse events are among the main focuses of Phase I studies.

B-level Evidence Items do not have to be derived from clinical trials but also can describe studies which attain a sufficient sample size to be considered more informative than a series of case studies, and ideally have some component of statistical conclusions in their results.

Greater than five patients are typically required for an Evidence Item to be considered a B-level Evidence Item.

Evidence Statements should include the gene/variant (molecular profile) being evaluated, the study population, disease state, study size, statistical significance (e.g., p-value, confidence interval), duration of the study, and other relevant information that is required to assess the evidence for interpretation.

Categorical variants (sometimes called bucket variants colloquially) often appear in B-level Evidence Items describing clinical trials, which pool together patient populations with mutations of a certain class (e.g. “PIK3CA mutation”), in order to attain a disease specific, statistically significant, clinical result across the patient population (e.g. Trastuzumab resistance in HER2 positive breast cancer).

C-Level Evidence Example

Below is an example of a C-level (case study) Evidence Item for the BRAF - V600E molecular profile (variant). In this example, the Evidence Item is describing a single patient with the BRAF - V600E molecular profile (variant) who demonstrated sensitivity/response to Pictilisib in the disease context of melanoma. This Evidence Item was classified as a Case Study because it described results for a single patient with advanced melanoma who had been enrolled in a larger Phase I clinical trial that evaluated 60 patients with advanced solid tumors and any BRAF variant for sensitivity to Pictilisib.

Screenshot of an C-level (case study) evidence item summary
Figure 3: Screenshot of an C-level (case study) evidence item summary

C-Level Curation Practices

C-level Evidence Items should describe a specific variant and likely will not apply to a categorical variant.

In some cases a clinical trial employing a categorical or bucket variant (e.g. EGFR mutation) will contain additional supplementary information on individual patient mutations and outcomes (e.g. CR, PR, SD or PD as best response). In such cases, along with the B-level Evidence Item based on the categorical variant, individual C-level case study Evidence Items can be curated for each listed variant.

Evidence Items involving fewer than five patients are typically considered to be C-level Evidence Items.

Evidence Statements should include the gene/variant (molecular profile) being evaluated, the study population, disease state, study size, statistical significance (e.g., p-value, confidence interval, if applicable), duration of the study, and other relevant information that is required to assess the evidence for interpretation.

D-Level Evidence Example

Below is an example of a D-level (Preclinical) Evidence Item for the BRAF - V600E molecular profile (variant). In this example, 49 BRAF-mutant melanoma cell lines exhibited resistance to a combination of dactolisib and selumetinib treatment. Note that older drug names were used in this study, BEZ238 and AZD6244, but since then, the drug names have been updated to dactolisib and selumetinib. To reduce confusion, the more current names are used in the drug field and the curator has included both the old and new names in the Evidence Statement.

Screenshot of an D-level (preclinical) evidence item summary
Figure 4: Screenshot of an D-level (preclinical) evidence item summary

D-Level Curation Practices

D-level Evidence Items typically describe animal models or cell line studies. The sample size for these studies can influence the Trust Rating, whereby increased numbers of mice or independent biological replicates used should increase the Trust Rating.

A concise description of the experiments performed should be prepared by the curator, supporting the Evidence Item Clinical Significance, and describing the controls that were used, and the significant findings that were observed.

Evidence Statements should include the gene/variant (molecular profile) being evaluated, the study population, disease state, study size, statistical significance (e.g., p-value, confidence interval), duration of the study, and other relevant information that is required to assess the evidence for interpretation.

When choosing a disease for Preclinical Evidence Items, it should reflect the context of the ultimate disease type that is being investigated and not necessarily the individual cell-line being evaluated. For example in EID1356, the preclinical work was performed on BA/F3 however the conclusions supported work across multiple cancer subtypes, therefore the selected disease field for this Evidence Item was “Cancer”.

E-Level Evidence Example

Below is an example of an E-level (inferential) Evidence Item for the BRAF - V600 Amplification molecular profile (variant). In this example, the Evidence Item is describing how BRAF - V600E Amplification could be a mechanism of selumetinib resistance in patients with colorectal cancer.

Screenshot of an E-level (inferential) evidence item summary
Figure 5: Screenshot of an E-level (inferential) evidence item summary

E-Level Curation Practices

E-level Evidence Items provide inferential support for the described molecular profile (variant). This could mean that the molecular profile (variant) was not ever actually measured, or that the results from the study do not directly evaluate the claims made by the Evidence Item.

E-level Evidence Items can be derived from in silico predictions, cell lines, animal models, or human studies.

Evidence Statements should include the gene/variant (molecular profile) being evaluated, the study population, disease state, study size, statistical significance (e.g., p-value, confidence interval), duration of the study, and other relevant information that is required to assess the evidence for interpretation. Often these data are not available for E-level Evidence Items.



Type
The Evidence Type refers to the type of clinical (or biological) association described by the Evidence Item’s clinical summary.

Understanding Evidence Types
Six Evidence Types are currently supported: Predictive (i.e. Therapeutic), Diagnostic, Prognostic, Predisposing, Oncogenic, and Functional. Each Evidence Type describes the clinical or biological effect a Molecular Profile (MP) has on the following: therapeutic response (Predictive), determining a patient’s diagnosis or disease subtype (Diagnostic), predicting disease progression or patient survival (Prognostic), disease susceptibility (Predisposing), or biological alterations relevant to a cancer phenotype (Oncogenic) or protein function (Functional). Selecting an Evidence Type has implications on available selections for Significance, which are detailed on the Evidence Significance page.

Type

Icon

Definition

Diagnostic

attribute-diagnostic

Evidence pertains to a variant’s impact on patient diagnosis (cancer subtype)

Predictive

attribute-predictive

Evidence pertains to a variant’s effect on therapeutic response

Prognostic

attribute-prognostic

Evidence pertains to a variant’s impact on disease progression, severity, or patient survival.

Predisposing

attribute-predisposing

Evidence pertains to a germline Molecular Profile’s role in conferring susceptibility to disease (including pathogenicity evaluations)

Oncogenic

attribute-oncogenic

Evidence pertains to a somatic variant’s involvement in tumor pathogenesis as described by the Hallmarks of Cancer.

Functional

attribute-functional

Evidence pertains to a variant that alters biological function from the reference state.

Extensive documentation for curating Evidence types is provided on the Curating Evidence page. Be sure to closly study the examples for each type.



Direction
Evidence Direction indicates if the Evidence Statement supports or refutes the significance of an event.

Understanding Evidence Direction
The available options include: “Supports” or “Does Not Support”. Nuanced examples for how to correctly use the Evidence Direction for Predictive Evidence Types are shown in the section on curating Evidence Items.

Curating Evidence Direction
Evidence Direction interpretation differs slightly depending on the Evidence Type.

Direction for Predictive Evidence

Direction

Icon

Definition

Supports

attribute-supports

Experiment or study supports the variant’s response to a drug

Does not support

attribute-doesnotsupport

Experiment or study does not support, or was inconclusive of an interaction between the variant and a drug

Direction for Diagnostic Evidence

Direction

Icon

Definition

Supports

attribute-supports

Experiment or study supports the variant’s impact on the diagnosis of disease or subtype

Does not support

attribute-doesnotsupport

Experiment or study does not support the variant’s impact on diagnosis of disease or subtype

Direction for Prognostic Evidence

Direction

Icon

Definition

Supports

attribute-supports

Experiment or study supports the variant’s impact on prognostic outcome

Does not support

attribute-doesnotsupport

Experiment or study does not support a prognostic association between variant and outcome

Direction for Predisposing Evidence (where Significance is Predisposition)

Direction

Icon

Definition

Supports

attribute-supports

Suggests a pathogenic or a protective role for a germline variant in cancer

Does not support

attribute-doesnotsupport

Supports a benign (for Predisposition) or lack of protective (for Protectiveness) role for a germline variant in cancer.

Direction for Functional Evidence

Direction

Icon

Definition

Supports

attribute-supports

Experiment or study supports the variant causing alteration or non-alteration of the gene product function

Does not support

attribute-doesnotsupport

Experiment or study does not support the variant causing alteration or non-alteration of the gene product function

Direction for Oncogenic Evidence (where Significance is Oncogenicity)

Direction

Icon

Definition

Supports

attribute-supports

Supports an oncogenic or protective role for a somatic variant.

Does not support

attribute-doesnotsupport

Supports a benign (for Oncogenicity) or lack of protective (for Protectiveness) role for a somatic variant in cancer.

Not Applicable

attribute-na

Not applicable for Oncogenic Evidence Type

Significance
Significance describes how the variant is related to a specific, clinically-relevant property as described in the Evidence Statement. Significance terms vary depending on the Evidence Type (e.g. “Resistance” for Predictive Evidence, “Better Outcome” for Prognostic Evidence, etc.).

Understanding Significance
The available options for Significance depend on the Evidence Type selected for the Evidence statement. If a Predictive Evidence Type is selected, Significance can include: Sensitivity/Response, Resistance, Adverse Response, Reduced Sensitivity, or N/A. Each of these refers to the association between the Molecular Profile and clinical or preclinical response of the therapeutic(s). If a Diagnostic Evidence Type is selected, the Significance can be either Positive or Negative. A Positive Diagnostic Evidence Item implies that the Molecular Profile is associated with diagnosis of disease or disease subtype whereas a Negative Diagnostic Evidence Item implies lack of association. If a Prognostic Evidence Type is selected, the Significance options include: Better Outcome, Poor Outcome, or N/A. The N/A option can be used to imply that the variant does not have an impact on patient prognosis. A Functional Evidence Type should be associated with one of the following Significance values: Gain of Function, Loss of Function, Unaltered Function, Neomorphic, Dominant Negative, or Unknown. These options allow curators to indicate how the variant impacts the biological function described in the Evidence Statement. Predisposing and Oncogenic Evidence use the Significance values Predisposition/Oncogenicity and Protectiveness. However, final classification of the Significance for these Evidence Types should be established at the assertion level using the appropriate guidelines.

Significance for Predictive Evidence

Significance

Icon

Definition

Sensitivity/Response

attribute-sensitivityresponse

Associated with a clinical or preclinical response to treatment

Reduced Sensitivity

attribute-reducedsensitivity

Response to treatment is lower than seen in other treatment contexts

Resistance

attribute-resistance

Associated with clinical or preclinical resistance to treatment

Adverse Response

attribute-adverseresponse

Associated with an adverse response to drug treatment

N/A

attribute-na

Variant does not inform clinical interpretation

Significance for Diagnostic Evidence

Significance

Icon

Definition

Positive

attribute-positive

Associated with diagnosis of disease or subtype

Negative

attribute-negative

Associated with lack of disease or subtype

Significance for Prognostic Evidence

Significance

Icon

Definition

Better Outcome

attribute-betteroutcome

Demonstrates better than expected clinical outcome

Poor Outcome

attribute-pooroutcome

Demonstrates worse than expected clinical outcome

N/A

attribute-na

Variant does not inform clinical action

Significance for Predisposing Evidence

Significance

Icon

Definition

Predisposition

attribute-predisposition

Germline variant has predisposing potential for cancer, and may meet select ACMG/AMP criteria supporting pathogenic or benign classification.

Protectiveness

attribute-protectiveness

Germline variant has properties that protect individuals from acquiring cancer.

Significance for Oncogenic Evidence

Significance

Icon

Definition

Oncogenicity

attribute-oncogenicity

Somatic variant has oncogenic potential for driving cancer, and may meet select ClinGen/CGC/VICC criteria supporting pathogenic or benign classification.

Protectiveness

attribute-protectiveness

Somatic variant has a protective role against cancer.

Significance for Functional Evidence

Significance

Icon

Definition

Gain of Function

attribute-gainoffunction

Sequence variant confers an increase in normal gene function

Loss of Function

attribute-lossoffunction

Sequence variant confers a diminished or abolished function

Unaltered Function

attribute-unalteredfunction

Gene product of sequence variant is unchanged

Neomorphic

attribute-neomorphic

Sequence variant creates a novel function

Dominant Negative

attribute-dominantnegative

Sequence variant abrogates function of wildtype allele gene product

Unknown

attribute-unknown

Sequence variant that cannot be precisely defined by the other listed categories

Origin
Presumed source of the variant in the context of this study.

Understanding Variant Origin
The origin of a variant in a study is important for interpreting the results in context. Studies may provide specific information about the origin of the variant (somatic with tumor/normal paired data) while others may be more ambiguous (tumor-only sequencing with a variant that may be somatic or germline, e.g., BRCA1 mutation from a breast cancer sample). Documenting Variant Origin allows for quick filtering of evidence and provides context for the study compared to other studies that involve that variant.

Curating Variant Origin
The Variant Origin in and Evidence Item identifies whether the variant was presumed as an inherited (germline mutation) or acquired (somatic mutation) event in the context of the study. We generally consider somatic events to be the priority, as this is an area that has not been as well addressed by existing resources. However, germline mutations with established clinical relevance are acceptable. Germline polymorphisms (>1% allele frequency in the population) are considered low priority, again unless there is an established clinical relevance. We encourage the use of large population resources such as gnomAD for population frequency estimations rather than relying on the frequency reported by the original study. Polymorphisms described in association studies should be curated with great caution and may face additional scrutiny from CIViC moderators. For some variant types, the variant origin field may be unknown or N/A. For example, EXPRESSION variants are neither germline nor somatic and should be marked as N/A. Fusion variants are an unusual case in that they are often observed in the transcriptome but are usually accompanied by an underlying somatic (or germline) mutation. Most fusions should be entered as somatic. If in doubt, please note the issue at the time of your submission to encourage discussion during the moderation stage.

Expression variants should be marked as ‘N/A’.

Fusions are often observed in the transcriptome but are usually accompanied by an underlying somatic (or germline) mutation.

Population frequencies should be based on current population databases (e.g., gnomAD) rather than the original report.

Origin

Icon

Description

Somatic

attribute-somatic

Variant is a mutation, found only in tumor cells, having arisen in a specific tissue (non-germ cell), and is not expected to be inherited or passed to offspring.

Rare Germline

attribute-raregermline

Variant is found in every cell (not restricted to tumor/diseased cells) and is thought to exist in less than 1% of the population relevant to this evidence item.

Common Germline

attribute-commongermline

Variant is found in every cell (not restricted to tumor/diseased cells) and is thought to exist in at least 1% of the population relevant to this evidence item.

Combined

attribute-combined

Variants in the corresponding Complex Molecular Profile have heterogeneous origins.

Mixed

attribute-mixed

The population of patient variants described in the Evidence is a mixture of Somatic and Germline.

Unknown

attribute-unknown

The variant origin is uncertain based on the available evidence.

N/A

attribute-na

The variant type (e.g., expression) is not compatible (or easily classified) with the CIViC concept of variant origin.

Examples

Somatic

DNAJB1-PRKACA (EID532), BRAF V600E (EID1409), KRAS Exon 2 Mutation (EID993), EGFR Amplification (EID473)

Rare Germline

BRCA2 Mutation (EID1371)

Common Germline

GSTP1 I105V (EID670), UGT1A1*28 (EID1792)

Unknown

FANCC Loss-of-function (EID1307)

N/A

CD274 Expression (EID1167)

Disease
The disease field generally requires an value that is known to the Disease Ontology database. (Kibbe et al. 2015) The Disease Ontology (DO) database provides an open-sourced ontology for the integration of biomedical data that is associated with human disease. Within the CIViC database, the disease should be the cancer or cancer subtype that is associated to the described Molecular Profile (variant or ensemble of variants) by the evidence being curated. The disease selected should be as specific as possible and should reflect the disease type described in the source that supports the evidence statement. In CIViC, Disease is largely synonymous with cancer type or sub-type.

Curating Diseases
The disease field will autofill based on existing diseases in the Disease Ontology (DO) database and the most specific disease subtype should be selected, if possible. Only a single disease can be associated with an evidence item. If the Molecular Profile and clinical evidence is implicated in multiple diseases in the source that is being curated, then multiple evidence items should be created. If the disease cannot be identified in the Disease Ontology database, the curator can add this new disease to CIViC during the curation of the associated Evidence Item (Figure 1). Alternatively, new DO terms, definitions, suggestions and questions in regard the Disease Ontology can be submitted to the DO Term Tracker.

Adding a new disease to CIViC
Figure 1: A new disease term can be added to CIViC during the Evidence Item curation process

The current Diseases (cancer types) with associated with Evidence, Assertions and other information in CIViC can be explored on the CIViC Disease Page.

Therapy
Therapies in CIViC are associated with Evidence Items or Assertions of the Predictive Type, which describe sensitivity, resistance or adverse response to drugs or other treatments when a given Molecular Profile is present in a patient or a preclinical model system. The Therapy field may also be used to describe more general treatment types and regimes, such as FOLFOX or Radiation, as long as the literature derived Evidence Item makes a scientific association between the Drug (treatment type) and the presence of the Molecular Profile (Molecular Profiles are comprised of a variant or collection of variants).

Curating Therapies
If the Evidence Item’s Evidence Type is Predictive, a new button entitled “Add a Therapy” will become available (Figure 1). It is required to add a Therapy if the Predictive Evidence Type is chosen. After clicking “Add a Therapy”, a field to type the Therapy name will appear. The curator can type the name of a therapy such as erlotinib, and a menu will appear with Therapies drawn from NCIT that contain the name. The specified Therapy will possess an NCI Thesaurus ID whenever available. Although often searchable, trade names for treatments should not be used.

Overview of adding a therapy to predictive EID
Figure 1: Adding a Therapy to a Predictive Evidence Item

After the Therapy is chosen from the menu, it will appear in the Add Evidence Form as shown in Figure 2. A popover menu can be accessed from the Therapy, and it contains information on how many Evidence Items and Assertions use the Therapy, as well as a link to the NCIT page for the Therapy.

Showing link to NCIT page for Therapies with an NCIT ID
Figure 2: Link to NCIT page for Therapies with an NCIT ID

Multiple Therapies can be added to a single Evidence Item, however, if two or more Therapies are added to an Evidence Item the curator is required to provide a Therapy Interaction Type. Therapy Interaction Types can be either combination, sequential, or substitutes. The Therapies and Therapy Interaction Types should be explicitly stated in the source supporting the Evidence Item.

Overview of dding more than one therapy and specifying Therapy Interaction Type
Figure 3: Adding more than one therapy and specifying Therapy Interaction Type

When a Therapy is not present in the NCIT, the Curator can add a new Therapy name to the Evidence Item (EID) field during EID curation, and it will then be added to the CIViC database (Figure 4). If the Therapy is not found, it may be helpful to search the NCIT directly (https://ncithesaurus.nci.nih.gov/) using relationships and mappings before creating a novel treatment in CIViC. The NCIT supports drug classes (e.g., EGFR Tyrosine Kinase Inhibitor, C2167), but the most precise therapy or combination should be used whenever possible (e.g., Afatinib, Erlotinib - Substitutes).

Overview of adding a Therapy not present in NCIT
Figure 4: Adding Therapy not present in NCIT

Therapies added to CIViC which are not in NCIT should be submitted to NCIT using this form to submit new terms to the NCI Thesaurus.


Associated Phenotype
Associated Phenotypes can be added to any evidence item. Phenotypes standardize symptoms or abnormalities that are encountered in human disease (e.g., pheochromocytoma) and each phenotype is taken from the Human Phenotype Ontology database. This field is optional and evidence items can be submitted without associated phenotypes. Associated Phenotypes should provide additional information beyond what is implied by the Disease field. Phenotypes should be particularly considered for Predisposing Evidence Items whereby the variant is associated with a non-binary phenotype or syndrome for a particular genotype.

Curating Associated Phenotypes
The Associated Phenotypes field should be curated when the literature or abstract source specifically mentions the given phenotype being observed in a patient with the Molecular Profile (variant) of interest. If the phenotype was seen in a group of patients with related Molecular Profiles, then the Associated Phenotypes field should be left blank. If the curator has knowledge that the given phenotype is often associated with the Molecular Profile, but this association is not specifically noted in an observed patient being reported in the specific literature source used for creation of the EID, then the Associated Phenotype field should be left blank.

The current Associated Phenotypes linked to Evidence Items and Assertions in CIViC can be explored on the CIViC Phenotypes Page.

Source
An evidence item summarizes data from one specific source publication.

Understanding Source
Each Evidence Item must be associated with a Source Type and Source ID, which link the Evidence Item to the original publication supporting evidence claims. Currently, CIViC accepts publications indexed in PubMed or abstracts published through the American Society of Clinical Oncology (ASCO) or the American Society of Hematology (ASH). If a PubMed Source Type is selected, the curator can then enter the PubMed ID, which can be verified by comparing the desired source to the abbreviated citation that is automatically generated below the PubMed ID field. Additionally, ClinicalTrials Registry Number(s) are automatically linked via the PubMed database, when available. If an ASCO Source Type is selected, the ASCO Web ID should be entered into the source ID field. If an ASH Source Type is selected, the ASH DOI should be entered into the source ID field.

Curating Source
All curated CIViC Evidence, Assertions, Molecular Profile Descriptions, and Gene Descriptions are based on cited sources from the biomedical literature, currently limited to those publications indexed in PubMed, the ASCO Meeting Library, or ASH Meeting Abstracts in the Journal Blood. As soon as any publication is cited in CIViC it appears as a separate Source Record and can be browsed or searched within the CIViC knowledgebase. Each Source Record includes details about the publication as well as a table linking to all CIViC evidence curated for that source.

Comments can be added to any Source Record at any time (see Figure 1 below). Source comments are a useful place to document general or specific notes to aid current and future curation. For example, if a source has an overlapping patient population with another study already curated within CIViC, this can be documented. In other cases, the reference sequence used for determining the CIViC Variant’s coordinates might be recorded.

The current Sources associated with Evidence, Assertions and other information in CIViC can be explored on the CIViC Sources Page.

Screenshot of source summary
Figure 1: Screenshot of source summary


Clinical Trial
Clinical Trial ID is associated with an Evidence Item in an automated fashion. If a CIViC Evidence item shows a Clinical Trial ID, then that Clinical Trial ID is found on the PubMed page for that Evidence Source. Following the link in CIViC for the Trial ID brings the user to the corresponding clinicaltrials.gov page for the trial. This field is not accessible to direct curation.

The current Clinical Trials associated with Evidence and Sources in CIViC can be explored on the CIViC Clinical Trials Page.


Evidence Rating
The Evidence Rating is scored on a scale from 1-5 stars reflecting the curator’s confidence in the quality of the summarized evidence.

Understanding Evidence Ratings
The Evidence Rating depends on a number of factors, including study size, study design, orthogonal validation, and reproducibility. Although the overall publication/study/abstract might be high quality, the Evidence Rating may be low for an Evidence Item referring to a single conclusion in the study that is not well supported. The Evidence rating therefore does not rate the journal, publication, or Evidence Source itself, but instead evaluates in isolation the components of evidence extracted from the Evidence Source. While this remains a somewhat subjective measure, general best-practices for the Evidence Rating are detailed below.

Curating Evidence Ratings
In order to quickly discern how well the evidence derived from the article (PubMed indexed) or abstract (ASCO/ASH) evidence source supports a given evidence statement, a five star evidence rating system is used. Each evidence item is given a rating, from 1 to 5 stars, based on the quality of the evidence the statement summarizes. This rating depends on a number of factors, including study size, quality control, orthogonal validation, and reproducibility. It should be noted that this rating is largely subjective and may be debated (hopefully within the CIViC interface). Also the rating should be specific to the evidence statement. The overall publication/study might be high quality, but the evidence statement may refer to a single conclusion in the study, and that part of the study might not be well supported. For example, the assertion may relate to patients with a particular mutation, and the study might involve an impressive 500 patients, but if only 2 patients have the mutation in question, the quality rating may be low for this evidence statement.

Evidence Rating

Definition

    

Strong, well supported evidence from a lab or journal with respected academic standing. Experiments are well controlled, and results are clean and reproducible across multiple replicates. Evidence confirmed using independent methods. The study is statistically well powered.

    

Strong, well supported evidence. Experiments are well controlled, and results are convincing. Any discrepancies from expected results are well-explained and not concerning.

    

Evidence is convincing, but not supported by a breadth of experiments. May be smaller scale projects, or novel results without many follow-up experiments. Discrepancies from expected results are explained and not concerning.

    

Evidence is not well supported by experimental data, and little follow-up data is available. Publication is from a journal with low academic impact. Experiments may lack proper controls, have small sample size, or are not statistically convincing.

    

Claim is not supported well by experimental evidence. Results are not reproducible, or have very small sample size. No follow-up is done to validate novel claims.

Curating Five-Star Evidence
The example Evidence Item below describes a Phase III clinical trial (PROFILE 1014) that evaluated the impact of the ALK - Fusions (single variant molecular profile) on therapeutic response with crizotinib for patients with lung non-small cell carcinoma. The clinical trial was a randomized, double-blinded, placebo-control study of 343 patients that evaluated progression free survival, objective response rate, and quality of life. The results were published in the New England Journal of Medicine.

Screenshot of EID1199 summary, a five-star Evidence Item
Figure 1: Screenshot of EID1199 summary, a five-star Evidence Item

Evidence Items with a 5-star rating should be strong, well-supported evidence from a lab or journal with respected academic standing. Experiments should be well controlled, and results should be clean and reproducible across multiple replicates. Evidence should be confirmed using independent methods and the study should be statistically powered.

In general, Evidence Rating is a rating of the unit of evidence extracted from a data source (publication index in PubMed or ASCO/ASH abstract) and is not a rating of the publication or abstract itself. Thus, an isolated supplementary figure in a high quality and well-researched publication may yield a relevant piece of clinical information on a Molecular Profile (simple or complex variant) of interest, and an Evidence Item (EID) could be prepared from this figure. Due to the limited nature of the data supporting this type of Evidence Item, it would receive a lower Evidence Rating. This is because this rating would applies only to the evidence used to create this single EID, not to the publication as a whole.

Curating Four-Star Evidence
The example Evidence Item below describes a Phase 2A clinical trial with multiple arms that included evaluation of the therapeutic effect of pertuzumab and trastuzumab on 37 patients with HER2 - Amplified colorectal cancer. The study was sufficiently powered to demonstrate an increase in patient response and remission provided their advanced, refractory state and relatively rare molecular alteration for that tumor type. The study was part of a clinical trial that was registered through the NIH and was published in the Journal of Clinical Oncology.

Screenshot of EID5981's summary, a four-star Evidence Item
Figure 2: Screenshot of EID5981's summary, a four-star Evidence Item

Evidence items with a 4-star rating should be strong, have well-supported evidence, well-controlled experiments, and convincing results. Any discrepancies from expected results are well-explained and not concerning.

This example was similar in design as the 5-star example, however, the reduced sample size contributed to the reduction in the star rating.

Curating Three-Star Evidence
The example Evidence Item below describes the same Phase 2A clinical trial as shown above as a four-star Evidence Item, but differs in the advanced solid tumor type being evaluated. In the subset of patients with bladder cancer, three of nine patients showed response to combination therapy with trastuzumab and pertuzumab, which supports sensitivity/response. Although this Evidence Item is derived from the same clinical trial, the reduction in Evidence Rating is representative of the smaller number of patients and large 95% confidence interval.

Screenshot of EID5982's summary, a three-star Evidence Item
Figure 3: Screenshot of EID5982's summary, a three-star Evidence Item

Evidence Items with a 3-star rating are convincing but not supported by a breadth of experiments. These Evidence Items may be smaller scale studies, or novel results without many follow-up experiments.

Even though these Evidence Items might contain reduced amount of data, discrepancies from expected results should still be explained and not concerning.

Curating Two-Star Evidence
The example Evidence Item below describes a Phase II clinical trial that evaluated 29 patients with breast cancer who were being treated with either afatinib, lapatinib, or trastuzumab. In this study, 18 patients showed response to one of the therapeutics. The Evidence Rating for this evidence item was only 2 stars due to lack of evidence supporting the clinical claim (supports sensitivity/response). Specifically, the sample size was low for each of the three arms, there was no reported statistical significance. Additionally, the clinical endpoint for the study was objective response rate, which is not as strong of an endpoint as other metrics such as overall survival.

Screenshot of EID887's summary, a two-star Evidence Item
Figure 4: Screenshot of EID887's summary, a two-star Evidence Item

Evidence items with a 2-star rating are not well supported by experimental data, and little follow-up data is available.

Typically, Evidence Items received a 2-star rating if the experiments lack proper controls, have small sample size, or are not statistically convincing.

Curating One-Star Evidence
The example Evidence Item below describes a B-level clinical study that evaluated 6 patients with ERBB2 - Amplification for response to capecitabine, oxaliplatin, and chemoradiotherapy, with or without cetuximab. There was no difference in outcome between the 6 patients with amplification when compared to the 135 patients with no visible ERBB2 - Amplification on FISH / IHC. The study described in this Evidence Item includes a heterogenous combination of variant detection methods, a low number of patients in the experimental arm (n=6) and overall low statistical power. Therefore, despite being a B-level Evidence Item, the curator assigned the EID a 1-star Evidence Rating.

Screenshot of EID895's summary, a one-star Evidence Item
Figure 5: Screenshot of EID895's summary, a one-star Evidence Item

Evidence items with a 1-star rating contain claims that are not well-supported by experimental evidence. Typically, the results are not reproducible and/or have very small sample size. No follow-up is done to validate novel claims.

Typically, Evidence Items received a 1-star rating if the experiments lack proper controls, have small sample size, or are not statistically convincing.


Assertions Overview
An assertion classifies the clinical significance of a variant-disease association under recognized guidelines (see AMP Classification, NCCN Guidelines, for more).

Figure showing an overview of the attributes and associations of a CIViC Assertion
Figure 1: Assertion Attributes and Associations

The CIViC Assertion (AID) summarizes a collection of Evidence Items (EIDs) that covers predictive/therapeutic, diagnostic, prognostic, predisposing or oncogenic information for a molecular profile (variant) in a specific cancer context (Figure 1). Functional Assertions are not currently supported. In general, an Assertion of a certain Type (e.g. Diagnostic) will be supported by a collection of Evidence Items (EIDs) of the same type, but Functional EIDs may be used to support Assertions of other types. The collection of EIDs associated with an Assertion should cover the important clinically relevant findings for the variant in the context of the specific cancer (and drug entity for Predictive Assertions). Assertion summaries mention NCCN or other practice guidelines related to the variant, as well as FDA drug approvals. In place of the curator assigned star rating found in CIViC Evidence Items, CIViC Assertions utilize widely adopted, published guidelines for variant tiering and pathogenicity/oncogenicity assessment, which are detailed below. CIViC Assertions are the primary entity that make up CIViC submissions to ClinVar.

CIViC currently has two main types of Assertions: those based on variants of primarily somatic origin (predictive/therapeutic, prognostic, diagnostic, and oncogenic) and those based on variants of primarily germline origin (predisposing). When the number and quality of Predictive, Prognostic, Diagnostic, Predisposing or Oncogenic Evidence Items (EIDs) in CIViC sufficiently cover what is known for a particular Molecular Profile and cancer type, then a corresponding assertion may be created in CIViC.

Fields Shared with Evidence
Assertions share several fields with evidence, which for the most part can be understood and curated in the same manner. Please review the evidence documentation for these fields, and the notes below on any nuances in interpretation or curation between entity’s fields.

Shared Field

Evidence Documentation

Notes

Gene

Gene Field

Molecular Profile

Molecular Profile Field

Origin

Origin Field

Disease

Disease Field

In some cases, several evidence items with non-identical but highly related disease terms may be incorporated into a single assertion. In this case, choose the most general disease category that includes all of the evidence diseases.

Type

Type Field

Direction

Direction Field

Significance

Significance Field



Associated Phenotypes
Associated Phenotypes for an Assertion are phenotypes that have been observed and recorded in patients documented to have the specific variant for which the Assertion has been created. The Associated Phenotypes field is hand curated and terms are drawn from the Human Phenotype Ontology (HPO).

Curating Associated Phenotypes
Associated Phenotypes for an Assertion are a collection of the Associated Phenotypes taken from the Assertion’s supporting Evidence Items.

Any phenotypes added to an Assertion’s Associated Phenotypes field must occur in at least one of the supporting Evidence Items (EIDs). Note that when an HPO term is added to an EID, it has been reported in the specific evidence source for that EID in a patient with the specific CIViC Variant for that EID.

Supporting EIDs for a given Assertion may be drawn from categories of different generality (i.e. an EID for “Cancer” may support an Assertion for melanoma). Therefore, curators should be careful to only draw HPO terms to use in the Assertion from EIDs that strictly match the Assertion Disease and Variant in a highly specific manner.

Note that the HPO Terms chosen for Associated Phenotypes for an Assertion do not give quantitative data. For instance a given HPO term may be found in multiple supporting EIDs for an Assertion, while a second HPO term may occur only once in the collection of supporting EIDs. In the Assertion, both terms will occur only once. Therefore the information on frequency of phenotype observation is not carried over into the Assertion. While the collection of evidence supporting an Assertion should do a good job of covering the field for that given variant, CIViC Clinical Significance, and disease, the system of publishing on variants and noting Associated Phenotypes may not yet be reliable enough to use literature curation as a measure for phenotype frequency, especially when the numbers are small. For variants with larger bodies of curated literature in CIViC, advanced search functions can give statistics on phenotype frequency occurring in literature for a given variant.


NCCN Guideline
The National Comprehensive Cancer Network (NCCN) is a nonprofit collaboration of multiple cancer centers which contributes to research and education. NCCN maintains an influential set of detailed guidelines for the treatment of specific cancer types, which is regularly updated. CIViC cites these and other guidelines during the curation process.

Understanding NCCN Guidelines
NCCN and other guidelines are relevant to Assertions on multiple levels. If a given molecular profile (variant or combination of variants) and cancer type, for which the assertion is being prepared, appears in guidelines which are relevant to the field, and pertain to the Assertion Type which is being curated, then those guidelines should be cited in the Assertion NCCN Guideline input fields (cancer type and version).

Curating NCCN Guidelines
For many Assertions in CIViC, NCCN Guidelines may cover key clinical recommendations associated to the variant or Molecular Profile. When this is the case, the curator can cite the specific guideline that contains these recommndations, so that end users can explore these guidelines on their own if interested. The version should be provided in the format number.YYYY (version number followed by dot and year).

NCCN guidelines are copyrighted content and should not be quoted or repurposed into Assertion description.

Screenshot of AID10, an assertion with an NCCN guideline assigned
Figure 1: Assertion for a Molecular Profile which cites NCCN guidelines version.

FDA Companion Test
A companion diagnostic device can be in vitro diagnostic device or an imaging tool that provides information that is essential for the safe and effective use of a corresponding therapeutic product.

Understanding FDA Companion Tests
A positive identification of a variant using an IVD companion diagnostic device indicates the use of a specific therapeutic product. The use of the IVD companion diagnostic is stipulated in the instructions for use in the labeling of both the diagnostic device and the corresponding therapeutic product, as well as in the labeling of any generic equivalents and biosimilar equivalents of the therapeutic product. A list of Cleared or Approved Companion Diagnostic Devices (In Vitro and Imaging Tools) can be found on the FDA website.

This list is distinct from the list of Nucleic Acid Based Tests, which provides a list of tests that analyze variations in the sequence, structure, or expression of deoxyribonucleic acid (DNA) and ribonucleic acid (RNA) in order to diagnose disease or medical conditions, infection with an identifiable pathogen, or determine genetic carrier status. Diagnostics listed on this list can be used for diagnosis of disease and potentially prognosis but are not associated with a specific targeted therapeutic for intervention.

Curating FDA Companion Tests
The Molecular Profile (variant) list(s) or definitions provided by the FDA should be used when determing if FDA Companion Tests are associated with Assertions. The checkbox for this label should only be selected if both the disease and the variant listed in the Assertion directly correlates with those listed by the FDA. The FDA Companion Test designation in CIViC is only relevant to Assertions where the Assertion Type is Predictive (therapeutic).



Summary and Description
Assertion Summary

The Assertion Summary restates the Clinical Significance as a brief single sentence statement. It is intended for potential use in clinical reports. The Assertion Summary is designed for rapid communication of the Clinical Significance, especially when displayed in a longer list with other variants.

Assertion Description

The Assertion Description gives detail including practice guidelines and approved tests for the variant.

Molecular Profiles Overview
CIViC Molecular Profiles are combinations of one or more CIViC variants. Most Molecular Profiles are “Simple” Molecular Profiles comprised of a single variant. In most cases, these can be considered equivalent to the CIViC concept of a Variant. However, increasingly clinical significance must be considered in the context of multiple variants simultaneously. Complex Molecular Profiles in CIViC allow for curation of such variant combinations. Regardless of the nature of the Molecular Profile (Simple or Complex), it must have a Predictive, Prognostic, Predisposing, Diagnostic, Oncogenic, or Functional clinical relevance to be entered in CIViC.

The co-occurrence and mutual exclusivity of mutations in cancer are gaining clinical relevance. Double Hit Lymphoma (DHL) is characterized by combinations of mutations in MYC, BCL2, or BCL6. Trastuzumab resistance in HER2 overexpressing breast cancer may be induced by mutations in PIK3CA. Resistance to Imatinib may be conferred by mutations to BCR-ABL fusions (e.g. BCR::ABL + ABL F317L). Recent studies have indicated that checkpoint inhibitor therapy targeting PDL1 may be more effective in the absence of strong drivers like ALK Fusion or EGFR Mutation.

Past versions of the CIViC data model had Gene as a top level entity, associated to one or more Variants, with literature curated Evidence Items (EIDs) supporting each variant (Figure 1). Evidence Items could only be curated for variants associated with a single gene, so curation of evidence for an entity like DHL would not be possible. Molecular Profiles (MPs) were introduced to address this shortcoming of the data model.

Figure depicting the transition for a Variant model to a Molecular Profile model
Figure 1: Original and updated model based on Molecular Profiles

Figure 2 shows the attributes of a Molecular Profile, its associations with other CIViC entities, and how its Score is computed.

Figure depicting the CIViC Molecular Profile with its attributes and associations
Figure 2: Molecular Profile Attributes and Associations

Consider the following case study:

A 42 year old man with non-smoking history presented with EGFR L858R positive lung adenocarcinoma. He was given various treatments including erlotinib and gefitinib and progressed four years later. Biopsy revealed EGFR T790M mutation, and osimertinib treatment was given. Partial response was seen, and progression occurred after 13 months. BRAF V600E mutation was found in progressed tumor cells, but was not reported before osimertinib resistance.

This case describes a lung cancer patient with EGFR L858R, EGFR T790M, and BRAF V600E mutations gaining resistance to osimertinib. We define the following Molecular Profile (MP) to describe the relevant patient genotype of driver and resistance variants described in the case study:

EGFR L858R AND EGFR T790M AND BRAF V600E

Earlier versions of CIViC did not allow for evidence to be associated with collections of variants across different genes such as the MP above. To address this need, the CIViC data model has been updated to include MPs which allow the association of clinical evidence to complex combinations of multiple variants across different genes. The MP consists of a combination of one or more variants. Variants are placed in combinations connected by “AND”, “OR”, “AND NOT”, or “OR NOT”. These relationships may be further defined by parenthesis, as in DHL which has variants in MYC and either BCL2 or BCL6:

MYC Rearrangement AND (BCL2 Rearrangement OR BCL6 Rearrangement)

The specific absence of a variant in the MP is supported by AND NOT. An example of this is a Molecular Profile which may be indicated for checkpoint inhibitor therapy:

PDL1 Expression AND NOT (EGFR Mutation OR ALK Fusion)

Which is equivalent to:

PDL1 Expression AND NOT EGFR Mutation AND NOT ALK Fusion

Currently no specific form among equivalent MPs is enforced. Alternate forms for an MP should appear as aliases on the MP page. Curators should strive for the shortest and most intuitive representation of the MP. Evidence Items (EIDs) in the new model are associated with MPs instead of directly with variants. There are two types of MP, the simple MP which contains only one variant, and the complex MP which contains two or more variants (Figure 3). The variants in a complex MP can be associated with one or more genes.

Figure contrasting simple and complex molecular profiles in CIViC
Figure 3: Simple and Complex Molecular Profiles

A complex MP which has two or more variants can also be thought of as containing smaller MPs within it. Therefore, in the example Molecular Profile “NPM1 Exon 12 Mutation AND NOT FLT-3 ITD” (Figure 4), we see that Evidence Items can be associated with the complex MP as well as to the simple MPs of which the complex MP is comprised of:

Figure depicting how evidence may be associated with complex MPs as well as their component simple MPs
Figure 4: Evidence Items associated to complex Molecular Profiles as well as their component Molecular Profiles

Molecular Profiles associated with a gene are visible on the gene page (Figure 5). The list contains the simple MPs which are associated only to the given gene, as well as complex MPs which can be composed of multiple variants, including variants associated with other genes as well as the given gene. Note that the Molecular Profile “NPM1 Exon 12 Mutation AND NOT FLT3 ITD” is displayed in the order with FLT3 ITD first in Figure 5.

Screenshot depicting the display of molecular profiles on a CIViC Gene page
Figure 5: Molecular Profiles are displayed on the Gene page

Molecular profile naming follows a structure where the gene is named first, followed by the specific variant name, and for complex MPs this pattern is followed as well, but linked with AND, OR, and NOT. Therefore the gene EGFR and the variant L858R will together comprise the Molecular Profile EGFR L858R.

Screenshot depicting an example evidence item using a molecular profile
Figure 6: Example Evidence Item using a complex Molecular Profile

Evidence Items based on complex Molecular Profiles are drawn from the same six evidence types and contain the same structured fields to be filled out by the curator as Evidence Items based on simple MPs, or Evidence Items based on single gene variants from older versions of CIViC. The case study mentioned above has been curated into an evidence item and is seen in the example EID in Figure 6.

Molecular Profile Attributes

Attribute

Description

Source

Name

Name of the Molecular Profile. This is assembled automatically from the component gene/variant parts.

CIViC

Description

User-defined description of the clinical relevance of this molecular profile.

CIViC

Alias

Alternative names for this Molecular Profile

CIViC

Sources

A list of PubMed IDs referring to evidence supporting statements made in the Molecular Profile description. Source descriptions (e.g. ‘Weisberg et al., 2007, Nat. Rev. Cancer’) are pulled from the PubMed database at the time of submission, and are not editable.

CIViC (PubMed)

Molecular Profile Score

The Molecular Profile Score assesses the quality and quantity of evidence submitted for each molecular profile. The Molecular Profile Score is calculated by adding all Evidence Item Scores for each variant. The Evidence Item Score is calculated by multiplying the evidence level (A=10 points, B=5 points, C=3 points, D=1 point, E=0.25 points) by the evidence rating (Each Star = 1 point).

CIViC



Molecular Profile Score
The Molecular Profile Score was developed to calculate the relative abundance of total available curated evidence for each Molecular Profile. The Molecular Profile Score reflects: 1) the strength of the evidence that was curated and 2) the total amount of curation that has been completed for each Molecular Profile.

This field is automatically generated, not curated.

Understanding Molecular Profile Scores

The Molecular Profile Score sums the Evidence Scores (see Figure 1 for an example) for all Evidence Items associated with the Molecular Profile. The Evidence Level score is a 10-point scale that weighs the evidence strength based on category. Broadly, highest points are awarded to large clinical studies and lower points are awarded to case studies, in vitro studies, and inferential evidence. Evidence Item Scores are calculated by multiplying a weighted Trust Rating (i.e., one point for each star) by the values assigned to Evidence Level (i.e., A=10, B=5, C=3, D=1, E=0.5). The Molecular Profile Score is a relative measure of the total amount of curation in the database for a specific molecular profile and does not take into account conflicting evidence.

Figure depicting an example evidence score calculation
Figure 1: Evidence Score example calculation

Variants Overview
CIViC variants are usually genomic alterations, including single nucleotide variants (SNVs), insertion/deletion events (indels), copy number alterations (CNVs; such as amplifications or deletions), structural variants (SVs; such as translocations or inversions), and other events that differ from the “normal” genome. In some cases a CIViC variant may represent events of the transcriptome or proteome. For example, ‘expression’ or ‘over-expression’ is a valid variant. New curators should generally avoid proposing new variants that are unlike any already in CIViC. All CIViC Variants are associated with one or more Molecular Profiles with some evidence of clinical relevance (predictive, prognostic, diagnostic, etc).

Figure depicting the data model of a CIViC Variant
Figure 1: Variant Model - Attributes and Associations

Variant Attributes

Attribute

Description

Source

Name

Description of the type of variant (e.g., ‘V600E’, ‘BCR-ABL fusion’, ‘Loss-of-function’, ‘Exon 12 mutations’). Should be as specific and short as possible (i.e., specific amino acid changes).

CIViC

Aliases

Alternative names for this Variant. May be more verbose (e.g., ‘Val600Glu’) versions, dbSNP IDs or alternative nomenclature used in the literature.

CIViC

HGVS Description(s)

User-defined HGVS strings following HGVS nomenclature that represent this Variant at the DNA, RNA or protein level.

CIViC

ClinVar ID(s)

User-defined ClinVar ID referencing this Variant which will be linked directly to ClinVar. A value of “None Specified” indicates that the variant has not been evaluated for a ClinVar ID. A value of “None Found” indicates that an attempt was made to find a matching ClinVar Entry, but none exists. A value of “N/A” indicates that a ClinVar record is not applicable to the variant (e.g. “Overexpression” variants).

CIViC (ClinVar)

Allele Registry ID

Allele Registry identier (CA id) linked to corresponding ClinGen Allele Registry page. This link is automatically generated using the curated Primary Coordinates (chromosome, start, stop, reference base, variant base).

ClinGen Allele Registry

OpenCRAVAT Variant Report

Link to OpenCRAVAT Variant Report. This link is automatically generated using the curated Primary Coordinates (chromosome, start, stop, reference base, variant base).

OpenCRAVAT

Variant Type(s)

One or more terms from the Sequence Ontology that describes the type of variant. Should be the most descriptive term applicable on a given branch (e.g., ‘Conservative Missense Variant’, ‘Stop Gained’, ‘Transcript Fusion’).

CIViC (Sequence Ontology)

Representative Variant Coordinates (Primary Coordinates)

Reference Build

NCBI or GRC human reference assembly version.

CIViC

Ensembl Version

Ensembl annotation build version.

CIViC

Chromosome

Name of the chromosome in which the variant occurs.

CIViC

Start, Stop

Start and stop positions of the variant (1-based genome coordinate). Start must be less than or equal to stop.

CIViC

Reference & Variant Bases

The nucleotide base of the reference and variant allele (e.g. ‘C’, ‘A’).

CIViC

Representative Transcript

Ensembl transcript ID and version number for a known transcript of the gene that contains the variant (e.g. ‘ENST00000263967.3’).

CIViC

Secondary Coordinates

Same as Primary

For fusion variants, the secondary coordinates are used to specify the 3’ partner of the fusion gene.

CIViC

MyVariant.Info

MyVariant Info

Data retrieved from MyVariant.Info using the curated Primary Coordinates (chromosome, start, stop, reference base, variant base) described above as the query. Includes external IDs and links whenever possible with data displayed in several tabs.

MyVariant.Info

Name
The Variant Name describes the specific variant being interpreted for clinical utility. Selecting a Variant Name in the Variant list for a Gene will bring up a Variant specific page with aliases, HGVS expressions, ClinVar identifiers, Variant Type(s) and Molecular Profiles.

Understanding Variant Names
The Variant Name concisely describes a defining feature of the variant for rapid and clear identification. The Variant Name should be the most specific description of the variant that the underlying sources allow. However, names can be generalized to categorical variants (also called “bucket” variants) such as Mutation or Exon 11 Mutation, if more granular detail is not provided. Categorical variants often arise during studies that pool larger numbers of patients with unspecified mutations in a given gene or gene region, in order to reach statistical conclusions. Variant Names often follow HGVS-like conventions (e.g. L858R).

Adding New Variant Names
New CIViC Variant Names are entered into the database at the first instance of curation of evidence for Molecular Profile involving the given Variant. At the time of entering an Evidence Item for a new Molecular Profile, the user generates the Variant and Name by entering it into the Variant Name field, below the Gene Entrez Name field. Unlike Entrez name, which is drawn from a list of predetermined gene names, the variant name is free text written by the curator.

Screenshot of Gene and Variant fields in the Add Evidence form
Figure 1: Screenshot of Gene and Variant fields in the Add Evidence form

Curating Variant Names
When curating the Variant Name field, the most specific Variant Name described by the source should be used (e.g. KRAS G12 or G13 rather than KRAS Exon 2 Mutation). The Variant Name can be very specific [e.g. VHL R176fs (c.528del)], or can refer to a collection of variants fitting a named category (i.e. categorical variants). Examples of categorical variants include KRAS G12 or G13, EGFR Exon 20 Insertion, and PIK3CA Mutation. Categorical variants may be associated with multiple ClinVar entries. The Variant Name field is not limited to genetic events and can include expression or epigenetic alterations such as BRCA1 Underexpression or CDKN2A Promoter Hypermethylation. Other Variant Names, including star-allele nomenclature adopted by the pharmacogenetics field (e.g. DPYD*2A) are also supported. Variant Names can be associated with one or more Variant Types derived from the Sequence Ontology.

General Conventions:

Title case should be used.

Names and HGVS expressions should follow the HGVS 3’ rule.

Protein changes should be written in 1-letter form and exclude the preceding ‘p.’.

HGVS for c. and g. nomenclature may be used and should include the preceding ‘c.’ or ‘g.’ to differentiate it from protein nomenclature.

Shorthand should be avoided (e.g., use Mutation instead of Mut, Expression instead of Exp, etc.) unless part of HGVS nomenclature (e.g., E746_T751delinsVA).

‘or’ rather than ‘/’ should be used to connect variants (e.g. G12 or G13, not G12/G13).

Frameshift Variant Names should use the shorter HGVS-like protein naming style (e.g., P86fs). The longer protein nomenclature, which includes predicted downstream protein consequences can be included as an alias (e.g., P86Afs*46).

Somatic variants are not typically described at the genome or transcript level in publications. Protein-effect level descriptions are appropriate for most somatic variants.

Categorical variants should be singular and exclude the gene name (e.g., Fusion, Rearrangement, Mutation, Frameshift rather than ‘ALK Fusions’).

Splice variants should not use IVS nomenclature.

The table below includes an extensive set of example variants for many of the common variant types supported in CIViC. When curating a new variant, curators should refer to these examples and follow the established conventions wherever possible. The {sequence variant} root concept of Sequence Ontology is implied for Variant Type when it’s not otherwise specified.

Variant name

Gene

Variant type

Application and Notes

V600E

BRAF

Missense Variant

A specific amino acid change. Variant Name encapsulates all the nucleotide changes that could have produced it. Somatic variants are not typically described at the genome or transcript level in publications.

S65W (c.194C>G)

VHL

Missense Variant

A specific amino acid change where the precise nucleotide change is provided or ascertainable. Protein change p. notation is implied, other HGVS notation (e.g. ‘g.’ or ‘c.’) used when applicable. This degree of resolution is typically used for germline variants.

E709A and G719C

EGFR

Missense Variant

Multiple concomitant missense variants in the same gene (e.g. double mutants). Should not be used when patients with different mutations in the same gene are pooled and analyzed.

V600E or V600K

BRAF

Missense Variant, Copy Number Gain {sequence feature}

Different specific missense variants in the same gene but different patients pooled together. The shorthand V600E/K should not be used.

(V600E or V600K) and Amplification

BRAF

Missense Variant, Copy Number Gain {sequence feature}

Complex combination between two different types of variants in the same gene (e.g. missense and copy number gain). Boolean order of operations and parentheses should be used when needed.

V600

BRAF

Protein Altering Variant

Categorical variant involving a single amino acid position with multiple possible changes.

Non-V600

BRAF

Protein Altering Variant

Categorical variant excluding a common hotspot. This variant describes all BRAF mutations that are not at the V600 locus.

*214C (c.641_642insC)

VHL

Stop Lost

Use * rather than Ter to indicate a stop codon.

D770_N771insNPG

EGFR

Conservative In-frame Insertion

In-frame insertion of one or more amino acids.

V560del

KIT

Conservative In-frame Deletion

In-frame deletion of one or more amino acids.

E746_T751delinsVA

EGFR

Delins {sequence feature}

Replacement of one or more amino acids with one or more amino acids.

Y772_A775dup

ERBB2

In-frame Insertion

In-frame duplication of one or more amino acids.

P59fs (c.173_174insT)

VHL

Plus 1 Frameshift Variant, Frameshift Truncation

Insertion of one or more nucleotides into DNA causing a frameshift.

E189fs (c.565del)

VHL

Minus 1 Frameshift Variant, Frameshift Truncation

Deletion of one or more nucleotides causing a frameshift.

I206fs (c.615delinsAA)

VHL

Plus 1 Frameshift Variant, Frameshift Elongation

Replacement of one or more nucleotides with one or more nucleotides causing a frameshift.

A149fs (c.444dup)

VHL

Plus 1 Frameshift Variant, Frameshift Truncation

Duplication of one or more nucleotides inserted directly 3’ of the original copy of that sequence.

W288fs

VHL

Frameshift Variant

All frameshifts originating at the codon containing the designated locus. Used when the specific DNA change resulting in the frameshift is unknown, thus the first amino acid to change is unknown.

Exon 9 Frameshift

CALR

Frameshift Variant

All frameshifts originating in this exon.

Frameshift

MRE11

Frameshift Variant

All frameshifts within a gene.

Exon 11 Mutation

KIT

Coding Sequence Variant

Mutations within specific transcriptional boundaries.

Exon 14 Skipping Mutation

MET

Exon Loss Variant

All mutations causing specific transcriptional consequences.

DNA Binding Domain Mutation

TP53

DNA Binding Site {sequence feature}

Mutations within specific functional boundaries.

Mutation

PIK3CA

Transcript Variant

All genetic variants within a gene. Widest categorical variant name for genetic variants.

EML4-ALK

ALK

Transcript Fusion

Specific gene fusion: GENEA-GENEB. Fusions should be named 5’->3’ where GENEA occurs at the 5’ end of the fusion transcript.

EML4-ALK e6-e20

ALK

Transcript Fusion

Fusion with known specific exon boundaries; specific fusion isoforms.

BCR-ABL T315I

ABL1

Transcript Fusion, Missense Variant

Complex genotype describing a concurrent fusion variant and a missense variant.

Fusion

ALK

Transcript Fusion

Fusion with an unknown partner (common for fusions detected by methods like FISH).

Rearrangement

MLL

Structural Variant

A change in the genetic structure wherein a fusion protein is not necessarily implied to have been created (e.g. translocations, genetic fusions with a regulatory region).

FLT3-ITD

FLT3

In-frame Insertion

Imprecise internal tandem duplications (insertion) with shared consequences.

Exon 1-2 Deletion

VHL

Deletion {sequence feature}

Deletion of specific regions of a gene.

Partial Deletion

VHL

Deletion {sequence feature}

All partial deletions where boundaries are not specified. When the size of the deletion is known but the specific exons are not, “Partial deletion of 0.7 Kb” can be included in the Evidence Statement, but not the Variant Name.

Deletion

VHL

Deletion {sequence feature}

Presumed deletion of the whole gene.

Underexpression

ATRX

N/A

Reduced or eliminated expression of protein or mRNA products, as detected by assays such as Western blots, RT PCR, IHC. Do not use if the causal genomic alteration is known; the alteration would be the variant name.

Loss

ARID1A

N/A

Broadest categorical (bucket) variant in CIViC, to be used when the source describes a mix of genetic (e.g. Deletion), expression (e.g. Underexpression), and deleterious mutation events, or does not clarify how gene loss was ascertained. Loss can be used at the Assertion level to combine Underexpression and deleterious genetic variants.

Amplification

PIK3CA

Transcript Amplification

The number of gene copies is greater than two.

Overexpression

ERBB2

N/A

Increased expression of protein or mRNA products, as detected by assays such as Western blots, RT PCR, IHC. Do not use if the causal genomic alteration is known; the alteration would be the variant name.

Splice Site (c.340+1G>A)

VHL

Splice Donor Variant

A splice variant that changes the 2 base pair region at the 5’ end of an intron.

Splice Site (c.341-2A>C)

VHL

Splice Acceptor Variant

A splice variant that changes the 2 base pair region at the 3’ end of an intron.

Splice Region (c.463+3A>G)

VHL

Splice Donor Region Variant

Splice region within 3-8 bases of the intron.

Splice Region (c.464-4C>T)

VHL

Splice Region Variant

Splice region within 3-8 bases of the intron.

Promoter Hypermethylation

CDKN2A

N/A

Epigenetic modification.

S473 Phosphorylation

AKT1

N/A

Describe the specific phosphorylated residue(s), if known, or the whole gene if >2 residues or unknown residues were phosphorylated.

rs3814960

CDKN2A

UTR Variant

rsIDs can be used when easily understandable protein- or splice- altering p. or c. notations are not available.

DPYD*2A Homozygosity

DPYD

Splice Donor Variant

Pharmacogenomic nomenclature (can be any applicable variant type).

p16 Expression

CDKN2A

N/A

Use when distinct proteins (e.g. p16 vs. INK4) are transcribed from the same locus.

Aliases
Variant Aliases are alternative names, descriptions, or identifiers that differ from the primary CIViC Variant Name and are used to describe alternate names for a variant. Variants may be known by more colloquial terms, amino acid positions that reference transcripts of a different length, alternative IDs, etc. which can be captured here. For example, MTHFR A222V is also known as rs1801133, C677T, and Ala222Val.

These terms are manually curated and are incorporated into the search fields within the CIViC interface. Aliases may include protein changes on alternative transcripts (e.g., D754Y for ERBB2 D769Y), dbSNP IDs, COSMIC IDs or other identifiers used in the literature.




My Variant Info
After manual coordinate curation for a variant, a specifically formatted coordinate expression is automatically generated and used to query myvariant.info. A selected set of MyVariant.info fields are retrieved and displayed on the CIViC variant page, which also includes links to ClinVar, COSMIC and OMIM variant pages. Note that this ClinVar link is in addition to hand curated ClinVar IDs which are also an editable field on the CIViC Variant. MyVariant details also include HGVS expressions which may be used to convert the variant between different genome builds.

This information is automatically extracted from the MyVariant.info database, and is not curated.



Types
Variant Type(s) are used to classify variants by Sequence Ontology terms.

Variant Types permit advanced searching for categories of variants in the CIViC interface and downstream semantic analyses of CIViC variants. Some examples of variant types are listed below.

Curating Variant Types
The most specific term(s) that can be applied to a given variant should be utilized. Use of the Sequence Ontology browser is recommended to identify appropriate terms.

When choosing variant types, selection of multiple terms is supported in order to capture both functional and structural effects of the variant. However, these terms should not be ancestors or descendents of one another, and all selected terms should be descendents of the ‘sequence_variant’ term whenever possible.

Variant Type Guidelines
Choose the most specific terms.

Do not use terms that are ancestors/decendants of each other.

Wherever possible use the ‘sequence_variant’ tree of the sequence ontology.

Curation Guidelines for Specific Sequence Ontology Types
Sequence Ontology Term

Sequence Ontology Definition

Comments

missense_variant

A sequence variant, that changes one or more bases, resulting in a different amino acid sequence but where the length is preserved.

stop_gained

A sequence variant whereby at least one base of a codon is changed, resulting in a premature stop codon, leading to a shortened polypeptide.

Also known as a nonsense variant.

protein_altering_variant

A sequence_variant which is predicted to change the protein encoded in the coding sequence.

frameshift_truncation

A frameshift variant that causes the translational reading frame to be shortened relative to the reference feature.

inframe_deletion

An inframe non synonymous variant that deletes bases from the coding sequence.

inframe_insertion

An inframe non synonymous variant that inserts bases into in the coding sequence.

splice_acceptor_variant

A variant the impacts the RNA splice acceptor site (i.e. at or upstream/3prime of an exon edge)

splice_donor_variant

A variant the impacts the RNA donor acceptor site (i.e. at or downstream/5prime of an exon edge)

[ gene_variant

OR

transcript_variant ]

AND

[ loss_of_function_variant

OR

gain_of_function_variant ]

[ gene_variant: A sequence variant where the structure of the gene is changed.

OR

transcript_variant: A sequence variant that changes the structure of the transcript ]

AND

[ loss_of_function_variant: A sequence variant whereby the gene product has diminished or abolished function.

OR

gain_of_function_variant: A sequence variant whereby new or enhanced function is conferred on the gene product. ]

Depends on situation.

exon_variant

A sequence variant that changes exon sequence.

transcript_fusion

OR RARELY…

gene_fusion

transcript_fusion: A feature fusion where the deletion brings together transcript regions.

OR

gene_fusion: A sequence variant whereby a two genes have become joined.

Depends on situation.

Note that transcript_fusion mentions “deletion” specifically as the genomic alteration, and both gene_fusion and transcript_fusion are children of feature_fusion, which also mentions “deletion” specifically. However, it is assumed that deletion is just one possible mechanism (along with translocation, inversion, etc) for bringing two gene or transcribed regions together. The decision of which term to use therefore rests on the level of specificity. If the genomic event is thought to result in a fusion transcript then “transcript_fusion” is the preferred term.

transcript_fusion

AND

missense_variant

transcript_fusion: A feature fusion where the deletion brings together transcript regions.

AND

missense_variant: A sequence variant that changes one or more bases, resulting in a different amino acid sequence but where the length is preserved.

transcript_translocation

OR

feature_translocation

OR

transcript_fusion

transcript_translocation: A feature translocation where the region contains a transcript.

OR

feature_translocation: A sequence variant, caused by an alteration of the genomic sequence, where the structural change, a translocation, is greater than the extent of the underlying genomic features.

OR

transcript_fusion: A feature fusion where the deletion brings together transcript regions.

Depends on situation.

wild_type

An attribute describing sequence with the genotype found in nature and/or standard laboratory stock.

loss_of_heterozygosity

A functional variant whereby the sequence alteration causes a loss of function of one allele of a gene.

transcript_amplification

A feature amplification of a region containing a transcript.

transcript_ablation

A feature ablation whereby the deleted region includes a transcript feature.

copy_number_change

A sequence variant where copies of a feature (CNV) are either increased or decreased.

loss_of_function_variant

A sequence variant whereby the gene product has diminished or abolished function.

loss_of_function_variant…?

transcript_ablation…?

loss_of_fuction_variant: A sequence variant whereby the gene product has diminished or abolished function.

transcript_ablation: A feature ablation whereby the deleted region includes a transcript feature.

Depends on situation.

exon_loss_variant

A sequence variant whereby an exon is lost from the transcript.

5_prime_UTR_variant

A UTR variant of the 5’ UTR.

3_prime_UTR_variant

A UTR variant of the 3’ UTR.

synonymous_variant

A sequence variant where there is no resulting change to the encoded amino acid.

N/A

The Sequence Ontology does not currently describe expression or epigenetic variants.

Variant Type Examples
Sequence Ontology Term

Examples

missense_variant

G12D

stop_gained

R130*

protein_altering_variant

G12

KINASE DOMAIN MUTATION

frameshift_truncation

V2288fs*1

inframe_deletion

DEL I843

V560DEL

DEL 755-759

inframe_insertion

P780INS

M774INSAYVM

ITD

[ gene_variant

OR

transcript_variant ]

AND

[ loss_of_function_variant

OR

gain_of_function_variant ]

MUTATION

exon_variant

EXON 10 MUTATION

transcript_fusion

OR RARELY…

gene_fusion

EML4-ALK

ALK FUSIONS

transcript_fusion

AND

missense_variant

EML4-ALK G1269A

transcript_translocation

OR

feature_translocation

OR

transcript_fusion

REARRANGEMENT

wild_type

WILD TYPE

loss_of_heterozygosity

LOH

transcript_amplification

AMPLIFICATION

transcript_ablation

DELETION

copy_number_change

COPY NUMBER VARIATION

loss_of_function_variant

LOSS-OF-FUNCTION

loss_of_function_variant…?

transcript_ablation…?

LOSS

exon_loss_variant

EXON 14 SKIPPING MUTATION

5_prime_UTR_variant

5’ UTR MUTATION

3_prime_UTR_variant

3’ UTR MUTATION

N/A

EXPRESSION

NUCLEAR EXPRESSION

CYTOPLASMIC EXPRESSION

OVEREXPRESSION

UNDEREXPRESSION

METHYLATION

PROMOTER METHYLATION

PROMOTER HYPERMETHYLATION




Coordinates
Primary and Secondary Coordinates are manually curated and verified representative genomic coordinates of the variant (Chromosome, Start, Stop, Reference base, and Variant base) for the assigned reference assembly (e.g., GRCh37).

Understanding Coordinates
Primary Coordinates are generated for all Variants. Secondary Coordinates are utilized for structural variants involving two loci (e.g., fusion variants).

Curating Coordinates
Choosing representative coordinates

Although multiple genomic changes can often lead to functionally equivalent alterations (e.g., same amino acid change), CIViC uses representative coordinates to provide user-friendly variant context rather than enumerate all possible alterations that could cause the variant. When choosing a representative variant, it is preferable to use the most common or highly recurrent alteration observed. Genomic coordinates are 1-based with left-shifted normalization and include a specified reference assembly (GRCh37 preferred). Based on manually curated representative coordinates, an automated linkout to the ClinGen Allele Registry is created. This link provides additional information such as unique and referenceable identifiers for every registered variant with links to additional resources (e.g., gnomAD, ClinVar). The ClinGen Allele Registry also provides coordinate conversions between different builds of the human references genome and alternative cDNA transcript sequences. If the required ClinGen Allele does not yet exist, the curator should create a ClinGen account and register it.

Choosing a representative transcript

Multiple transcripts can often be expressed for a single gene. For this reason, a specific protein coding alteration, resulting from a genomic change, should always be expressed relative to a specific/individual transcript sequence. CIViC representative transcripts use the Ensembl archived version 75 (GRCh37), and should always include the transcript version number (i.e., ENST00000078429.1 instead of ENST00000078429). There is rarely only one correct transcript. Representative transcripts must contain the variant but are otherwise chosen based on priority criteria such as: wide use in the literature, having the longest open reading frame or most exons, containing the most common exons between transcripts, or having the widest genomic coordinates. These are consistent with Ensembl’s glossary definition of canonical.

Wherever possible curators should use the Ensembl MANE Select Transcript.

Curation Practice for SNVs and Small Indels
Variant annotation for single nucleotide variants (SNV) and small insertion/deletions (indels) follow a 1-based coordinate system and utilize left-shifted normalization. Reference positions are indicated in green and variant positions in blue. Below in Figure 1, each representation is the text that would be entered into the CIViC Reference Base and Variant Base fields in the Variant Suggested Revision form.

Example SNVs and small indels
Figure 1: Example SNVs and small indels

When selecting a representative variant, utilize the most specific and recurrent variant, whenever possible. For example, there are more than 70 insertions listed in COSMIC that lead to the highly recurrent NPM1 W288fs mutation; however, one 4bp insertion (also known as NPM1-A) accounts for more than 90% of all variant entries. Therefore, the coordinates associated with the NPM1-A variant were chosen as the representative coordinates for the NPM1 W288fs variant in CIViC.

For complex variants such an DelIns variants (combination of both deleted and inserted bases) you should follow the logic of the HGVS nomenclature. Specifically, use the start/stop coordinates to indicate the reference genome position of bases deleted as you would for a small deletion. Then, under Reference Base(s) show the corresponding sequence of bases deleted. Finally, under Variant Base(s) show the sequence of bases inserted (e.g. NC_000003.11:g.10183874_10183881delinsCG would be Chr: 3, Start: 10183874, Stop: 10183881, Ref Bases: ACGGGCCC, Var Bases: CG).

For complex variants such as SNVs in genes involved in fusions (e.g., EML4-ALK C1156Y), enter the genomic position of the SNV.

Categorical variants involving a single amino acid can be indicated by using the three or two base pairs of the corresponding triplet codon that could result in a SNV at that site (see BRAF V600 for example).

Curation Practice for Categorical and Large-scale Variants
Variant annotations for large-scale rearrangements or categorical variants aim to utilize the minimum genomic space that encompasses the range of variants observed for that gene. For example, although PIK3CA amplification can encompass much larger genomic coordinates, the outermost coordinates of the gene PIK3CA are used to define the start and stop coordinates. Similarly, categorical variants that contain mutations within the same domain or exon use the outermost coordinates of that domain or exon. Fusion coordinates are based on the closest exon boundary included in the fusion. Although multiple breakpoints can occur, the most common breakpoint is prefered for the representative coordinate.

Example categorical and large-scale variants
Figure 2: Example *PIK3CA* amplification

Use coordinates that would encompass the most variants that fit the Variant Name to aid others using coordinates to find relevant and similar variants.

For fusions:

Names are always written in a 5’ to 3’ order (e.g. 5’ BCR-ABL 3’);

The Variant is placed under the most ‘important’ gene - e.g. kinase domain - (not repeated under both) which is often the 3’ gene;

Coordinates represent the entire putative fusion transcript including start to end of fused/involved exons of 5’ transcript partner (primary coordinates) and start to end of fused/involved exons of 3’ transcript partner (secondary coordinates).

Curation Practice for representative transcripts
Genes often have multiple transcript representations. CIViC utilizes Ensembl v75 for transcript annotations. The representative transcript for WT1 depicted in blue below was chosen because it has the widest outer coordinates with the most common exons compared to the other transcripts depicted in green. This transcript is further highlighted by *** because it is also designated as the “canonical transcript” by Ensembl using select criteria defined in their glossary of terms.

Example representative transcript for *WT1*
Figure 3: Example representative transcript for *WT1*

There is no one ‘right’ answer for representative transcript.

It must:

contain the variant (except in rare cases like promoter mutations);

be based on an Ensembl transcript and include the transcript version.

It may:

be the transcript with the longest ORF or most exons;

be the transcript that contains the ‘canonical exons’ that are used in many transcripts;

be the variant that has the greatest outer coordinates;

be the transcript that is widely used in literature;

be a transcript that is compatible with interpretation/visualization in the primary literature source.

An IGV reference transcript file containing Ensembl (v75) transcripts can be obtained here (Ensembl-v75_build37-hg19_UcscGenePred_CIViC-Genes.ensGene).

Ensembl canonical transcripts are designated by ***.

Selection of Representative Transcripts for intronic or regulatory variants follow a similar pattern as protein coding variants.


HGVS Expressions
Multiple valid HGVS strings following HGVS nomenclature (see HGVS guidelines) can be entered here to represent a variant at different levels (DNA/RNA/protein).

Understanding HGVS Expressions
The CIViC Variant knowledge model supports The Human Genome Variation Society (HGVS) Expression to describe sequence variation in genomic, RNA, coding DNA, and protein coordinates. HGVS expressions must be entered individually in the Variant editing interface and may capture HGVS entries not described by the representative coordinates. Manual entry is required (e.g., not automatically linked based on representative coordinates) to permit entries for complex or categorical variants and to support alternate transcripts and reference build versions.

Curating HGVS Expressions
HGVS expressions should follow the published HGVS guidelines

HGVS expressions should utilize NCBI and Ensembl transcripts separated by a colon, and followed by the c-dot, p-dot, or g-dot notation style (e.g. ENST00000275493.2:c.2369C>T, NM_005228.4:c.2369C>T, NP_005219.2:p.Thr790Met)

Once variant coordinates have been entered and approved and a variant is linked to the ClinGen Allele Registry, that resource can be a convenient source of useful HGVS expressions to add to the Variant.

ClinVar IDs
The CIViC Variant knowledge model supports curated ClinVar IDs for each variant. ClinVar IDs must be entered individually in the Variant editing interface and may capture ClinVar IDs not described by the representative coordinates. Manual entry is required (e.g., not automatically linked based on representative coordinates) to permit entries for complex or categorical variants and to support alternate transcripts and reference build versions.

Curating ClinVar IDs
Curators can associate multiple valid ClinVar IDs with a variant which will link directly to that ClinVar entity, allowing manual associations not easily resolved by programmatic methods. For more general variants, more than one ClinVar ID may be appropriate. Enter N/A for variants that aren’t expected to have a ClinVar record (e.g., Expression). Enter NONE FOUND to indicate a search was completed and no ClinVar record was found. This allows for the possibility of future searches and updates later.

Categorical variants are associated with multiple ClinVar entries, if applicable. In the example below, each of the ClinVar IDs links to a specific missense variant that can change KRAS at amino acid position G12.

Screenshot of Variant KRAS G12 showing multiple ClinVar entries
Figure 1: Screenshot of Variant KRAS G12



Genes
The gene entity within the CIViC database includes several useful features for assessing the clinical relevance of variants (Figure 1). The first is a human curated gene-level summary describing the gene’s clinical relevance with associated sources. The second feature is an external link to The Drug Gene Interaction Database, which can be selected to learn more about specific drug-gene interactions and the druggable genome. The third feature is an external link to the ProteinPaint resource allowing a view of variant recurrence data for the gene in the context of alternative transcripts, known protein domains, etc. The fourth feature includes gene-level details (e.g., gene aliases, domains, pathways) pulled in from MyGene.info with a link to additional details.

Understanding Genes

In order to be listed in CIViC a Gene must have at least one clinical Evidence Item that has been curated from the literature and associated with at least one Molecular Profile (variant) of the gene. A new Gene record will be created automatically when the first Evidence Item is assigned to the Gene. The official gene name according to Entrez Gene (assigned by HGNC) is used. Alternative gene names or “aliases” are autopopulated from MyGeneInfo and searchable throughout the database. However, new Evidence Items must be associated with an official gene symbol to prevent ambiguity.

A figure showing a CIViC Gene's attributes, associations, computed properties
Figure 1: A CIViC Gene's attributes, associations, computed properties

Gene Attributes

Attribute

Description

Source

Name

Entrez symbol of the gene.

EntrezDB

Summary

User-defined summary of the clinical relevance of this Gene. Curation efforts should aim to concisely summarize the relevance of Molecular Profiles (simple or complex variants) in this gene to treatment prediction, prognosis, diagnosis, predisposition, oncogenicity and function. The summary should also provide an overview of the most relevant cancer types. The summary may also include relevant mechanistic information such as pathway interactions, functional alterations caused by variants within this Gene (i.e., activating, loss-of-function, etc.), and normal functions key to its oncogenic properties.

CIViC

Sources (PubMed IDs)

A list of PubMed IDs referring to evidence supporting statements made in the Gene’s description. Source descriptions (e.g. ‘Weisberg et al., 2007, Nat. Rev. Cancer’) are pulled from the PubMed database at the time of submission, and are not editable.

CIViC (PubMed)

MyGene.Info

MyGene Info

Data retrieved from MyGene.Info using the HGNC symbol as the query. Includes synonyms, protein domains, and pathways with additional data displayed by clicking the “Details” button.

MyGene.Info

Curating Genes

Most of the information within the Gene entity is automatically imported after the gene is created. These automatically generated fields include: 1) information from MyGene.info and 2) link to DGIdb details, 3) link to ProteinPaint.

Curators can add gene-level summaries and sources associated with the gene-level summaries. These clinical summaries should include relevant cancer subtypes, specific treatments for the gene’s associated variants, pathway interactions, functional alterations caused by the variants in the gene, and normal/abnormal functions of the gene with associated roles in oncogenesis. The sources used for gene-level summaries should correspond to Pubmed IDs.

Contents:

Gene Name
Understanding Gene Names
Curating Gene Names
Summary
Understanding Gene Summaries
Curating Gene Summaries
MyGene.info
Understanding MyGene.info


Gene Name
The CIViC Gene Name utilizes official Entrez Gene Names from the Entrez Gene database.

Understanding Gene Names
The CIViC Gene Name utilizes official Entrez Gene Names from the Entrez Gene database, which are approved by the HUGO Gene Nomenclature Committee (HGNC). Curators must enter a valid Entrez Gene Name (e.g., TP53) and should verify the correct entry against the Entrez Gene ID automatically displayed by the CIViC interface. Alternative Gene Names (Aliases/Synonyms) are imported from Entrez and are searchable throughout the database.

Curating Gene Names
Only Entrez Gene Names are accepted for the CIViC Gene Name field. Curators should verify the correct entry against the Entrez Gene ID automatically displayed by the CIViC interface.

Summary
The CIViC Gene Summary provides a high-level overview of clinical relevance of cancer variants for the gene.

Understanding Gene Summaries
A CIViC Gene Summary should be created to provide a high-level overview of clinical relevance of cancer variants for the gene. Gene Summaries should focus on emphasizing the clinical relevance from a molecular perspective and should not describe the biological function of the gene unless necessary to contextualize its clinical relevance in cancer. Gene Summaries should include relevant cancer subtypes, specific treatments for the gene’s associated variants, pathway interactions, functional alterations caused by the variants in the gene, and normal/abnormal functions of the gene with associated roles in oncogenesis. A CIViC Gene Summary should generally be limited to one or two paragraphs and cite relevant reviews to further support the gene’s clinical relevance in cancer.

Annotated screenshot of the Gene view in CIViC
CIViC Gene View for BRAF

Curating Gene Summaries
The Gene Summary is a user-defined description of the clinical relevance of this gene. Just as a Molecular Profile Summary should be a synthesis of Evidence Statements for a Molecular Profile, the Gene Summary should be a synthesis of the Molecular Profile Summaries for a Gene.

This summary should also discuss the relevance of the Gene to different cancer types, patient outcomes and treatment decisions, and highlight differences and similarities between different variants of this gene or different molecular profiles involving this gene. This section may include information about the gene product’s pathway interactions, functional alterations caused by variants within this gene and normal functions that are relevant to its association with cancer. Although individual evidence statements do not capture biological/mechanistic impact of variants on gene function, the Gene Summary is a place where this information may be summarized.

A CIViC Gene Summary should generally be limited to one or two paragraphs and cite relevant reviews for a more extensive discussion of clinical relevance of the gene in cancer.

Sources

Although in-line citations are not currently supported, citations can be tracked using the Sources field and entered by specifying the PubMed ID associated with the publication. The addition of citations used to generate the gene description, particularly relevant reviews, is highly encouraged with the intention of directing users to more in-depth information.

The sources used for Gene Summaries should be derived from Pubmed and, unlike typical CIViC Evidence Items, may include review articles.



Variant Groups
Variant Groups provide user-defined grouping of Variants within and between genes based on unifying characteristics.

Understanding Variant Groups

Variant groups allow users to group variants from a single Gene or multiple Genes that have similar clinical consequences.

Example uses:

Variants that confer resistance/sensitivity to a class of drugs (e.g., EGFR TKI Resistance)

Categorical or Bucket Variants (e.g., BRAF V600)

Variants with strong data to support a very similar effect on protein function (e.g., loss-of-function, activating)

Functional Characteristics (e.g., Fusion Groups)

Variants that can be effectively combined when considering patient outcomes/treatment

Variant groups can associate multiple related variants within or between genes. Each variant can belong to one or more variant groups, these act to combine functionally similar or clinically related variants into a single entity. For example, ‘FGFR Fusions’ is a group that contains several gene fusions where FGFR2 (or FGFR3) is involved in a fusion with various 3’ partner genes, and ‘Imatinib Resistance Mutations’ is a group of variants that confer resistance to imatinib treatment. A variant group may also contain variants from multiple genes. For example, the group ‘EGFR TKI Resistance’ consists of variants in EGFR, MET, and KRAS.

Variant Group Attributes

Variant Group Attributes and Associations
Figure 1: Variant Group Attributes and Associations

Attribute

Description

Source

Name

Name of the Variant Group

CIViC

Summary

User-defined summary of the clinical relevance of this variant group.

CIViC

Sources (PubMed IDs)

A list of PubMed IDs referring to evidence supporting statements made in the Variant Group’s description. Source descriptions (e.g. ‘Weisberg et al., 2007, Nat. Rev. Cancer’) are pulled from the PubMed database at the time of submission, and are not editable.

CIViC (PubMed)

Variants

User-defined list of variants in the variant group.

CIViC

CURATING VARIANT GROUPS

Variants within a Variant Group can be derived from different Gene Records.

Create a Variant Group

Users with Editor or Admin roles are allowed to create a new Variant Group. To create a new Variant Group use the “Add Variant Group” button below the list of Variants on any Gene/Variant page. Multiple Variants from multiple Genes may then be added by using the + button next to the Variant field. Note that a Variant must exist in CIViC in order to be added to a Variant Group. To exist, a Variant must have at least one Evidence Statement. You can add a new Variant by creating a new Evidence Item using the Add Evidence form.

Add to a Variant Group

Variants can be added to a Variant Group by using the ‘edit’ function of a Variant Group.

Contents:

Summary
Understanding Variant Group Summaries
Curating Variant Group Summaries

Summary
Variant Groups provide user-defined grouping of Variants within and between genes based on unifying characteristics.

Understanding Variant Group Summaries
This is a user-defined description of the clinical relevance of this variant group. This description should include the rationale for grouping these variants together, summarize their relevance to cancer diagnosis, prognosis or treatment and highlight any treatments or cancers of particular relevance. Cancers or treatments where grouping this set of variants is not appropriate should also be highlighted.

Curating Variant Group Summaries
Although in-line citations are not currently supported, the addition of citations used to generate the variant group description, particularly relevant reviews, is highly encouraged with the intention of directing other users to more in-depth information. Citations can be added using the Sources field and entered by specifying the PubMed ID associated with the publication.



Sources
Attributes, associations and computed properties of a Source
Figure 1: Attributes, associations and computed properties of a Source

Contents:

Source Types
PubMed Sources
ASCO Sources
ASH Sources


