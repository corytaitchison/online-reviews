from readability_score.calculators.fleschkincaid import FleschKincaid
# Download from https://github.com/wimmuskee/readability-score
import pandas as pd
import numpy as np
from loadRandom import loadRandom
from models import getLM, getNBM
import matplotlib.pyplot as plt
import numpy_indexed as npi

if __name__ == '__main__':
    seed = 2
    data = loadRandom(
        '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json', 1e5, seed).loc[
            :, ('stars', 'text', 'useful', 'cool', 'funny')]

    # Get metric and mask
    interactions = np.array(data.useful + data.cool + data.funny)
    mask = interactions >= np.median(interactions)
    interactions = interactions[mask]

    # Get readability score using FleischKincaid
    reviews = np.array(data.text)[mask]
    minAge = np.array([FleschKincaid(text).min_age for text in reviews])
    mask = minAge > 0
    minAge = minAge[mask]
    interactions = interactions[mask]

    x = np.log10(minAge)
    x_unique, y_mean = npi.group_by(x).median(interactions)

    # Get results
    results = getLM(x_unique[x_unique < 1.3][1:],
                    y_mean[x_unique < 1.3][1:])

    """
    plt.hist(rsq, density=False, bins=15, rwidth=0.95)
    plt.title('Correlations of Readability to Interactions (N=1e5, n=1e2)')
    plt.xlabel('Pearson Correlation Coefficient')
    plt.ylabel('Count')
    plt.show()

    """
    print("READABILITY (Means)\n", results.summary())

    # Get graph
    plt.subplot(2, 1, 1)
    plt.scatter(x, np.log10(interactions), alpha=0.5)
    plt.title('Readability Score vs Interactions')
    plt.ylabel('Interactions Count (log10)')

    # Get average y-value per x-value
    plt.subplot(2, 1, 2)
    plt.scatter(x_unique, y_mean, alpha=0.5)
    plt.xlabel('Log(10) Minimum Reading Age (FK)')
    plt.ylabel('Interactions Count (means)')

    plt.show()
