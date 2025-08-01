# Loan Approval Prediction App

This is a Streamlit-based web application that predicts whether a loan application is likely to be approved based on user inputs such as income, loan amount, credit score, and other relevant details.

## Live App
   Try the deployed app here:  
   [https://loan-predictor-bayarmaa.streamlit.app](https://loan-predictor-bayarmaa.streamlit.app)

## Features
- Cleaned and preprocessed dataset (feature engineering and encoding)
- Logistic Regression model trained with scaled features
- Predicts loan approval status: Approved or Rejected
- Interactive Streamlit UI
- Model and scaler saved with `pickle`

##  Dataset Columns
- `no_of_dependents`
- `education`
- `self_employed`
- `income_annum`
- `loan_amount`
- `loan_term`
- `credit_score`
- `Assets`

## 🛠 Tech Stack
- Python
- Pandas, Scikit-learn
- Streamlit
- Pickle

## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/bayrmaatt/loan-approval-app
   cd loan-approval-app
   
   pip install -r requirements.txt

   streamlit run app.py
