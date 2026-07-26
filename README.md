# Exoplanet Classification Using Machine Learning

### A systematic investigation of predictive performance, generalization, interpretability, probability reliability, and scientific robustness

This project investigates whether measurable **host-star properties** contain predictive information about whether an observed exoplanet belongs to a defined **gas-giant class**.

Rather than stopping after training a classifier, the project evaluates the complete scientific machine-learning workflow:

> **Data → Modeling → Evaluation → Interpretation → Calibration → Generalization → Robustness → Scientific Limitations**

The central question is not simply:

> **Can a machine-learning model classify gas giants?**

It is:

> **How reliable, interpretable, stable, and scientifically defensible are the conclusions drawn from that model?**

---

## Research Question

Can measurable host-star properties be used to predict whether an observed exoplanet is a gas giant, and do the resulting predictive relationships remain stable across:

* Different models
* Different train/test partitions
* Repeated cross-validation
* Astronomical subgroups
* Alternative target definitions
* Small perturbations to measured stellar properties
* Multiple independent interpretation methods

The project deliberately separates **predictive performance** from **scientific interpretation**.

A model can perform well without its probabilities being well calibrated, its predictions being equally reliable across feature space, or its learned relationships representing causal physical mechanisms.

---

# Project Overview

The study is organized into **nine focused notebooks**, each addressing a distinct scientific question.

| Notebook | Scientific Question                                                    |
| -------- | ---------------------------------------------------------------------- |
| **01**   | What data are available?                                               |
| **02**   | How do we construct the machine-learning problem?                      |
| **03**   | Which model performs best?                                             |
| **04**   | What has the selected model learned, and where does it fail?           |
| **05**   | Are the model's probability outputs reliable?                          |
| **06**   | How stable and generalizable is model performance?                     |
| **07**   | Do multiple analyses support the same feature interpretation?          |
| **08**   | Are the conclusions robust to definitions and measurement uncertainty? |
| **09**   | What can we genuinely conclude scientifically?                         |

Each notebook has a distinct purpose rather than combining the entire analysis into one large modeling notebook.

---

# Features and Target

The final modeling analysis uses three measurable host-star properties:

| Feature   | Description                   |
| --------- | ----------------------------- |
| `st_teff` | Stellar effective temperature |
| `st_rad`  | Stellar radius                |
| `st_met`  | Stellar metallicity           |

The target is a binary classification label identifying whether an exoplanet belongs to the defined **gas-giant class**.

The target definition is based on planetary-radius criteria established during the data-construction stage.

The project later tests whether the scientific conclusions remain stable when reasonable alternative target thresholds are used.

---

# Methodology

## 1. Data Preparation

The initial notebooks establish the dataset and construct the machine-learning problem.

The preprocessing workflow includes:

* Dataset inspection
* Duplicate handling
* Missing-value analysis
* Feature selection
* Target construction
* Dataset integrity checks
* Train/test partitioning
* Preparation of modeling datasets

The modeling data are stored in processed form for reproducibility.

---

## 2. Model Development and Selection

Multiple classification models are evaluated using a consistent modeling procedure.

The project compares:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting

The final Random Forest configuration is selected during model development and remains fixed for the subsequent scientific analyses.

Later notebooks do not repeatedly optimize the model simply to improve individual results.

This is intentional.

Once the model is selected, the remaining analyses investigate:

> **What does this model learn, how reliable is it, and how robust are its conclusions?**

---

# The Nine-Notebook Analysis

## Notebook 01 — Data Exploration and Preprocessing

### Core question

> **What data are available?**

This notebook examines the source exoplanet dataset and establishes the data used for the study.

The analysis includes:

* Dataset structure
* Variable availability
* Missingness
* Duplicate observations
* Feature distributions
* Initial data-quality assessment

---

## Notebook 02 — Machine-Learning Problem Construction

### Core question

> **How do we construct the machine-learning problem?**

This notebook defines:

* The prediction target
* The target-labeling framework
* The selected host-star features
* The modeling dataset
* The train/test partition
* Data-processing decisions used by later notebooks

The resulting processed datasets provide the foundation for the rest of the project.

---

## Notebook 03 — Model Comparison and Selection

### Core question

> **Which model performs best?**

Candidate classifiers are evaluated using multiple metrics rather than accuracy alone.

The analysis considers:

* Accuracy
* Precision
* Recall
* F1 score
* ROC-AUC
* Average Precision
* Confusion matrices
* Classification reports

The Random Forest is selected as the reference model for the remainder of the project.

Its configuration is then held fixed for subsequent robustness and interpretation analyses.

---

## Notebook 04 — Model Behavior and Error Analysis

### Core question

> **What has the selected model learned, and where does it fail?**

This notebook investigates the behavior of the selected Random Forest beyond a single performance score.

The analysis examines:

