# Exoplanet Classification Using Stellar Properties

## Problem Statement

The discovery of exoplanets has significantly expanded our understanding of planetary systems beyond our own. However, the observed exoplanet population is heavily influenced by observational limitations and detection biases, meaning that the data does not represent a perfectly random or complete sample of planetary systems in the universe.

This project investigates whether stellar properties such as temperature, radius, metallicity, and age can be used to distinguish systems that host gas giant planets from those that do not.

Rather than treating this purely as a classification task, this work frames it as an exploration of how stellar environments relate to planet formation under real observational constraints.

---

## Scientific Objective

The primary objective of this project is to analyze the relationship between stellar characteristics and the likelihood of gas giant planet formation using machine learning methods.

This project aims to:
- Identify which stellar properties are most strongly associated with gas giant exoplanet systems
- Evaluate the predictive power of stellar features in classifying planetary systems
- Understand how observational bias and incomplete data influence model performance

---

## Research Question

Can stellar properties alone provide meaningful predictive signal for the presence of gas giant exoplanets, despite observational bias and incomplete observational data?

---

## Why This Matters

Understanding the relationship between stars and their planetary systems is fundamental to astrophysics and planetary science. However, exoplanet datasets are shaped by detection methods that preferentially identify certain types of planets, especially large gas giants.

By applying machine learning to these datasets, we can not only build predictive models but also gain insight into the structure, limitations, and biases present in astronomical observations.

---

## Dataset

The dataset is sourced from the NASA Exoplanet Archive and contains confirmed exoplanet systems along with stellar and planetary parameters.

### Key attributes include:
- Stellar properties: temperature, radius, metallicity, age, luminosity
- Planetary properties: orbital period, radius, equilibrium temperature
- System properties: distance from Earth, discovery method

---

## Feature Selection & Astrophysical Interpretation

The following stellar features were selected based on astrophysical relevance:

### Stellar Temperature (`st_teff`)
Indicates the star’s spectral type and energy output. This affects the thermal environment in which planets form and evolve.

### Stellar Radius (`st_rad`)
Relates to stellar evolution stage. Larger stars may indicate different planetary formation environments and detection biases.

### Metallicity (`st_met`)
Represents the abundance of elements heavier than hydrogen and helium. Higher metallicity is strongly linked to increased probability of gas giant planet formation.

### Stellar Age (`st_age`)
Indicates system maturity. Older systems may have more dynamically evolved planetary architectures.

These features were selected because they directly influence planet formation theory and are physically meaningful in astrophysical models.

---

## Data Preprocessing

- Removed or handled missing values across key features
- Filtered irrelevant or extremely sparse attributes
- Standardized feature selection for modeling consistency
- Defined binary target variable:
  - 1 → Gas giant system
  - 0 → Non-gas giant system

---

## Data Leakage Prevention and Experimental Rigor

One of the most important considerations in building a reliable machine learning model is ensuring that no information from the test set is used during training. This project was designed to strictly avoid data leakage at every stage of the pipeline.

### Train-Test Split Strategy

The dataset was split into training and testing sets **before any scaling or model training was performed**. This ensures that statistical properties of the test set do not influence the training process.

All preprocessing steps such as scaling and missing value handling were applied using parameters derived only from the training set.

### Scaling and Preprocessing Safety

Feature scaling (where applicable) was fit only on the training data and then applied to the test set using the same transformation. This prevents any leakage of distributional information from the test set into the training process.

### Model Training Integrity

All models were trained exclusively on the training dataset, and performance evaluation was conducted only on the held-out test set. No test data was used during feature selection, tuning, or preprocessing decisions.

### Random State Consistency

To ensure reproducibility, a fixed random state was used across:
- train-test splitting
- model initialization (Logistic Regression, Decision Tree, Random Forest)

This ensures that results are stable and can be replicated exactly under the same environment.

### Summary

These steps ensure that all reported results reflect true generalization performance rather than artificially inflated accuracy due to data leakage or inconsistent experimental setup.

--

## Machine Learning Pipeline Overview

The project follows a structured end-to-end machine learning pipeline:

1. Data Loading (NASA Exoplanet Archive)
2. Initial Exploration and Cleaning
3. Feature Selection (stellar parameters)
4. Train-Test Split (before preprocessing)
5. Feature Scaling (fit on training set only)
6. Model Training (Logistic Regression, Decision Tree, Random Forest)
7. Model Evaluation (test set only)
8. Performance Comparison and Interpretation

--

## Class Imbalance & Dataset Bias

### Class Imbalance
The dataset contains an uneven distribution between classes:
- Class 0 (non-gas giant systems): majority
- Class 1 (gas giant systems): minority

To address this:
- Class weighting was applied in models
- Model performance was evaluated using recall and F1-score, not just accuracy

### Observational Bias
Exoplanet datasets are not randomly sampled:
- Large planets are easier to detect (especially via radial velocity and transit methods)
- Smaller planets are underrepresented
- Detection method influences what is observed

This means the dataset reflects observational constraints rather than true planetary distributions.

---

## Models Used

Three machine learning models were trained and evaluated:

- Logistic Regression (baseline linear model)
- Decision Tree Classifier (non-linear interpretability)
- Random Forest Classifier (ensemble model)

---

## Model Evaluation

Performance was evaluated using accuracy, precision, recall, and F1-score.

### Summary Table

| Model               | Accuracy | Precision (Class 1) | Recall (Class 1) | F1-score (Class 1) |
|---------------------|----------|---------------------|------------------|--------------------|
| Logistic Regression | TBD      | TBD                 | TBD              | TBD                |
| Decision Tree       | ~0.78    | ~0.67               | ~0.27            | ~0.38              |
| Random Forest       | ~0.84    | ~0.76               | ~0.54            | ~0.63              |

Random Forest performed best overall, particularly in identifying gas giant systems.

---

## Error Analysis

Model performance shows stronger prediction for non-gas giant systems compared to gas giants.

### Observed failure cases:
- Misclassification of gas giant systems with incomplete stellar data
- Confusion in borderline systems with intermediate planetary sizes
- Reduced performance on systems with missing or noisy stellar parameters

### Interpretation:
Gas giant classification is more difficult due to:
- overlapping feature distributions
- observational bias in detection methods
- incomplete measurement of stellar environments

---

## Key Findings

- Metallicity is one of the strongest predictors of gas giant presence
- Stellar radius and temperature also contribute significantly to model performance
- Class imbalance heavily affects recall for gas giant classification
- Random Forest provides the best balance between interpretability and performance

---

## Limitations

- Dataset is affected by strong observational bias
- Many missing values in stellar parameters
- Class imbalance reduces model sensitivity to minority class
- Models do not incorporate temporal or orbital dynamics
- Only tabular data is used (no light curve or time-series signals)

---

## Reproducibility

To reproduce this project:

1. Install dependencies:

2. Run notebooks in order:
- 01_data_understanding.ipynb
- 02_data_cleaning.ipynb
- 03_exploratory_data_analysis.ipynb
- 04_model_training.ipynb
- 05_model_evaluation.ipynb

3. Ensure:
- random_state is fixed in all models
- dataset path is correctly set

---

## Conclusion

This project demonstrates how machine learning can be applied to astrophysical datasets not only for prediction, but also for interpreting underlying scientific patterns and observational limitations.

Rather than treating exoplanet classification as a purely computational task, this work highlights the role of data bias, measurement limitations, and stellar physics in shaping model outcomes.

---

## Future Work

- Incorporate time-series data from TESS or Kepler
- Improve handling of missing astrophysical parameters
- Expand classification to include Earth-like planets
- Study detection method bias explicitly as a separate model feature
