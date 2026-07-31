# Data Science Internship - Week 1-2: Exploratory Data Analysis

## Overview
This folder contains two EDA projects completed during Week 1-2 of the internship: **Titanic Passenger Survival Analysis** and **Housing Price Prediction Analysis**. Both projects focus on data cleaning, exploration, and feature importance identification to prepare datasets for predictive modeling.

---

## Project 1: Titanic Dataset - Exploratory Data Analysis

### Dataset Information
- **Source:** Kaggle Titanic Dataset
- **Rows:** 891 passengers
- **Columns:** 12 features
- **Target Variable:** Survived (0 = Did not survive, 1 = Survived)

### Objectives
1. Clean and prepare the Titanic dataset for analysis
2. Explore passenger demographics and ticket information
3. Identify key factors influencing survival rates
4. Generate actionable insights for predictive modeling

### Key Findings

**Most Important Predictors of Survival:**

1. **Sex (Gender)** - Strongest predictor
   - Women: ~74% survival rate
   - Men: ~19% survival rate
   - Clear evidence of "women and children first" protocol

2. **Passenger Class (Pclass)** - Strong predictor
   - 1st Class: ~62% survival rate
   - 2nd Class: ~47% survival rate
   - 3rd Class: ~24% survival rate
   - Wealthy passengers had better access to lifeboats

3. **Fare (Ticket Price)** - Moderate predictor
   - Higher ticket prices correlate with higher survival
   - Overlaps with passenger class effect

4. **Age** - Weak predictor
   - Children had slightly higher survival odds
   - Minor impact compared to gender and class

5. **Embarked, SibSp, Parch** - Minimal impact
   - Port of embarkation showed no significant survival difference
   - Family size had weak influence on survival

### Recommendations for Modeling
- Use Sex as the primary feature for survival prediction
- Include Pclass to capture economic/social status effect
- Feature engineer Fare with Pclass to avoid multicollinearity
- Consider Age interaction with Sex (women and children first)
- Drop or carefully engineer family-related features (SibSp, Parch)

### Deliverables
- `Titanic_EDA.ipynb` - Complete analysis notebook
- Cleaned dataset (saved for modeling phase)

---

## Project 2: Housing Price Prediction - Exploratory Data Analysis

### Dataset Information
- **Source:** Kaggle Housing Price Prediction Dataset
- **Rows:** 545 house records
- **Columns:** 13 features
- **Target Variable:** Price (house price in original currency)

### Objectives
1. Clean and structure the housing dataset
2. Perform exploratory analysis to understand price drivers
3. Identify key features predicting house prices
4. Prepare cleaned dataset for modeling

### Data Quality Summary
- **Dataset Size:** 545 rows, 13 columns
- **Data Completeness:** No missing values, no duplicates
- **Data Types:** 6 numeric features, 7 categorical features (properly converted)
- **Status:** Clean and ready for modeling

### Key Findings

**Numeric Features (by correlation strength):**

1. **Area** (r = 0.54) - Strongest predictor
   - Larger house area directly correlates with higher prices
   - Primary value driver in the market

2. **Bathrooms** (r = 0.52) - Strong predictor
   - More bathrooms moderately increase price

3. **Stories** (r = 0.42) - Moderate predictor
   - Multi-story homes command higher prices

4. **Parking** (r = 0.38) - Weak-Moderate predictor
   - Parking spaces add value but have lower impact

5. **Bedrooms** (r = 0.37) - Weak predictor
   - Number of bedrooms alone is a weaker price predictor than bathrooms

**Categorical Features (by price premium):**

1. **Air Conditioning** - Largest impact (+43% premium)
2. **Main Road Access** - Significant impact (+47% premium)
3. **Guest Room** - Moderate impact (+28% premium)
4. **Hot Water Heating** - Moderate impact (+17% premium)
5. **Prefarea Location** - Moderate impact (+33% premium)
6. **Basement** - Moderate impact (+16% premium)
7. **Furnishing Status** - Clear market segmentation
   - Furnished: Premium house
   - Semi-furnished: Mid-range
   - Unfurnished: Lower price (Furnished vs Unfurnished = +37% premium)

### Key Insights & Patterns

- **Area is the dominant numeric predictor.** It shows the strongest correlation with price, indicating that square footage is the primary value driver.

- **Amenities act as price multipliers.** While individual amenities have moderate correlations, their presence collectively increases price substantially. Air conditioning and main road access provide the largest premiums (40-47%).

