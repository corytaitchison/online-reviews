import pandas as pd
import numpy as np
from loadRandom import loadRandom, loadRandom2
from time import perf_counter
import statsmodels.api as sm
import matplotlib.pyplot as plt


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
        '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json', 1e5).loc[:, ('stars', 'text', 'useful', 'cool', 'funny')]
    # data = loadRandom2(
    #     r'/Users/caitchison/Google Drive/Undergrad/SCDL1991/SCDL1991 2019 Semester 2/yelp_csvs/review.csv')
    print("Time taken to load:", perf_counter() - start, "s")

    # data = data[data.useful > 4]

    # starCorr = np.corrcoef(data.stars, data.useful)
    avgWords = [len(text.split(" ")) for text in data.text]
    results = getLM(avgWords, data.useful)
    print("AVERAGE WORDS\n", results.summary())

    # # plot

    # plt.scatter(avgWords, data.useful, c=(0, 0, 0), alpha=0.5)
    # plt.title('Average Words vs Usefulness')
    # plt.xlabel('Average words per review')
    # plt.ylabel('Usefulness score')
    # plt.show()

    # log

    interactions = np.log(data.useful + data.cool + data.funny + 1)

    results = getLM(avgWords, interactions)
    print("AVERAGE WORDS vs INTERACTIONS\n", results.summary())
