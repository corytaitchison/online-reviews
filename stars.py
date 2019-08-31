import pandas as pd
import numpy as np
from loadRandom import loadRandom, loadRandom2
from time import perf_counter
import statsmodels.api as sm


def countWords(text):
    sentences = text.split(".")
    wordCount = [len(sentence.split(" ")) for sentence in sentences]
    return np.mean(wordCount)


def getLM(x, y):
    x = sm.add_constant(np.array(x).reshape((-1, 1)))
    model = sm.OLS(y, x)
    return model.fit()


if __name__ == '__main__':
    start = perf_counter()
    data = loadRandom(
        '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json', 1e5).loc[:, ('stars', 'text', 'useful')]
    print("Time taken to load: ", perf_counter() - start, "s")

    starCorr = np.corrcoef(data.stars, data.useful)
    avgWords = [len(text.split(" ")) for text in data.text]
    results = getLM(avgWords, data.useful)
    print(results.summary())
