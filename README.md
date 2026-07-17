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

---

## Conclusion

Week 3 provided hands-on experience with statistical hypothesis testing, probability distributions, and causal inference. Both datasets demonstrated that real-world data is rarely normally distributed, requiring appropriate non-parametric tests. Statistical significance was proven for key relationships in both domains.
