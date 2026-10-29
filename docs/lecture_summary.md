# Lecture summary — Marketing Measurement: From Attribution to Influence

*Universidad Galileo student conversation · October 28, 2026 · Mohammed Jawhar*

## The central idea

**A conversion is the end of a customer journey, not proof of which marketing interaction caused it.** The talk introduces the measurement questions that lead from attribution to incrementality, shows a beginner-friendly Meridian example, and closes with how AI is changing marketing strategy.

## Slide-by-slide speaking prompts

| Slide | Theme | Core message |
|---|---|---|
| 1 | From attribution to influence | Data science should support credible marketing decisions, not just produce scores |
| 2 | What makes somebody buy? | Product, price, timing, trust, and multiple marketing touches all matter |
| 3 | Attribution | Last-click or multi-touch credit assignment is not equivalent to causal impact |
| 4 | Incrementality | Ask what would have happened without the campaign (the counterfactual) |
| 5 | Uncontrolled marketing | Holidays, promotions, competitors, macro trends, and selection can confound estimates |
| 6 | MMM in plain language | Decompose an outcome into modeled baseline, media effects, controls, and noise |
| 7 | Practical Meridian example | Inspect synthetic data, R-hat/model fit, response curves, and incremental revenue under budget changes |
| 8 | Bayesian vs. frequentist | Both can work; Bayesian gives a transparent prior-to-posterior decision framework, but neither guarantees causality |
| 9 | Generative AI and marketing | Personalization and automation create opportunities alongside hallucination, privacy, and trust risks |
| 10 | From 7Ps to proposed 7Gs | The research framework raises questions about AI-driven influence; reliable measurement is still the challenge |

## Five-minute walkthrough of the notebook

1. **Data:** 156 weekly observations from a fictional national e-commerce business; Search, Meta, YouTube, demand index, and promotion.
2. **KPI:** revenue (USD)—**not conversion counts** in this particular fitted example.
3. **Model:** Meridian learns parameters governing baseline, media carryover, diminishing returns, and uncertainty.
4. **Evaluation:** inspect R-hat, posterior predictive/model fit, and whether modeled baseline and effects are plausible.
5. **Decisions:** move budget sliders and compare *modeled incremental revenue* before and after; hold overall budget fixed when demonstrating reallocations.

## Discussion prompts

- A company increases advertising every holiday, and sales rise. What else could cause the association?
- What makes a variable a useful external control rather than noise or a consequence of advertising?
- If more spending predicts more revenue, is the change necessarily profitable?
- Would you approve a $1M reallocation based only on MMM posterior probabilities?
- In AI-mediated journeys, how should we measure trust as well as conversion?

## Closing takeaway

> The future of marketing measurement is not merely better prediction or more persuasive AI. It is evidence-driven decisions: identifying meaningful signals, measuring incremental effects, acknowledging uncertainty, and protecting customer trust.

[Slide deck](../slides/Marketing_Measurement_From_Attribution_to_Influence.pptx) · [Notebook](../notebooks/01_meridian_mmm_workshop.ipynb) · [Reading guide](marketing_4p_7p_7g.md)
