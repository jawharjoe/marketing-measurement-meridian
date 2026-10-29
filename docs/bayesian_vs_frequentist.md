# Bayesian vs. frequentist reasoning: a practical primer

## First, a coin toss

A coin is tossed **10 times** and lands **heads 7 times**. Let `p` be the unknown probability of heads.

**Frequentist:** Treat `p` as a fixed unknown parameter. The maximum-likelihood estimate is `p̂ = 7/10 = 0.70`. A confidence interval comes from a method that would cover the true fixed probability at its stated frequency across repeated experiments. This is not a statement that `p` has a 95% probability of lying in this one realized interval.

**Bayesian:** Describe uncertainty about `p` with a prior. Starting with a uniform `Beta(1,1)` prior and observing 7 heads and 3 tails gives a `Beta(8,4)` posterior. This lets us ask for the posterior probability that `p > 0.5` (about **88.7%**, conditional on that prior and binomial model). With only 10 tosses, neither approach establishes the coin is unfair with certainty.

## How the distinction appears in MMM

| Question | Frequentist MMM | Bayesian MMM |
|---|---|---|
| What are unknown effects? | Fixed unknown parameters | Posterior distributions over uncertain parameters |
| How do we estimate them? | e.g. OLS, Ridge, optimization and bootstrap | Prior + likelihood → posterior, often approximated using MCMC |
| How do we communicate uncertainty? | Confidence intervals, standard errors, bootstrap | Credible intervals, probabilities of business events |
| How can experiment results help? | Constraints, calibration, joint estimation | Experiment-informed priors, calibration, joint modeling |
| What are the trade-offs? | Fast/simple models, long-run inference properties | Flexible probability statements, but prior and computation sensitivity |
| Examples | Classical econometric regression, Meta Robyn | Google Meridian, PyMC-Marketing |

## Why choose a Bayesian method for this class?

Marketing is observational: media spend and demand move together. A Bayesian framework makes assumptions through priors visible, can incorporate credible external evidence, and expresses posterior uncertainty for budget decisions. **However, Bayesian inference does not discover the correct external controls automatically.** Causal assumptions, identification, and validation matter in both approaches.

## Common misconceptions

- **“Bayesian automatically solves collinearity.”** No. Priors can regularize estimates but cannot create information missing from the data.
- **“Frequentist means no assumptions.”** No. Controls, functional form, regularization and sampling designs still embody assumptions.
- **“Small samples mean Bayesian always wins.”** No. Weak data often means the posterior depends strongly on priors.
- **“R-hat near 1 means the marketing effect is causal.”** No. It means the sampling chains appear consistent, not that the model is correctly specified.
- **“The highest R² is the best causal MMM.”** No. Predictive fit and causal identification are different goals.

## A quick classroom question

> If we simultaneously increase Meta and YouTube every Black Friday, can a regression always separate the impact of the two channels from holiday demand?

No. The data need sufficient independent variation, credible assumptions, and often experimental evidence. Neither Bayesian nor frequentist methodology resolves that automatically.

**Further reading:** [Meridian](https://developers.google.com/meridian) · [Robyn](https://facebookexperimental.github.io/Robyn/) · [PyMC-Marketing](https://www.pymc-marketing.io/)
