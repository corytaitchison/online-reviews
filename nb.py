import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
###
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
###
from loadRandom import loadRandom2

ps = PorterStemmer()
# lemmatizer = WordNetLemmatizer()


def textProcess(text):
    stopWords = set(stopwords.words('english'))
    noPunc = word_tokenize(text)
    return [ps.stem(word) for word in noPunc if word not in stopWords]


if __name__ == '__main__':
    _seed = 123
    _observations = 1e4
    _subsets = [1, 2, 3, 4]

    location = '/Users/caitchison/Documents/Yelp/yelp_dataset/restaurants_only.csv'
    data = loadRandom2(location, _observations, seed=_seed, n=3778803).loc[:,
                                                                           ('text', 'useful', 'cool', 'funny', 'stars_x')]

    # Calculate "interaction" score
    data['interactions'] = data.useful + data.cool + data.funny
    data = data[data['interactions'] >= _subsets[0]].dropna()
    # TODO: Make equal sampling from each set (e.g 3000 for 0, 3000 for 1 etc)

    # Subset to get equal amounts of low-useful and high-useful
    masks = [data.interactions == x for x in _subsets]
    masks.append(data.interactions > _subsets[-1])
    subsetSize = min([sum(mask) for mask in masks])

    print("Creating subsets of size %i" % subsetSize)

    newData = pd.DataFrame([])
    for mask in masks:
        df = data[mask].sample(n=subsetSize, random_state=_seed)
        newData = newData.append(df)

    data = newData

    # Split interactions into quantiles (5)
    data['group'] = pd.qcut(data['interactions'], q=5, labels=False)
    print(pd.qcut(data['interactions'], q=5).cat.categories)
    data.rename(columns={"stars_x": "stars"})

    # Create a bag of words and convert the text to a sparse matrix
    text = np.array(data['text'])
    bow = CountVectorizer(analyzer=textProcess).fit(text)
    print("Unique (Not Stop) Words:", len(bow.vocabulary_))
    text = bow.transform(text)

    # Split into features for testing and training at 30%
    xTrain, xTest, yTrain, yTest = train_test_split(
        text, np.array(data['group']), test_size=0.3, random_state=_seed)

    # Train model (Multinomial Naive Bayes)
    nb = MultinomialNB()
    nb.fit(xTrain, yTrain)

    # Test and Evaluate Model
    preds = nb.predict(xTest)
    print(confusion_matrix(yTest, preds))
    print('\n')
    print(classification_report(yTest, preds))
