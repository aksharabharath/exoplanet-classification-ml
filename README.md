# Exoplanet Classification Using Machine Learning

## Project Overview

This project develops a machine learning pipeline to classify exoplanets based on stellar and planetary characteristics. The workflow includes data preprocessing, feature engineering, model training, evaluation, and interpretability analysis using permutation importance and SHAP (SHapley Additive Explanations).

The objective is to predict whether an exoplanet is a gas giant using astrophysical parameters derived from confirmed exoplanet observations.

---

## Problem Statement

Given a dataset of confirmed exoplanets and associated stellar properties, the goal is to build a classification model that accurately distinguishes gas giant planets from non-gas giants using supervised machine learning techniques.

---

## Dataset Description

The dataset consists of astrophysical parameters describing exoplanets and their host stars. Key variables include:

- `st_teff`: Stellar effective temperature  
- `st_rad`: Stellar radius  
- `st_met`: Stellar metallicity  
- `pl_rade`: Planetary radius  
- Target variable: `is_gas_giant`

### Data Preprocessing Summary

- Removal of duplicate planet records
- Handling of missing values in stellar parameters
- Final dataset contains 4,747 unique exoplanet records

---

## Methodology

### Data Preprocessing and Feature Engineering

- Deduplication of records to ensure data integrity
- Missing value analysis and treatment
- Feature selection based on astrophysical relevance and statistical completeness

### Models Implemented

- Logistic Regression (baseline model)
- Random Forest Classifier (final model)

Hyperparameters for the Random Forest model were optimized using grid search cross-validation.

---

## Model Evaluation

The Random Forest model achieved the strongest performance among all tested models.

### Performance Summary

- Accuracy: approximately 83%
- Strong performance on majority class (non–gas giants)
- Reduced performance on minority class due to class imbalance

Evaluation metrics included precision, recall, F1-score, and confusion matrix analysis.

---

## Model Interpretability

To ensure scientific interpretability and robustness, multiple feature importance techniques were applied:

### Random Forest Feature Importance
Derived directly from impurity reduction across decision trees.

### Permutation Importance
Evaluates the impact of feature shuffling on model performance.

### SHAP (SHapley Additive Explanations)
Quantifies the contribution of each feature to individual predictions based on cooperative game theory.

---

## Key Findings

- Stellar radius (`st_rad`) is the most influential predictor across all interpretability methods.
- Stellar metallicity (`st_met`) provides moderate predictive contribution.
- Stellar effective temperature (`st_teff`) has lower but consistent influence.
- Feature importance rankings are broadly consistent across Random Forest, permutation, and SHAP analyses, indicating model stability.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- Joblib

---

## Project Structure
exoplanet-classification-ml/
│
├── data/
├── models/
├── notebooks/
│ ├── 01_data_preprocessing.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_model_training.ipynb
│ └── 04_model_evaluation_and_explainability.ipynb
├── src/
├── outputs/
└── README.md

## Reproducibility

To reproduce results:

```bash
git clone <repository-url>
cd exoplanet-classification-ml
pip install -r requirements.txt

## Future Work
- Address class imbalance using SMOTE or class-weighted learning
- Evaluate gradient boosting methods such as XGBoost and LightGBM
- Incorporate additional orbital and spectroscopic features
- Deploy model as a web-based inference API
- Extend analysis to multi-class planetary classification

## Conclusion

This project presents a complete machine learning pipeline for exoplanet classification, combining predictive modeling with interpretability techniques. The consistency across multiple feature importance methods supports the reliability of the model, with stellar radius emerging as the most significant predictive variable.