* Model performance
* Confusion patterns
* Misclassified observations
* Feature importance
* Permutation importance
* Model behavior across the feature space

The purpose is to understand not only whether the model predicts correctly, but also:

> **Which observations does it struggle with, and what patterns appear to influence its predictions?**

---

## Notebook 05 — Probability Calibration and Prediction Reliability

### Core question

> **Can the model's probability outputs be trusted?**

A classification model's predicted probability is not automatically a reliable probability estimate.

This notebook evaluates:

### Calibration curves

Comparing:

> Predicted probability

against:

> Observed frequency of gas giants

### Reliability tables

Probability bins are used to compare:

* Number of observations
* Mean predicted probability
* Observed gas-giant frequency

### Brier score

The Brier score provides a quantitative measure of probabilistic prediction error.

### Calibration comparison

The analysis compares probability reliability across:

* Logistic Regression
* Random Forest
* Gradient Boosting

### Calibration methods

The Random Forest's uncalibrated probabilities are compared with calibrated alternatives, including:

* Sigmoid / Platt calibration
* Isotonic calibration

This notebook deliberately distinguishes between:

> **A model that classifies well**

and:

> **A model whose numerical probabilities correspond well to observed frequencies.**

---

## Notebook 06 — Generalization and Subgroup Performance

### Core question

> **How stable and generalizable is model performance?**

### Random-seed robustness

The modeling process is repeated across multiple stratified train/test partitions using different random seeds.

Performance is summarized using:

* Mean
* Standard deviation
* Minimum
* Maximum

for metrics including:

* Accuracy
* F1
* ROC-AUC
* Average Precision

This tests whether the original result depended heavily on one particular split.

### Repeated stratified cross-validation

Repeated stratified cross-validation provides a stronger estimate of performance variability than a single cross-validation run.

The analysis evaluates:

* Accuracy
* Precision
* Recall
* F1
* ROC-AUC
* Average Precision

### Training versus validation versus test performance

The notebook compares:

> Training performance
> ↓
> Cross-validation performance
> ↓
> Held-out test performance

Generalization gaps are calculated to investigate potential overfitting.

### Subgroup performance

The model is also evaluated across scientifically meaningful regions of host-star feature space, including groups defined by:

* Stellar effective temperature
* Stellar radius
* Stellar metallicity

This asks:

> **Does overall performance hide weaknesses in particular regions of astronomical parameter space?**

---

## Notebook 07 — Feature Contribution and Scientific Pattern Agreement

### Core question

> **Do multiple independent analyses support the same scientific interpretation?**

This notebook brings together several complementary approaches.

### Feature ablation

The model is compared using:

* All three features
* All features except `st_teff`
* All features except `st_rad`
* All features except `st_met`

This tests how predictive performance changes when individual features are removed.

### Single-feature and feature-combination models

The analysis evaluates:

* `st_teff`
* `st_rad`
* `st_met`
* `st_teff + st_rad`
* `st_teff + st_met`
* `st_rad + st_met`
* All three features

This helps distinguish between features that are:

* Individually predictive
* Complementary
* Potentially redundant

### SHAP analysis

SHAP is used to investigate:

* Global feature contribution
* Direction of feature influence
* Individual predictions

The analysis is focused on interpretation rather than presenting SHAP as a separate modeling objective.

### Direct analysis of the underlying data

The project also steps away from machine learning and directly compares the observed feature distributions of:

* Gas giants
* Non-gas giants

For each feature, the analysis examines:

* Distributions
* Medians
* Interquartile ranges
* Binned gas-giant frequencies

The key distinction is:

> **The model learned this pattern**

versus:

> **The underlying dataset contains this observable association**

### Interpretation agreement

Evidence is compared across:

* Random Forest impurity importance
* Permutation importance
* SHAP
* Feature ablation
* Feature-combination models
* Direct data patterns

The goal is not to force every method to produce identical feature rankings.

Disagreement can itself be informative, potentially reflecting:

* Feature redundancy
* Correlation
* Nonlinear relationships
* Model-specific behavior
* Different statistical questions

---

## Notebook 08 — Robustness to Scientific Definitions and Measurement Uncertainty

### Core question

> **Would the conclusions change if the target definition or measured stellar properties changed slightly?**

### Alternative target definitions

The gas-giant radius threshold is varied across reasonable alternatives.

For each target definition, the analysis examines:

* Class balance
* Model performance
* Feature importance
* Error patterns

This tests whether the scientific conclusions depend heavily on one arbitrary threshold.

### Feature perturbation

Small perturbations are applied to:

* `st_teff`
* `st_rad`
* `st_met`

The resulting changes in model output are measured using:

* Probability change
* Mean absolute probability change
* Classification flip rate

### Stability versus confidence

The analysis compares perturbation sensitivity for:

* Predictions near the classification boundary
* Predictions far from the classification boundary

