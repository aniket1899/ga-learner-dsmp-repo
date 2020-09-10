# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df =pd.read_csv(path)
print(df.info())

total = len(df)

#A -  fico credit score is greater than 700
p_a = len(df[df.fico>700])/total
print(f'P(A) = P(fico>700): {p_a}')

#B -  purpose == 'debt_consolation'
df1 = df[df['purpose'] == 'debt_consolidation'] # debt_consolidation capped df
p_b = len(df1)/total
print(f'P(B) = P(purpose is debt_consolation): {p_b}')
# print(df.purpose.value_counts())

# p(B & A)
p_a_and_b = df[(df.fico>700)&(df['purpose'] == 'debt_consolidation')][['fico']].shape[0]/df.shape[0]

# p(B|A)
p_a_b = p_a_and_b/p_b
print(f'P(B|A) = {p_a_b}')

#independency check: P(B|A) == P(B)?
result = p_a_b==p_b
print(f'Independent events?: {str(result)}')

# code ends here


# --------------
# code starts here

#total rows
total = df.shape[0]

# A: paid.back.loan == Yes
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/total
print(f'P(A) = P(paid.back.loan == Yes): {prob_lp}')

# B: credit.policy == Yes
new_df = df[df['credit.policy'] == 'Yes']
prob_cs = new_df.shape[0]/total
print(f'P(B) = P(credit.policy == Yes): {prob_cs}')

# P(paid.back.loan == Yes & credit.policy == Yes)
prob_cs_and_lp = new_df[new_df['paid.back.loan'] == 'Yes'].shape[0]/total
prob_pd_cs = prob_cs_and_lp/prob_lp
print(f'P(B|A): {prob_pd_cs}') 

# Using Bayes theorem to calculate P(A|B)
bayes = prob_pd_cs * prob_lp / prob_cs
print(f'P(A|B): {bayes}') 

# code ends here


# --------------
# code starts here

# Visualize the bar plot for the feature purpose.
df.groupby('purpose')['purpose'].count().plot(kind='bar')
plt.show()

# Visualize the bar plot for the feature purpose where paid.back.loan
# df['paid.back.loan'].value_counts()
df1 = df[df['paid.back.loan'] == 'No']
df1.groupby('purpose')['purpose'].count().plot(kind='bar')
plt.show()

# code ends here



# --------------
# code starts here

# installment median
inst_median = df.installment.median()
print(f'installment median: {inst_median}')

# installment mean
inst_mean = df.installment.mean()
print(f'installment mean: {inst_mean}')

# plot the histogram for installment
print("Histogram for 'installment':")
plt.hist(df.installment)
plt.xlabel('installment')
plt.title('Distribution for installment')
plt.show()

# plot the histogram for log.annual.inc

print("Histogram for 'log.annual.inc':")
plt.hist(df['log.annual.inc'])
plt.xlabel('log annual income')
plt.title('Distribution for log annual income')
plt.show()
df.info()
# code ends here


