# Data dictionary — fictional national e-commerce campaign

Each row represents one Monday-starting week. The dataset is synthetic, not real advertising or customer data. Generated data may embed relationships that are not fully identifiable to MMM.

| Column | Unit | Role in the notebook |
|---|---|---|
| `week` | YYYY-MM-DD | Weekly time coordinate |
| `revenue` | USD | Dependent variable / Meridian KPI |
| `google_search_spend` | USD | Paid Search expenditure |
| `google_search_impressions` | impressions | Paid Search media execution |
| `meta_spend` | USD | Meta expenditure |
| `meta_impressions` | impressions | Meta execution |
| `youtube_spend` | USD | YouTube expenditure |
| `youtube_impressions` | impressions | YouTube execution |
| `consumer_demand_index` | index (unitless) | External demand proxy / model control |
| `promotion` | binary (0/1) | Advertiser-controlled non-media treatment |

**Observations:** 156 continuous weeks, January 2, 2023 through December 22, 2025 (the notebook dates determine the precise period; no assumptions of December 29). There are no geography identifiers, user-level records, platform conversion counts, clicks, or customer-level attribution fields.

**Channel totals over this synthetic period:** Search $11,278,020.56 · Meta $7,317,416.47 · YouTube $4,520,780.28. Combined $23,116,217.31 (rounding may differ by $0.01).

**Caution:** Treatment assignments are observational in the simulation and the notebook does not include a ground-truth causal effect benchmark. It does not establish causal identification solely by fitting a model.
