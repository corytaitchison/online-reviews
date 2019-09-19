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

if __name__ == '__main__':
    _seed = 123
    _subsets = [1, 2, 3, 4, 5, 15]

    location = '/Users/caitchison/Documents/Yelp/online-reviews/LIWC/LIWC2015 Results (sample2.csv).csv'
    data = loadRandom2(location, 9e4, seed=_seed, n=int(1e5-1))

    # Calculate "interaction" score
    data['interactions'] = data.useful + data.cool + data.funny
    data = data[data['interactions'] >= _subsets[0]].dropna()

    # Group data to get equal amounts of each subset
    data = groupData(data, _subsets, _seed)

    # data['Tone'] = np.round(data['Tone'])
    # data2 = data.groupby(['Tone']).median()

    # plt.hexbin(data['differ'], data['interactions'],
    #            gridsize=(100, 10), cmap='summer')
    # axes = plt.gca()
    # axes.set_ylim([0, None])
    # plt.colorbar()

    sns.jointplot(x=data['differ'], y=data['interactions'], kind='kde')
    plt.show()

'''
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