- **Location and facilities matter significantly.** Preferred area location and amenities can add 40-50% premium to house price.

- **Furnishing status shows clear market segmentation.** Furnished homes command approximately 37% premium over unfurnished homes.

- **Interaction effects are likely.** A large, furnished house with AC in a preferred area with main road access would command a substantial cumulative premium.

### Recommendations for Modeling
- Use area as the primary feature — It's the strongest numeric predictor
- Include all amenity features — They collectively improve price prediction
- Create interaction terms — Combine area with amenities to capture synergistic effects
- Feature engineering — Create composite features like "total_amenities"
- Monitor multicollinearity — Check correlation between bathrooms and bedrooms before modeling

### Deliverables
- `Housing_EDA.ipynb` - Complete analysis notebook with code and visualizations
- `Housing_cleaned.csv` - Cleaned dataset ready for modeling

---

## Tools & Technologies Used
- **Python:** Pandas, NumPy, Matplotlib, Seaborn
- **Jupyter Notebook:** For analysis, visualization, and documentation
- **Data Analysis:** Univariate analysis, bivariate analysis, correlation analysis

## Methodology (Both Projects)

### 1. Data Cleaning & Preparation
- Load data and examine structure
- Check for missing values and duplicates
- Identify and convert data types appropriately
- Handle missing values and outliers

### 2. Exploratory Data Analysis
- **Univariate Analysis:** Understand distribution of individual features
- **Bivariate Analysis:** Explore relationships between features and target variable
- **Correlation Analysis:** Quantify strength of relationships

### 3. Feature Importance Identification
- Calculate correlation coefficients for numeric features
- Analyze categorical feature impact on target variable
- Rank features by importance for predictive power

### 4. Insight Generation & Documentation
- Summarize key patterns and findings
- Provide actionable recommendations for modeling phase
- Document data quality and preparation steps

---

## Key Learnings

1. **Data quality is foundational** — Both projects confirmed importance of clean, complete data
2. **Feature importance varies by domain** — Different features drive outcomes in different contexts
3. **Categorical features can be powerful** — Amenities in housing and gender in Titanic showed strong predictive power
4. **Relationships matter** — Numeric features show correlation, but categorical features can create significant price/survival premiums
5. **Visualization enables insight** — Plots reveal patterns that raw numbers often obscure

---

# Week 3: Statistics & Probability Analysis

## Objective
Understand statistical concepts in data science through comprehensive analysis of two datasets: Titanic survival data and Housing price prediction data.

---

## Datasets Analyzed

### 1. Titanic Dataset
- **Records:** 891 passengers
- **Target:** Survival (binary: died/survived)
- **Key Variables:** Pclass, Sex, Age, Fare, Embarked

### 2. Housing Price Prediction Dataset
- **Records:** 545 properties
- **Target:** Price (continuous)
- **Key Variables:** Area, Bedrooms, Bathrooms, Stories, Parking

---

## Analysis Completed

### Descriptive Statistics
- Calculated mean, median, variance, standard deviation
- Identified quartiles and ranges
- Grouped analysis by categorical variables
- Created distributions and visualizations

### Probability Distributions
- Tested normality using Shapiro-Wilk test
- Titanic: Age and Fare are right-skewed, not normally distributed
- Housing: Price and Area are right-skewed, not normally distributed

### Hypothesis Testing

**Titanic (Categorical variables - Chi-Square Test):**
- Sex vs Survival: p-value = 1.20e-58 (SIGNIFICANT)
- Pclass vs Survival: p-value = 4.55e-23 (SIGNIFICANT)
- Fare vs Survival: t-test p-value = 6.12e-15 (SIGNIFICANT)

**Housing (Continuous variables - Spearman Correlation):**
- Area vs Price: correlation = 0.6, p-value = 3.13e-55 (SIGNIFICANT)
- Bathrooms vs Price: correlation = 0.48, p-value = 9.65e-33 (SIGNIFICANT)
- All tested variables significantly correlate with Price

### Correlation vs Causation

**Titanic Findings:**
- Gender was strongest causal factor (evacuation priority)
- Class was secondary factor (access and priority)
- Fare was correlated but confounded by Class—not a direct cause

**Housing Findings:**
- Area is primary cause of price (0.6 correlation)
- Bathrooms is secondary cause (0.48 correlation)
- Both independently drive housing prices

