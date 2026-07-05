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

## Feature Selection and Justification

The final model uses four stellar features: `st_teff` (stellar effective temperature), `st_rad` (stellar radius), `st_met` (stellar metallicity), and `st_age` (stellar age).

These features were selected because they are physically meaningful and have strong connections to planet formation and classification.

- **Stellar effective temperature (`st_teff`)**: This helps describe the type of star. Different stellar temperatures are associated with different stellar classes, which can influence the likelihood of certain types of planets forming or being detectable.

- **Stellar radius (`st_rad`)**: The size of the star affects gravitational interactions and observational signals such as transit depth. Larger stars can make it harder to detect smaller planets, which indirectly affects the observed distribution of planet types.

- **Stellar metallicity (`st_met`)**: Metallicity is one of the most important factors in planet formation. Higher metallicity stars tend to have a greater abundance of heavy elements, which increases the probability of forming gas giants.

- **Stellar age (`st_age`)**: The age of a star system provides information about its evolutionary stage. Older systems may have more dynamically evolved planetary architectures.

Planetary features such as planet radius were intentionally excluded from the feature set to avoid trivial classification. Since the goal is to predict whether a planet is a gas giant, using planet radius directly would leak target-related information and make the problem unrealistic.

Instead, the model focuses on stellar properties that influence planet formation indirectly, making the prediction task more scientifically meaningful and closer to real-world discovery scenarios.

--
## Class Imbalance Handling

The dataset exhibited a moderate class imbalance, with approximately 4386 non-gas giant planets (class 0) and 1439 gas giant planets (class 1). This imbalance can bias machine learning models toward predicting the majority class more frequently, leading to misleading accuracy scores.

To address this, model evaluation was focused not only on accuracy but also on precision, recall, and F1-score, particularly for the minority class (gas giants). This ensured that model performance was assessed in a more balanced and realistic way.

In addition, experiments were conducted using class-weight adjustments in models such as Random Forest and Logistic Regression. The `class_weight="balanced"` parameter was considered to penalize misclassification of the minority class more heavily, improving sensitivity toward gas giant detection.

Although resampling techniques such as oversampling or undersampling were not applied in this version of the project, they are recognized as potential improvements for future iterations.

Overall, this approach helped mitigate bias toward the majority class while maintaining interpretability and simplicity in the modeling pipeline.

--

## Data Leakage Prevention

To ensure the model evaluation was realistic and not overly optimistic, careful steps were taken to avoid data leakage.

First, the dataset was split into training and testing sets before any preprocessing steps that could introduce information from the test set into the training process. This ensures that the model does not learn patterns from unseen data during training.

Second, only selected stellar features were used for prediction (`st_teff`, `st_rad`, `st_met`, `st_age`). Planet-specific attributes such as radius and orbital characteristics were excluded from the feature set to prevent indirect leakage of target-related information.

Finally, all transformations and model training steps were performed strictly within the training dataset, and evaluation was done exclusively on the held-out test set. This helps ensure that performance metrics reflect true generalization ability rather than memorization.

--

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

## Error Analysis

Although the models achieved reasonable overall accuracy, performance was significantly weaker on the minority class (gas giants), particularly in terms of recall.

The main source of error is the model’s tendency to misclassify gas giants as non-gas giants. This is reflected in the lower recall values for class 1 across all models, especially in Logistic Regression and Decision Tree.

This issue can be explained by several factors:

- **Class imbalance**: The dataset contains substantially more non-gas giant examples, causing the model to favor predicting class 0 more often.
- **Feature overlap**: Many stellar systems that host gas giants share similar stellar characteristics with systems that do not, making separation less distinct in feature space.
- **Indirect relationship between features and target**: The selected stellar features (such as temperature, radius, metallicity, and age) influence planet formation probabilistically rather than deterministically, which introduces ambiguity into classification.

Among all models, Random Forest reduced this issue the most, likely due to its ability to capture non-linear interactions between features. However, even this model still shows reduced sensitivity toward gas giants compared to the majority class.

Overall, the errors highlight that this is a scientifically realistic classification problem where perfect separation is not expected.

--

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

## Model Performance Summary

The following table compares the performance of different classification models used in this project:

| Model               | Accuracy | Precision (Class 1) | Recall (Class 1) | F1-score (Class 1) |
|--------------------|----------|---------------------|------------------|---------------------|
| Logistic Regression| ~0.76    | ~0.60               | ~0.26            | ~0.36               |
| Decision Tree      | ~0.79    | ~0.67               | ~0.27            | ~0.38               |
| Random Forest      | ~0.84    | ~0.76               | ~0.54            | ~0.63               |

### Key Observation
Random Forest performed the best overall, particularly in identifying gas giants (class 1), due to its ability to capture non-linear relationships between stellar features.

--

## Conclusion

This project demonstrates that machine learning can be used to identify patterns between stellar properties and the likelihood of hosting gas giant planets.

While the models are not perfect, they capture meaningful trends that align with known astrophysical research. In particular, ensemble methods such as Random Forest show strong performance, suggesting that the relationship between stellar features and planet formation is complex and non-linear.

Overall, this project serves as a full end-to-end example of applying data science techniques to a real scientific dataset, from raw data processing to model interpretation.
