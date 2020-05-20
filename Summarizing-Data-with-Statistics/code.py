# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
# print(data.head())

#Code starts here 

data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()

gender_count.plot(kind='bar')
plt.show()



# --------------
#Code starts here

alignment = data.Alignment.value_counts()
print(alignment)

plt.pie(alignment, labels=list(data.Alignment.unique()))
plt.title('Character Alignment')
plt.show()


# --------------
#Code starts here

sc_df = data[['Strength','Combat']]
# print(sc_df)
sc_covariance = sc_df.cov().iloc[0,1]
# print(sc_covariance)
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()
sc_pearson = sc_covariance/(sc_strength*sc_combat)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.cov().iloc[0,1]
# print(ic_covariance)
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print(ic_pearson)


# --------------
#Code starts here

total_high = data.Total.quantile(0.99)
print(total_high)

super_best = data[data.Total > total_high]

super_best_names = list(super_best.Name)
print(super_best_names)


# --------------
#Code starts here
 
fig, (ax_1, ax_2, ax_3) = plt.subplots(3)
ax_1.boxplot(data.Intelligence,vert=False)
ax_1.set_title('Intelligence')

ax_2.boxplot(data.Speed,vert=False)
ax_2.set_title('Speed')

ax_3.boxplot(data.Power,vert=False)
ax_3.set_title('Power')


plt.show()