---

## Key Insights

### Titanic
1. Women had 74% survival rate vs men at 19%—gender overrode wealth
2. A 3rd-class woman (50%) had better odds than a 1st-class man (36.9%)
3. Evacuation protocol prioritized gender > class > wealth

### Housing
1. Larger properties cost significantly more (Area: 0.6 correlation)
2. More bathrooms indicate higher-value properties (0.48 correlation)
3. All features (Area, Bathrooms, Bedrooms, Stories, Parking) significantly affect price
4. Market prices based on space and amenities

---

## Methodology

- **Descriptive Stats:** `.describe()`, `.mean()`, `.median()`, `.groupby()`
- **Distributions:** Histograms, Shapiro-Wilk normality test
- **Hypothesis Testing:** Chi-Square (categorical), Spearman correlation (continuous, non-normal)
- **Visualizations:** Histograms, box plots, scatter plots, heatmaps
- **Statistical Significance:** p-value threshold = 0.05

---

## Deliverables

-  Jupyter Notebook: Statistical analysis with code and visualizations
-  Summary Reports: Markdown summaries for each section
-  Correlation Heatmaps: Variable relationships visualized
-  Hypothesis Test Results: p-values and conclusions documented

---

## LinkedIn Post Requirement

Post published with tag @AnalystLab Africa featuring statistical insight from analysis.

**Sample insight:** "On the Titanic, gender was a stronger predictor of survival than wealth. A 3rd-class woman had better odds than a 1st-class man. Sometimes, protocol matters more than resources. 



## Conclusion

Week 3 provided hands-on experience with statistical hypothesis testing, probability distributions, and causal inference. Both datasets demonstrated that real-world data is rarely normally distributed, requiring appropriate non-parametric tests. Statistical significance was proven for key relationships in both domains.


# Model Evaluation Report - Week 4 Supervised Learning

## Executive Summary
This report evaluates two supervised learning models: Logistic Regression for passenger survival prediction (Titanic) and Linear Regression for house price prediction (House Prices). Both models were trained and tested on preprocessed datasets with 80/20 train/test splits.

---

## 1. Titanic Dataset - Logistic Regression Model

### Dataset Overview
- **Samples:** 891 passengers
- **Target:** Survived (1 = Survived, 0 = Did not survive)
- **Features:** Pclass, Sex, Age, SibSp, Parch, Fare, Embarked

### Steps Taken
1. Loaded Titanic dataset
2. Data cleaning: Handled missing values (Age: median imputation, Embarked: mode imputation, Cabin: dropped)
3. Feature engineering: Created Age_Bin for analysis
4. Encoded categorical variables: Sex, Pclass, Embarked (LabelEncoder)
5. Selected features and target
6. Train/test split: 80/20 (test_size=0.2, random_state=42)
7. Trained Logistic Regression model
8. Made predictions on test data
9. Evaluated with Accuracy Score and Classification Report

### Model Performance

**Accuracy: 0.81 (81%)**

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0 (Did not survive) | 0.83 | 0.86 | 0.84 | 105 |
| 1 (Survived) | 0.79 | 0.74 | 0.76 | 74 |
| **Overall** | | | **0.81** | **179** |
| Macro Avg | 0.81 | 0.80 | 0.80 | 179 |
| Weighted Avg | 0.81 | 0.81 | 0.81 | 179 |

### Performance Interpretation
- **Accuracy 81%:** Model correctly predicts survival 81% of the time.
- **Precision (79-83%):** When model predicts a class, it's correct 79-83% of the time.
- **Recall (74-86%):** Model catches 74-86% of actual survivors and non-survivors.
- **F1-Score (0.76-0.84):** Good balance between precision and recall.

### Challenges Encountered
- Class imbalance: More non-survivors (105) than survivors (74) in test set
- Survivor recall lower (74%) than non-survivor recall (86%) due to class imbalance
- Some survivors missed by model predictions

### Key Insights
1. Gender was the strongest predictor of survival (from Week 1–3 EDA)
2. Model performs well on both classes despite imbalance
3. Strong precision indicates low false positives (reliable predictions)
4. Logistic Regression is effective for binary classification on Titanic data

---

## 2. House Prices Dataset - Linear Regression Model

### Dataset Overview
- **Samples:** Property listings with price data
- **Target:** Price (house price)
- **Features:** Area, Bedrooms, Bathrooms, Stories, Mainroad, Guestroom, Basement, Hotwaterheating, Airconditioning, Parking, Prefarea, Furnishingstatus

