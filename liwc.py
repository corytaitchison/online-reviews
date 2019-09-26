import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
###
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
###
from loadRandom import loadRandom2
from groupData import groupData
###
from scipy.stats import chi2_contingency


def testChi(row, _normalize=False):
    row = np.round(row)
    contingency = pd.crosstab(row, data['interactions'], normalize=_normalize)
    c, p, dof, _ = chi2_contingency(contingency)
    print(c, p, dof)


def doPlots(data, _seed):
    columns = data.columns[4:]

    for column in columns:
        _std = np.std(data[column])
        _mean = np.mean(data[column])
        breaks = [_mean-1.2*_std, _mean-0.9*_std, _mean-0.6*_std, _mean-0.3*_std,
                  _mean, _mean+0.3*_std, _mean+0.6*_std, _mean+0.9*_std, _mean+1.2*_std]
        print(breaks)
        _data = groupData(data, data[column], breaks, _seed)
        sns.jointplot(x=_data[column], y=(_data['interactions']), kind='kde')
        fig = plt.gcf()
        fig.savefig('plots2/%s.png' % column)
        plt.close(fig)
        print(column)


def checkReligion(data, _seed):
    _std = np.std(data['relig'])
    _mean = np.mean(data['relig'])
    breaks = [_mean-1.2*_std, _mean-0.9*_std, _mean-0.6*_std, _mean-0.3*_std,
              _mean, _mean+0.3*_std, _mean+0.6*_std, _mean+0.9*_std, _mean+1.2*_std]
    _data = groupData(data, data['relig'], breaks, _seed)
    ba = data[data['interactions'] >= 15]
    return ba.loc[:, ('relig', 'interactions', 'text')]


if __name__ == '__main__':
    _seed = 123
    _subsets = [1, 3, 5, 7, 9, 11]

    location = '/Users/caitchison/Documents/Yelp/online-reviews/LIWC/LIWC2015 Results (complete).csv'
    data = loadRandom2(location, 1e6, seed=_seed, n=3778803)

    # Calculate "interaction" score
    data['interactions'] = data.B + data.C + data.D

    # Group data to get equal amounts of each subset
    # data = groupData(data, data.interactions, [1, 15], _seed)
    data = data[data['interactions'] >= 4].dropna()
    data['interactions'] = [15 if x >= 15 else x for x in data['interactions']]

    data2 = checkReligion(data, _seed)

'''
# data['Tone'] = np.round(data['Tone'])
# data2 = data.groupby(['Tone']).median()

# plt.hexbin(data['differ'], data['interactions'],
#            gridsize=(100, 10), cmap='summer')
# axes = plt.gca()
# axes.set_ylim([0, None])
# plt.colorbar()
    
# Split interactions into quantiles (5)
data['group'] = pd.qcut(data['interactions'], q=5, labels=False)
print(pd.qcut(data['interactions'], q=5).cat.categories)
data.rename(columns={"stars_x": "stars"})

# Split into features for testing and training at 30%
# TODO: Fix to use LIWC inputs
# xTrain, xTest, yTrain, yTest = train_test_split(
#     text, np.array(data['group']), test_size=0.3, random_state=_seed)

# Train model (Multinomial Naive Bayes)
nb = MultinomialNB()
nb.fit(xTrain, yTrain)

# Test and Evaluate Model
preds = nb.predict(xTest)
print(confusion_matrix(yTest, preds))
print('\n')
print(classification_report(yTest, preds))
'''
