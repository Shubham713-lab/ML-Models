# House Price Prediction Using Machine Learning

This project focuses on predicting house prices using Machine Learning techniques. The model is trained on house price data and uses the XGBoost Regression algorithm to make accurate price predictions based on different housing features.

## Project Overview

House price prediction is a regression-based machine learning problem where the goal is to estimate the price of a house using historical data.  
In this project, data preprocessing, analysis, model training, and evaluation are performed to build an efficient prediction system.

## Dataset

The dataset contains different features related to houses that help in predicting the final price.

Dataset Link:

https://drive.google.com/file/d/16CNlwatBYLccXMqPAICFuUoVdHECkKkf/view?usp=sharing


## Technologies Used

- Python
- Machine Learning
- XGBoost Regression
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn


## Project Workflow

### 1. Data Collection

- Loaded the house price dataset
- Explored dataset structure and information

### 2. Data Preprocessing

Performed preprocessing steps to prepare the data for training:

- Handling missing values
- Checking data types
- Cleaning the dataset
- Preparing input and output features

### 3. Data Analysis

Analyzed the dataset to understand:

- Feature relationships
- Data patterns
- Correlation between variables
- Important factors affecting house prices

### 4. Train Test Split

The dataset was divided into:

- Training data
- Testing data

Training data is used to train the model, while testing data is used to evaluate model performance.


### 5. Model Training

Used XGBoost Regressor for prediction.

XGBoost is an advanced regression algorithm based on a tree structure. It builds multiple decision trees and combines their results to improve prediction accuracy.

Algorithm Used:

- XGBoost Regressor


### 6. Model Evaluation

The trained model was evaluated using performance metrics to check prediction accuracy.

Evaluation metrics:

- R Squared Error
- Mean Absolute Error


## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost
```


## Usage

Run the Python file or Jupyter Notebook:

```bash
python house_price_prediction.py
```

or open:

```bash
House_Price_Prediction.ipynb
```


## Results

The XGBoost Regression model successfully learns patterns from the housing dataset and predicts house prices with good accuracy.


## Conclusion

This project demonstrates the implementation of a complete Machine Learning workflow including data preprocessing, analysis, model building, and evaluation using XGBoost Regression.