### Steps Taken
1. Loaded House Prices dataset
2. Data cleaning: Checked for missing values (none found)
3. Encoded categorical variables using LabelEncoder: Mainroad, Guestroom, Basement, Hotwaterheating, Airconditioning, Parking, Prefarea, Furnishingstatus
4. Selected features and target (Price)
5. Train/test split: 80/20 (test_size=0.2, random_state=42)
6. Trained Linear Regression model
7. Made predictions on test data
8. Evaluated with RMSE

### Model Performance

**RMSE: 1,331,071**

### Performance Interpretation
- **RMSE 1,331,071:** Model predictions deviate by approximately 1.33 million on average from actual prices.
- **Error Margin:** Given house prices range from 11–13 million, the error represents ~10% average deviation, which is reasonable.
- **Meaning:** For any predicted price, expect actual house price to differ by ~1.33 million on average.

### Challenges Encountered
- House price data may contain outliers that increase RMSE
- Some features may have weak predictive power
- Price variations influenced by market factors beyond available features

### Key Insights
1. Model captures general price trends reasonably well
2. Area, bedrooms, bathrooms, and parking are likely strong price predictors (from Week 1–3 analysis)
3. Acceptable RMSE indicates the model can be used for price estimation
4. Linear Regression is appropriate for continuous target (price) prediction

---

## 3. Comparative Analysis

| Aspect | Titanic (Classification) | House Prices (Regression) |
|--------|--------------------------|--------------------------|
| **Model Type** | Logistic Regression | Linear Regression |
| **Task Type** | Binary Classification | Continuous Prediction |
| **Metric** | Accuracy (81%) | RMSE (1.33M) |
| **Performance** | Good (81% correct predictions) | Acceptable (~10% error margin) |
| **Imbalance** | Class imbalance (2:1 ratio) | No significant imbalance |
| **Model Complexity** | Lower (binary outcome) | Higher (continuous values) |

---

## 4. Conclusions

### Titanic Model
- Logistic Regression successfully predicts survival with 81% accuracy
- Model is reliable for both survivor and non-survivor prediction
- Gender and class remain strongest predictors of survival

### House Prices Model
- Linear Regression captures price patterns with ~10% error margin
- Model is suitable for price estimation in real-world applications
- Feature engineering and additional data could further improve accuracy

### Overall Assessment
Both models demonstrate effective supervised learning:
- **Classification (Titanic):** Binary prediction with strong performance
- **Regression (House Prices):** Continuous prediction with acceptable error

---

## 5. Recommendations for Future Work

1. **Titanic:** Address class imbalance through oversampling/undersampling for higher survivor recall
2. **House Prices:** Test other regression models (Ridge, Lasso, Random Forest) to compare RMSE
3. Both: Cross-validation for more robust performance estimates
4. Both: Feature importance analysis to identify most impactful predictors

---

# Week 5: Advanced Machine Learning - Model Comparison & Hyperparameter Tuning

## Overview

This project implements and compares advanced machine learning algorithms on two datasets: House Price Prediction (Regression) and Titanic Survival Classification. The primary objective is to build multiple models, evaluate their performance using appropriate metrics, optimize them through hyperparameter tuning, and identify the best-performing model for each dataset.

The project emphasizes understanding why certain models perform better than others, rather than simply achieving the highest accuracy.

---

## Datasets

### 1. House Price Prediction (Regression Task)

- **Objective**: Predict continuous house prices
- **Target Variable**: Price
- **Features**: Area, number of bedrooms, bathrooms, parking spaces, air conditioning, furnishing status, proximity to main road, proximity to preferred area, basement
- **Number of Samples**: 545 houses
- **Problem Type**: Regression
- **Evaluation Metrics**: MAE, MSE, RMSE, R² Score

### 2. Titanic Survival Classification

- **Objective**: Predict whether a passenger survived the Titanic disaster
- **Target Variable**: Survived (0 = Did not survive, 1 = Survived)
- **Features**: Age, Sex, Passenger Class (Pclass), Fare, Embarked port, Number of siblings/spouses (SibSp), Number of parents/children (Parch)
- **Number of Samples**: 891 passengers
- **Problem Type**: Binary Classification
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC

---

## Models Implemented

### House Price Prediction (Regression)

