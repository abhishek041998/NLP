import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset=pd.read_csv('studentperformance.csv')
dataset.columns = ['gender',
                   'race',
                   'ped',
                   'lunch',
                   'test',
                   'math',
                   'reading',
                   'writing']

dataset.info()
dataset.describe()

pd.plotting.scatter_matrix(dataset)
sns.pairplot(dataset)

sns.barplot(dataset['gender'].value_counts().index,
            dataset['gender'].value_counts(),
            hue=['female','male'])

sns.barplot(dataset['race'],
            dataset['math'],
            hue=dataset['gender'])

sns.barplot(dataset['race'],
            dataset['reading'],
            hue=dataset['gender'])

sns.barplot(dataset['race'],
            dataset['writing'],
            hue=dataset['gender'])

sns.barplot(dataset['ped'],
            dataset['math'],
            hue=dataset['gender'])

sns.barplot(dataset['ped'],
            dataset['reading'],
            hue=dataset['gender'])

sns.barplot(dataset['ped'],
            dataset['writing'],
            hue=dataset['gender'])


sns.barplot(dataset['lunch'],
            dataset['math'],
            hue=dataset['gender'])

sns.barplot(dataset['lunch'],
            dataset['reading'],
            hue=dataset['gender'])

sns.barplot(dataset['lunch'],
            dataset['writing'],
            hue=dataset['gender'])

sns.barplot(dataset['test'],
            dataset['math'],
            hue=dataset['gender'])

sns.barplot(dataset['test'],
            dataset['reading'],
            hue=dataset['gender'])

sns.barplot(dataset['test'],
            dataset['writing'],
            hue=dataset['gender'])


plt.hist(dataset['math'],bins=100)
plt.hist(dataset['reading'],bins=100)
plt.hist(dataset['writing'],bins=100)

sns.boxplot(dataset['math'],dataset['gender'])
sns.boxplot(dataset['reading'],dataset['gender'])
sns.boxplot(dataset['writing'],dataset['gender'])

sns.boxplot(dataset['math'],dataset['race'])
sns.boxplot(dataset['reading'],dataset['race'])
sns.boxplot(dataset['writing'],dataset['race'])

sns.boxplot(dataset['math'],dataset['ped'])
sns.boxplot(dataset['reading'],dataset['ped'])
sns.boxplot(dataset['writing'],dataset['pedr'])

sns.boxplot(dataset['math'],dataset['lunch'])
sns.boxplot(dataset['reading'],dataset['lunch'])
sns.boxplot(dataset['writing'],dataset['lunch'])

sns.boxplot(dataset['math'],dataset['test'])
sns.boxplot(dataset['reading'],dataset['test'])
sns.boxplot(dataset['writing'],dataset['test'])

