import pandas as pd
import numpy as np
from time import perf_counter
import statsmodels.api as sm
from textblob import TextBlob
# import matplotlib.pyplot as plt
# --- #
from loadRandom import loadRandom
from stars import getLM

if __name__ == '__main__':
    start = perf_counter()
    data = loadRandom(
        '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json', 1e5).loc[:, ('stars', 'text', 'useful', 'cool', 'funny')]
    print("Time taken to load:", perf_counter() - start, "s")

    # Get metric and mask
    interactions = np.array(data.useful + data.cool + data.funny)
    mask = interactions > 0
    interactions = interactions[mask]

    # Load TextBlob
    dtb = np.array([TextBlob(text) for text in data.text])[mask]

    # Calculate sentiment
    sent = np.abs(np.array([x.sentiment[0] for x in dtb]))

    # Calculate subjectivity
    subj = np.array([1 - x.subjectivity for x in dtb])

    # Calculate correlation
    results = getLM(sent, np.log(interactions))
    print("SENT\n", results.summary())

    # Combined objectivity
    results = getLM(subj + sent, np.log(interactions))
    print("COMBINED\n", results.summary())
