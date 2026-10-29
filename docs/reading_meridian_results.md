# Reading Meridian model results responsibly

**Workshop context:** Fictional national e-commerce business, weekly USD revenue KPI, three advertising channels, and one external demand index plus a promotion treatment.

| Output | What it means | What it cannot prove |
|---|---|---|
| Model fit: R², MAPE, wMAPE | Agreement of model predictions and observed training KPI | That estimated channel effects are causal |
| Baseline | Modeled outcome in absence of the included media activity, conditional on specification | Truly observed no-advertising sales |
| Channel contribution | Estimated incremental KPI attributed to modeled media | Platform-reported conversions or experimental certainty |
| Historical ROI | Modeled incremental revenue divided by spend (revenue-per-dollar metric) | Net profit after product costs |
| Marginal ROI | Estimated extra revenue from an extra unit of spend locally | A constant return across all spending levels |
| Response curve | How spend changes model-estimated incremental revenue at historical flighting patterns | Guaranteed results under different creative, targeting, or prices |
| CPIK | Spend divided by modeled incremental KPI | Cost per customer when the KPI is dollars |
| R-hat | Between-chain/within-chain convergence diagnostic, ideally close to 1 | Correct causal specification or good predictions |

## Reading the R-hat plot

An R-hat near 1 indicates consistency across MCMC chains. The workshop screenshot has visible R-hat values very close to 1, approximately below 1.01; this is a reassuring **sampling diagnostic**, not a validation of the marketing conclusions. Also inspect effective sample size (ESS), divergences, prior sensitivity, residuals, and out-of-sample performance.

## Before approving a budget change

1. Compare previous and proposed **total** spend, not just lift in incremental revenue.
2. Read the relevant response curves and ensure the proposed spend is within a plausible range.
3. Inspect uncertainty, causal assumptions, and possible channel collinearity.
4. Where possible, cross-check against lift experiments and business margin information.
5. Prefer controlled reallocations when explaining why a higher modeled outcome need not justify a larger total budget.

## Important unit distinction

This specific notebook models **revenue**, so plotted “incremental KPI” is incremental USD revenue. A different model can use counts of conversions and optionally a separate revenue-per-conversion value, but **we have not done that in this workshop**.
