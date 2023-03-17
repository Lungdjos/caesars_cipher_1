import pandas as pd

# Load data from CSV
data_set = pd.read_csv('water_portability.csv')

# Split features and labels
X = data_set.drop('Potability', axis=1)
y = data_set['Potability']