1. **Baseline Model: Linear Regression**
   - R² Score: 0.64
   - MAE: 979,679.69
   - MSE: 1,771,511,165,594.03
   - RMSE: 1,331,071.41

2. **Decision Tree Regressor**
   - R² Score: 0.44
   - MAE: 1,220,440.36
   - MSE: 2,825,423,389,908.25
   - RMSE: 1,680,899.57

3. **Random Forest Regressor**
   - R² Score: 0.61
   - MAE: 1,021,617.49
   - MSE: 1,945,127,147,994.66
   - RMSE: 1,394,678.15

4. **Gradient Boosting Regressor** (BEST)
   - R² Score: 0.66
   - MAE: 964,903.56
   - MSE: 1,699,782,928,866.53
   - RMSE: 1,303,757.23

5. **Tuned Random Forest Regressor**
   - R² Score: 0.59
   - MAE: 1,044,821.29
   - MSE: 2,059,393,077,878.17
   - RMSE: 1,435,058.56

### Titanic Survival Classification

1. **Baseline Model: Logistic Regression**
   - Accuracy: 0.8100
   - Precision: 0.7215
   - Recall: 0.7702
   - F1-Score: 0.7638
   - ROC-AUC: 0.8001

2. **Decision Tree Classifier**
   - Accuracy: 0.7821
   - Precision: 0.7215
   - Recall: 0.7703
   - F1-Score: 0.7450
   - ROC-AUC: 0.7803

3. **Random Forest Classifier**
   - Accuracy: 0.8044
   - Precision: 0.7671
   - Recall: 0.7567
   - F1-Score: 0.7619
   - ROC-AUC: 0.7942

4. **Gradient Boosting Classifier**
   - Accuracy: 0.8100
   - Precision: 0.8125
   - Recall: 0.7027
   - F1-Score: 0.7536
   - ROC-AUC: 0.7940

5. **Tuned Random Forest Classifier** (BEST)
   - Accuracy: 0.8156
   - Precision: 0.8360
   - Recall: 0.6891
   - F1-Score: 0.7555
   - ROC-AUC: 0.7969

---

## Hyperparameter Tuning

GridSearchCV was employed to systematically test different parameter combinations and identify optimal settings for model performance.

### Parameters Tested

- n_estimators: [50, 100, 200]
- max_depth: [5, 10, 15, 20]
- min_samples_split: [2, 5, 10]

Total combinations tested: 36 per model

### Best Parameters Found

**House Prices - Random Forest Regressor:**
- n_estimators: 50
- max_depth: 15
- min_samples_split: 10
- Result: R² = 0.59 (tuning did not improve over untuned Gradient Boosting)

**Titanic - Random Forest Classifier:**
- n_estimators: 100
- max_depth: 5
- min_samples_split: 2
- Result: Accuracy = 0.8156, ROC-AUC = 0.7969 (improved over baseline Random Forest)

---

## Evaluation Metrics

### For Regression Problems (House Prices)

- **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual values. Lower is better.
- **Mean Squared Error (MSE)**: Average squared difference between predicted and actual values. Lower is better.
- **Root Mean Squared Error (RMSE)**: Square root of MSE, in same units as target variable. Lower is better.
- **R² Score**: Proportion of variance explained by the model. Ranges from 0 to 1. Higher is better.

### For Classification Problems (Titanic)

- **Accuracy**: Percentage of correct predictions out of all predictions. (TP + TN) / Total
- **Precision**: Percentage of positive predictions that are correct. TP / (TP + FP)
- **Recall**: Percentage of actual positives correctly identified. TP / (TP + FN)
- **F1-Score**: Harmonic mean of Precision and Recall. Balances both metrics.
- **ROC-AUC**: Area under Receiver Operating Characteristic curve. Measures discrimination ability across thresholds. Ranges from 0 to 1.

---

## Key Findings

### House Price Prediction

1. Gradient Boosting Regressor achieved the best performance (R² = 0.66)
2. Property area is the dominant price predictor, accounting for 45% of feature importance
3. Number of bathrooms (18%) and air conditioning availability (9%) are secondary factors
4. Sequential tree-building in Gradient Boosting captures complex price patterns better than single Decision Trees or simple ensemble methods
5. Hyperparameter tuning of Random Forest did not improve upon untuned Gradient Boosting, suggesting the dataset dynamics favor boosting algorithms

### Titanic Survival Classification

