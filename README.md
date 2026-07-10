Titanic Dataset - Exploratory Data Analysis

Project Overview

Analysis of the Titanic passenger dataset to identify factors that influenced survival rates during the sinking of the RMS Titanic in 1912.

Dataset Information


Source: Kaggle Titanic Dataset
Rows: 891 passengers
Columns: 12 features
Target Variable: Survived (0 = Did not survive, 1 = Survived)


Objectives


Clean and prepare the Titanic dataset for analysis
Explore passenger demographics and ticket information
Identify key factors influencing survival rates
Generate actionable insights for predictive modeling


Methodology

Data Cleaning


Handled missing values in Age, Cabin, and Embarked
Removed duplicate records
Converted categorical columns (Sex, Embarked, Pclass) to appropriate data types


Exploratory Data Analysis (EDA)


Univariate Analysis: Distribution of individual features (histograms, bar plots, box plots)
Bivariate Analysis: Relationships between features and survival (scatter plots, box plots)
Correlation Analysis: Strength of relationships between numeric features and survival


Key Findings

Most Important Predictors of Survival

1. Sex (Gender) - Strongest predictor


Women: ~74% survival rate
Men: ~19% survival rate
Clear evidence of "women and children first" protocol


2. Passenger Class (Pclass) - Strong predictor


1st Class: ~62% survival rate
2nd Class: ~47% survival rate
3rd Class: ~24% survival rate
Wealthy passengers had better access to lifeboats


3. Fare (Ticket Price) - Moderate predictor


Higher ticket prices correlated with higher survival
Overlaps with passenger class effect


4. Age - Weak predictor


Children had slightly higher survival odds
Minor impact compared to gender and class


5. Embarked, SibSp, Parch - Minimal impact


Port of embarkation showed no significant survival difference
Family size had weak influence on survival


Recommendations for Modeling


Use Sex as the primary feature for survival prediction
Include Pclass to capture economic/social status effect
Feature engineer Fare with Pclass to avoid multicollinearity
Consider Age interaction with Sex (women and children first)
Drop or carefully engineer family-related features (SibSp, Parch)


Tools Used


Python: Pandas, NumPy, Matplotlib, Seaborn
Jupyter Notebook: For analysis and visualization


Deliverables


Titanic_EDA.ipynb - Complete analysis notebook
Cleaned dataset (saved for modeling phase)
Feature importance rankings
Insight summary with recommendations
