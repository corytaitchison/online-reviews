import pandas as pd
import numpy as np
from loadRandom import loadRandom


def countWords(text):
    sentences = text.split(".")
    wordCount = [len(sentence.split(" ")) for sentence in sentences]
    return np.mean(wordCount)


if __name__ == '__main__':
    data = loadRandom(
        '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json').loc[:, ('stars', 'text', 'useful')]
    starCorr = np.corrcoef(data.stars, data.useful)
    avgWords = [countWords(text) for text in data.text]
    avgWordsCorr = np.corrcoef(avgWords, data.useful)