1. Tuned Random Forest Classifier achieved the best accuracy (81.56%)
2. Sex is the strongest survival predictor, accounting for 50% of feature importance
3. Ticket fare (17%) and passenger class (15%) are important secondary factors
4. Historical records of "women and children first" evacuation policy are confirmed in feature importance rankings
5. All ensemble methods achieved similar performance (AUC > 0.88), indicating robustness across different tree-based approaches
6. The tuned model shows higher precision (83.60%) but lower recall (68.91%), meaning it is conservative in predicting survivors

### Hyperparameter Tuning Impact

1. Tuning improved model precision but yielded modest gains in overall accuracy
2. For House Prices, untuned Gradient Boosting outperformed tuned Random Forest
3. For Titanic, tuning improved accuracy from 80.44% to 81.56%
4. Dataset characteristics matter more than parameter optimization; algorithm selection is primary concern

---

## Visualizations

### House Price Prediction Visualizations

1. **Top 10 Feature Importance (Gradient Boosting)**
   - Bar chart ranking features by their contribution to predictions
   - Shows area as dominant factor (0.45), followed by bathrooms (0.18) and AC (0.09)

2. **Actual vs Predicted Scatter Plot**
   - Compares predicted prices against actual prices
   - Points clustered near diagonal line indicate good predictions
   - Shows model captures general price trends with some prediction errors at high price ranges

3. **Model Performance Comparison (R² Score)**
   - Bar chart comparing R² scores across all five models
   - Gradient Boosting leads at 0.66
   - Demonstrates ranking of model effectiveness

### Titanic Classification Visualizations

1. **Top 10 Feature Importance (Tuned Random Forest)**
   - Bar chart ranking features by survival prediction importance
   - Sex dominates at 0.50, followed by Fare (0.17) and Pclass (0.15)
   - Confirms historical evacuation priorities in data

2. **Confusion Matrix (Tuned Random Forest)**
   - Heatmap showing prediction breakdown
   - True Negatives: 95 (correctly identified non-survivors)
   - True Positives: 51 (correctly identified survivors)
   - False Positives: 10 (wrongly predicted survivors)
   - False Negatives: 23 (wrongly predicted non-survivors)

3. **ROC Curves Comparison**
   - Plots True Positive Rate vs False Positive Rate for all models
   - Random Forest: AUC = 0.891 (best discrimination ability)
   - Decision Tree: AUC = 0.890
   - Tuned Random Forest: AUC = 0.890
   - Gradient Boosting: AUC = 0.881
   - All models significantly outperform random classifier (AUC = 0.5)

4. **Model Performance Comparison (Accuracy)**
   - Bar chart comparing accuracy across all five models
   - Tuned Model leads at 0.8156
   - Shows similar performance across ensemble methods

---

## Conclusions

1. **Model Selection is Critical**: Ensemble methods (Gradient Boosting and Random Forest) consistently outperform single Decision Tree models, demonstrating the value of combining multiple weak learners.

2. **Feature Importance Reveals Insights**: Understanding which features drive predictions provides valuable domain insights (e.g., "women and children first" in Titanic data, "area" in house prices).

3. **Hyperparameter Tuning Has Limits**: While tuning can improve performance, the magnitude of improvement depends on the dataset. Algorithm choice should be the primary focus before optimization.

4. **Multiple Metrics Essential**: Relying on a single metric (e.g., accuracy) can be misleading. Using multiple metrics (Precision, Recall, F1-Score, ROC-AUC) provides a complete performance picture.

5. **Dataset Characteristics Matter**: Different algorithms suit different problem structures. Boosting algorithms excel at capturing complex patterns in house prices, while Random Forest performs well on Titanic survival data.

---

## Recommendations

1. For Price Prediction: Deploy Gradient Boosting Regressor as primary model. Monitor RMSE and R² Score in production.

2. For Survival Classification: Use Tuned Random Forest Classifier for best accuracy. Consider precision-recall trade-off based on business requirements.

3. Future Improvements:
   - Experiment with XGBoost or LightGBM for potentially better performance
   - Perform feature engineering to create new predictive features
   - Test ensemble methods combining multiple model types
   - Implement cross-validation for more robust performance estimates
   - Deploy models as REST API for production use

4. Model Monitoring: Track performance metrics over time to detect data drift and model degradation.

5. Interpretability: For high-stakes decisions, prioritize models with good interpretability and feature importance analysis.

---

