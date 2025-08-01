import streamlit as st
import pandas as pd
import pickle as pkl

model = pkl.load(open('model.pkl', 'rb'))
scaler = pkl.load(open('scaler.pkl', 'rb'))

st.header('Loan Approval Prediction App')
st.write('Choose the values for the following features to predict loan approval.')

no_of_dep = st.slider('Choose the number of dependents', 0, 5)
grad = st.selectbox('Choose the Education Level', ['Graduated', 'Not Graduated'])
self_emp = st.selectbox('Self Employed', ['Yes', 'No'])
Annual_Income = st.slider('Choose the Annual Income', 0, 100000000)
Loan_Amount = st.slider('Choose the Loan Amount', 0, 100000000)
Loan_Duration = st.slider('Choose the Loan Duration', 0, 20)
Credit_Score = st.slider('Choose the Credit Score', 0, 1000)
Assets = st.slider('Choose the Assets', 0, 100000000)

if grad == 'Graduated':
    grad_s = 1
else:
    grad_s = 0

if self_emp == 'Yes':
    self_emp_s = 1
else:
    self_emp_s = 0

if st.button('Predict'):
    pred_data = pd.DataFrame([[no_of_dep, grad_s, self_emp_s, Annual_Income, Loan_Amount, Loan_Duration, Credit_Score, Assets]],
                          columns = ['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'credit_score','Assets'])
    pred_data = scaler.transform(pred_data)
    prediction = model.predict(pred_data)
    if prediction[0] == 1:
        st.success('The loan is likely to be approved.')
    else:
        st.error('The loan is likely to be rejected.')


