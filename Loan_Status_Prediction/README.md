# Loan Status Prediction

## Project Overview

The Loan Status Prediction project uses Machine Learning to predict whether a loan application should be **Approved** or **Rejected** based on the applicant's information. The model is trained using historical loan data and can assist financial institutions in making faster and more consistent loan approval decisions.

---

## Workflow

### 1. Data Collection
- Load the loan dataset containing applicant details.
- Example features:
  - Gender
  - Marital Status
  - Education
  - Self Employed
  - Applicant Income
  - Coapplicant Income
  - Loan Amount
  - Loan Amount Term
  - Credit History
  - Property Area
  - Loan Status (Target)

---

### 2. Data Preprocessing
The dataset is cleaned and prepared before training.

Steps include:
- Handling missing values
- Encoding categorical variables
- Feature selection
- Data normalization (if required)

---

### 3. Train-Test Split
The processed dataset is divided into:
- **Training Data (80%)**
- **Testing Data (20%)**

This helps evaluate the model on unseen data.

---

### 4. Model Training
The project uses the **Support Vector Machine (SVM)** algorithm, a supervised machine learning technique.

- Algorithm: Support Vector Machine (SVM)
- Learning Type: Supervised Learning
- Library: Scikit-learn

The model learns patterns from historical loan data.

---

### 5. Model Evaluation
The trained model is evaluated using:
- Accuracy Score
- Confusion Matrix (optional)
- Classification Report (optional)

---

### 6. Prediction

New applicant data is provided to the trained model.

**Input → Trained Model → Prediction**

```
New Applicant Data
        │
        ▼
 Trained SVM Model
        │
        ▼
 Loan Status Prediction
        │
 ┌───────────────┐
 │ Approved      │
 │ or            │
 │ Rejected      │
 └───────────────┘
```

---

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib (optional)
- Jupyter Notebook

---

## Project Structure

```
Loan-Status-Prediction/
│
├── loan_status_prediction.ipynb
├── train.csv
├── model.pkl
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Loan-Status-Prediction.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

Run:

```
loan_status_prediction.ipynb
```

---

## Sample Prediction

Input:

- Gender: Male
- Married: Yes
- Education: Graduate
- Applicant Income: 5000
- Loan Amount: 150
- Credit History: 1

Output:

```
Loan Approved
```

or

```
Loan Rejected
```

---

## Future Improvements

- Hyperparameter tuning
- Compare multiple ML algorithms
- Deploy using Flask or Streamlit
- Create a web-based user interface
- Improve prediction accuracy using feature engineering

---

## Conclusion

This project demonstrates the complete machine learning pipeline for loan approval prediction, including data preprocessing, model training using Support Vector Machine (SVM), evaluation, and prediction on new applicant data. It provides a practical example of applying supervised learning to solve real-world financial decision-making problems.