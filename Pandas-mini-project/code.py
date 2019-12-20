# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)





# code ends here


# --------------
# code starts here
# print(bank.info())

banks = bank.drop('Loan_ID', axis=1)
# print(bank.head())

bank_null_count = banks.isnull().sum()
# print(bank_null_count)

bank_mode = banks.mode()
# print(bank_mode)

for col in banks.columns:
    if bank_null_count[col]>0:
        banks[col].fillna(bank_mode.loc[0, col], inplace = True)


# print(bank.isnull().sum())
# print(bank.head(13))

#code ends here


# --------------
# Code starts here





avg_loan_amount = banks.pivot_table(index = ['Gender', 'Married', 'Self_Employed'], values = 'LoanAmount', aggfunc = 'mean')

print(avg_loan_amount)


# code ends here



# --------------
# code starts here

print(banks.head())
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

Loan_Status_Y_count = len(banks)

percentage_se = (len(loan_approved_se)/Loan_Status_Y_count)*100
percentage_nse = (len(loan_approved_nse)/Loan_Status_Y_count)*100

print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here
# print(banks.head())

loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12.0)
big_loan_term = len(loan_term[loan_term>=25])

print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()

print(mean_values)

# code ends here


