
# Life Expectancy Analysis

![Life Expectancy Trends](https://www.shutterstock.com/image-vector/man-life-cycle-concept-set-260nw-1753181330.jpg)



## Objective
The goal of this analysis is to predict life expectancy by identifying key factors such as economic status, healthcare access, and lifestyle habits. Understanding these factors can help policymakers take proactive steps to improve public health and longevity.


'''
## Dataset Description
The dataset contains features related to health, demographics, and economic conditions, including:

- **Life Expectancy (target variable)**
- **GDP per Capita**
- **Infant Mortality Rate**
- **Healthcare Expenditure**
- **Access to Clean Water**
- **Education Levels**
- **Disease Prevalence** (e.g., HIV, tuberculosis)
- **Lifestyle Factors** (e.g., smoking, alcohol consumption)

The goal is to determine the most significant predictors of life expectancy and analyze trends across different regions.
'''

'''
## Exploratory Data Analysis (EDA)
### Key Insights:
'''

'''
# Economic and Healthcare Factors
- Higher GDP per capita and healthcare spending are correlated with higher life expectancy.
- Countries with low healthcare investment have shorter life spans.
'''

'''
# Infant Mortality and Disease Prevalence
- Higher infant mortality rates are strongly linked to lower life expectancy.
- Regions with high rates of infectious diseases (HIV, tuberculosis) have significantly lower longevity.
'''

'''
# Sanitation and Clean Water
- Access to clean water and sanitation significantly increases life expectancy.
- Poor water quality contributes to higher mortality rates from preventable diseases.
'''

'''
# Education and Lifestyle
- Higher education levels correlate with longer life expectancy.
- Unhealthy habits (e.g., smoking, alcohol consumption) negatively impact lifespan.
'''

'''
## Feature Engineering
### Skewness Handling:
'''

'''
# Right-skewed features (e.g., GDP per capita, healthcare expenditure, population)
# → Log transformation was applied to reduce skewness.
'''

'''
# Left-skewed features (e.g., schooling years, sanitation access)
# → Reciprocal transformation was used to adjust distribution.
'''

'''
### Standardization & Encoding:
- **StandardScaler** applied to numerical features.
- **OneHotEncoder** used for categorical features (e.g., region).
'''

'''
## Modeling and Metrics
The following models were tested:
- **Linear Regression** (Baseline model)
- **Random Forest Regressor** (Captures non-linearity)
- **Gradient Boosting Regressor** (Optimized for performance)
'''

'''
### Evaluation Metrics:
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R² Score** (Variance explained by the model)
'''

'''
## Key Findings from Modeling
'''

'''
# Linear Regression
- Struggled with capturing complex non-linear relationships.
- Moderate R² score, indicating some predictive power but room for improvement.
'''

'''
# Random Forest Regressor
- Showed higher importance for GDP, infant mortality, and healthcare spending.
- Performed better than Linear Regression but had slight overfitting.
'''

'''
# Gradient Boosting Regressor
- Best-performing model with the highest R² score and lowest MAE.
- Handled skewed data effectively due to transformations.
'''

'''
## Best Model Selection
- **Gradient Boosting** was chosen due to better generalization, higher predictive accuracy, and effective handling of feature relationships.
'''

'''
## Conclusion
Key determinants of life expectancy include:
- **Healthcare expenditure**
- **Infant mortality rate**
- **Access to clean water and sanitation**
- **Economic status (GDP per capita)**
- **Education and lifestyle factors**

Policymakers can use these insights to invest in healthcare, sanitation, and education to improve global life expectancy.
'''

