# Exoplanet Classification Using Machine Learning

## Overview

This repository presents an end-to-end supervised machine learning pipeline for classifying confirmed exoplanets as **gas giants** or **non-gas giants** using stellar properties from exoplanet observations.

The project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, model development, hyperparameter optimization, model evaluation, and explainability. Particular emphasis is placed on reproducibility and model interpretability through the use of SHAP (SHapley Additive Explanations) and permutation feature importance.

This project was developed as a portfolio project to demonstrate practical machine learning skills applied to an astrophysical dataset.

---

## Objectives

The primary objectives of this project are to:

* Build a reproducible machine learning pipeline for exoplanet classification.
* Compare baseline and ensemble classification models.
* Evaluate predictive performance using standard classification metrics.
* Interpret model behavior using multiple feature importance techniques.
* Demonstrate an end-to-end data science workflow suitable for scientific applications.

---

## Dataset

The dataset consists of confirmed exoplanets and their host star properties.

### Features Used

| Feature   | Description                   |
| --------- | ----------------------------- |
| `st_teff` | Stellar effective temperature |
| `st_rad`  | Stellar radius                |
| `st_met`  | Stellar metallicity           |

### Target Variable

| Variable       | Description                                                                 |
| -------------- | --------------------------------------------------------------------------- |
| `is_gas_giant` | Binary classification target indicating whether an exoplanet is a gas giant |

### Data Preparation

The preprocessing pipeline includes:

* Duplicate record removal
* Missing value analysis
* Feature selection
* Train/test split
* Preparation of datasets for model training

Final dataset size:

* **4,747 unique exoplanets**

---

## Methodology

### Data Preprocessing

The raw dataset was cleaned through:

* Removal of duplicate observations
* Analysis of missing values
* Selection of informative predictor variables
* Preparation of training and testing datasets

---

### Models Evaluated

The following supervised learning algorithms were implemented:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

The Random Forest model was selected as the final model after comparative evaluation.

Hyperparameter optimization was performed using GridSearchCV.

---

## Model Evaluation

Performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The Random Forest classifier achieved the strongest overall predictive performance, with an accuracy of approximately **83%** on the held-out test set.

---

## Model Interpretability

To improve scientific transparency, three complementary feature importance techniques were applied.

### Random Forest Feature Importance

Measures feature importance based on impurity reduction during tree construction.

### Permutation Importance

Evaluates the reduction in predictive performance after randomly shuffling each feature.

### SHAP (SHapley Additive Explanations)

Provides local and global explanations by estimating each feature's contribution to model predictions using cooperative game theory.

---

## Results

Across all interpretability methods, **stellar radius (`st_rad`)** consistently emerged as the most influential predictor.

General observations include:

* Stellar radius contributes most strongly to model predictions.
* Stellar metallicity provides moderate predictive value.
* Stellar effective temperature contributes less strongly but remains informative.
* Agreement between Random Forest importance, permutation importance, and SHAP indicates stable model behavior.

---

## Repository Structure

```text
exoplanet-classification-ml/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   ├── decision_tree.joblib
│   ├── logistic_regression.joblib
│   └── random_forest.joblib
│
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation_and_explainability.ipynb
│
├── images/
├── outputs/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/aksharabharath/exoplanet-classification-ml.git
```

Move into the project directory:

```bash
cd exoplanet-classification-ml
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute the notebooks in numerical order:

1. `01_data_preprocessing.ipynb`
2. `02_feature_engineering.ipynb`
3. `03_model_training.ipynb`
4. `04_model_evaluation_and_explainability.ipynb`

Each notebook builds upon the outputs generated in the previous stage.

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* SHAP
* Joblib
* Jupyter Notebook

---

## Future Improvements

Potential extensions include:

* Addressing class imbalance through resampling techniques such as SMOTE.
* Evaluating gradient boosting algorithms (XGBoost, LightGBM, CatBoost).
* Incorporating additional orbital and stellar parameters.
* Extending the problem to multi-class planetary classification.
* Deploying the trained model as an interactive web application.

---

## License

This project is distributed under the MIT License.

See the `LICENSE` file for details.