This tests whether uncertain predictions are also the predictions most sensitive to small changes in measured inputs.

---

## Notebook 09 — Scientific Limitations and Final Synthesis

### Core question

> **What can we genuinely conclude from this study?**

The final notebook does not develop another major model.

Instead, it evaluates the scientific context and limitations of the complete analysis.

The analysis considers:

### Feature-space coverage

Whether some regions of the astronomical parameter space are sparsely represented.

### Missingness and dataset composition

How preprocessing and missing measurements affect the final modeling sample.

### Class imbalance

Why accuracy alone is insufficient and why multiple performance metrics are necessary.

### Measurement uncertainty

The fact that stellar properties and planetary radii are measured estimates rather than perfectly known quantities.

### Observational selection effects

The observed exoplanet population is not necessarily a random sample of all planets that exist.

Detection may depend on factors such as:

* Planet size
* Orbital period
* Stellar properties
* Transit geometry
* Detection method
* Observational sensitivity

Therefore, the results describe patterns in the observed dataset rather than automatically describing the entire underlying exoplanet population.

### Host-star group structure

If multiple planets orbit the same star, row-based splitting may allow planets from the same stellar system to appear in both training and testing partitions.

This could make the test set less independent than it appears.

The ability to fully evaluate this issue depends on whether host-star identifiers are retained in the processed data.

### Final scientific synthesis

The final notebook brings together the conclusions from all previous analyses.

---

# Key Scientific Principles

This project deliberately avoids treating machine-learning output as automatically equivalent to scientific explanation.

The following distinctions are central:

### Prediction is not causation

A feature can be useful for prediction without being the physical cause of the predicted outcome.

### Feature importance is not physical importance

Different feature-importance methods answer different statistical questions.

### Accuracy is not probability reliability

A classifier can rank observations effectively while producing poorly calibrated probabilities.

### Random-split stability is not universal generalization

A model can be stable across random partitions while still performing differently on a genuinely different population.

### Model interpretation is stronger when independently supported

Confidence in a descriptive pattern increases when multiple analyses broadly agree, including direct analysis of the underlying data.

---

# Repository Structure

```text
exoplanet-classification-ml/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── exoplanets_clean.csv
│       ├── ml_ready_dataset.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       └── configuration files
│
├── models/
│   ├── logistic_regression.joblib
│   ├── decision_tree.joblib
│   ├── random_forest.joblib
│   └── other saved model artifacts
│
├── notebooks/
│   ├── 01_*.ipynb
│   ├── 02_*.ipynb
│   ├── 03_*.ipynb
│   ├── 04_*.ipynb
│   ├── 05_*.ipynb
│   ├── 06_*.ipynb
│   ├── 07_*.ipynb
│   ├── 08_*.ipynb
│   └── 09_*.ipynb
│
├── outputs/
│   └── generated analysis results
│
├── images/
│   └── selected visualizations
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Reproducibility

Clone the repository:

```bash
git clone https://github.com/aksharabharath/exoplanet-classification-ml.git
cd exoplanet-classification-ml
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

The notebooks should then be executed in numerical order:

```text
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09
```

Each stage builds on datasets, models, or conclusions established in earlier stages.

---

# Technology Stack

* **Python**
* **Jupyter Notebook**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **SHAP**
* **Joblib**

---

# Limitations

The conclusions of this study should be interpreted within the scope of the analyzed data and methodology.

Important limitations include:

* Observational selection effects
* Measurement uncertainty
* Target-definition sensitivity
* Missing data and preprocessing decisions
* Class imbalance
* Sparse regions of feature space
* Potential dependence between planets orbiting the same host star
* The distinction between predictive association and physical causation

The model should therefore not be interpreted as proving that host-star properties causally determine whether an exoplanet is a gas giant.

---

# Final Scientific Conclusion

Within the observed exoplanet dataset and the defined gas-giant classification framework, measurable host-star properties contain predictive information about gas-giant classification.

The project evaluates this conclusion through a broader scientific machine-learning framework involving:

* Model comparison
* Held-out testing
* Cross-validation
* Random-seed robustness
* Subgroup analysis
* Probability calibration
* Feature ablation
* Feature-combination analysis
* SHAP interpretation
* Permutation importance
* Direct analysis of the underlying data
* Alternative target definitions
* Feature perturbation experiments
* Feature-space coverage analysis
* Explicit scientific limitation analysis

The strongest conclusion is therefore not simply that:

> **A machine-learning model can classify exoplanets.**

It is that:

> **A reproducible analysis can investigate whether host-star properties contain predictive information about gas-giant classification, evaluate how stable that information is, examine whether multiple independent analyses support similar patterns, and explicitly characterize the limitations that constrain the scientific interpretation of those results.**

---

# License

This project is distributed under the MIT License.

See [`LICENSE`](LICENSE) for details.
