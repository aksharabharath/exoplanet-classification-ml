# Exoplanet Classification: Which Stars Host Giant Planets?

## Problem Statement

The goal of this project is to investigate whether stellar characteristics can help predict the presence of gas giant planets in a planetary system.

In astronomy, it is known that certain types of stars are more likely to host giant planets, particularly those with higher metallicity. This project applies machine learning to explore whether these relationships can be learned directly from observational data.

The core question is:

Can we predict whether a star hosts a gas giant planet using stellar properties alone?

---

## Dataset Source

The dataset used in this project is sourced from the NASA Exoplanet Archive, which contains confirmed exoplanet observations collected from multiple space and ground-based telescopes.

After preprocessing, the dataset includes stellar and planetary parameters for thousands of confirmed systems.

---

## Features Used

The following stellar features were selected as predictors:

- `st_teff`: Stellar effective temperature (K)
- `st_rad`: Stellar radius (solar radii)
- `st_met`: Stellar metallicity
- `st_age`: Stellar age (Gyr)

### Target Variable

A binary classification target was created based on planet radius:

- 1 → Gas Giant (planet radius > 6 Earth radii)
- 0 → Not Gas Giant

This threshold is commonly used in exoplanet classification studies.

---

## Methodology

The project follows a standard machine learning pipeline:

1. Data cleaning and preprocessing
   - Removed missing values
   - Selected relevant stellar features
   - Created binary classification target

2. Exploratory Data Analysis (EDA)
   - Class distribution analysis
   - Feature distribution comparison across classes
   - Correlation analysis

3. Model training
   - Decision Tree Classifier
   - Random Forest Classifier
   - Logistic Regression

4. Model evaluation
   - Accuracy score
   - Precision, recall, F1-score
   - Confusion matrix
   - ROC curve and AUC score

---

## Model Comparison

| Model                 | Accuracy | Strengths                          | Weaknesses                          |
|----------------------|----------|-----------------------------------|-------------------------------------|
| Decision Tree        | ~0.78    | Interpretable, simple structure   | Prone to overfitting                |
| Random Forest        | ~0.83-0.84 | Strong performance, robust        | Less interpretable                  |
| Logistic Regression  | Lower (~0.70–0.75) | Fast, simple baseline model | Cannot capture non-linear patterns  |

The Random Forest model performed best overall, particularly in handling class imbalance and capturing non-linear relationships.

---

## Key Findings

- Stellar properties contain meaningful predictive signal for identifying gas giant planets.
- Random Forest outperforms both Decision Tree and Logistic Regression.
- Stellar metallicity and stellar radius are among the most influential features.
- The relationship between stellar features and planet type is non-linear.
- Class imbalance significantly impacts model performance and must be accounted for.

---

## Feature Importance

From the Random Forest model:

- Stellar radius is the most influential feature
- Metallicity contributes strongly to classification
- Temperature and age have moderate predictive power

These findings are consistent with astrophysical theories that link metallicity to planet formation probability.

---

## Limitations

- The dataset contains missing values, reducing usable sample size.
- The binary classification simplifies a more complex astrophysical classification system.
- Observational bias may influence the dataset, since certain planets are easier to detect.
- Only a limited set of stellar features was used; additional orbital features could improve performance.
- Hyperparameter tuning was minimal.

---

## Future Improvements

- Extend classification to multiple planet types (terrestrial, super-Earth, Neptune-like, gas giant)
- Include orbital features such as period and equilibrium temperature
- Apply advanced models like XGBoost or LightGBM
- Perform hyperparameter optimization
- Investigate detection bias in exoplanet surveys

---

## Conclusion

This project demonstrates that machine learning can be used to identify patterns between stellar properties and the likelihood of hosting gas giant planets.

While the models are not perfect, they capture meaningful trends that align with known astrophysical research. In particular, ensemble methods such as Random Forest show strong performance, suggesting that the relationship between stellar features and planet formation is complex and non-linear.

Overall, this project serves as a full end-to-end example of applying data science techniques to a real scientific dataset, from raw data processing to model interpretation.