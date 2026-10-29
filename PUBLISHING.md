# Publishing this lecture project to GitHub

This folder is prepared as a **standalone public GitHub repository**, without any local credentials, trained model files, or private user data. The attached notebook contains no executed cell outputs or personal filesystem paths.

## Suggested repository settings

- **Repository name:** `marketing-measurement-meridian`
- **Description:** `Lecture materials and an educational Google Meridian Bayesian MMM notebook: attribution, incrementality, response curves, budget scenarios and AI-driven marketing.`
- **Visibility:** Public (only if you are comfortable publishing your name and lecture materials)
- **GitHub topics:** `marketing-mix-modeling`, `google-meridian`, `bayesian-statistics`, `marketing-analytics`, `causal-inference`, `jupyter-notebook`, `education`
- **Initialize with README:** No (this package has its own README)
- **License:** Choose a license deliberately if you want to permit reuse; none is supplied by default.

## Option A — Publish a new repository using Git

1. Create an empty repository at <https://github.com/new> under the GitHub account `jawharjoe`, using the name above.
2. Extract the project ZIP on your Mac, and in Terminal navigate to the extracted directory.
3. Run:

```bash
git init -b main
git add .
git commit -m "Add Meridian MMM lecture materials and synthetic workshop"
git remote add origin https://github.com/jawharjoe/marketing-measurement-meridian.git
git push -u origin main
```

GitHub may ask you to authenticate using a credential manager, GitHub CLI or a personal access token. Never paste tokens in the notebook, README, or commits.

## Option B — GitHub's website

Create an empty GitHub repository, then choose **Add file → Upload files** and upload the contents of this extracted folder (preserving directory structure). Commit the upload.

## After publishing

- Add the GitHub link to your LinkedIn post, speaker bio, presentation follow-up, and résumé/project portfolio.
- Optionally pin the repository on your GitHub profile.
- Verify the notebook opens in GitHub's notebook renderer and the PDF slides render correctly.
- Consider adding a selected open-source license and a short recording excerpt only if you own the rights and have participant permissions.

**Do not upload:** Jupyter authentication URLs/tokens, actual private customer data, model dumps containing privileged inputs, chat logs, or unredacted screenshots from private systems.
