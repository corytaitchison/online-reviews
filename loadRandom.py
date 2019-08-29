import numpy as np
import random
from loadData import loadJSON
import pandas as pd
import sys


def loadRandom(location, k=10, targetNum=1e5, seed=12345):
    # Location = location of file to load in, k = number of partitions,
    # targetNum is the number of observations wanted after random sampling
    random.seed(seed)
    # Relative number of observations per chunk
    weights = np.array(random.sample(range(1, 1000), k))
    chunkSize = int(6e6/k)  # TODO: Replace with actual size of the data
    # Array of number of observations per chunk
    partitions = (weights * targetNum / sum(weights)).astype(int)

    returnPanda = pd.DataFrame()

    for i in range(k):
        chunk = ((i)*chunkSize, (i+1)*chunkSize)

        # Load file based on file type
        if "csv" in location:
            # data = loadCSV(location, chunk[1], chunk[0])
            pass
        elif "json" in location:
            data = loadJSON(location, chunk[1], chunk[0])
        else:
            sys.exit("Unknown file - please specify correct csv or json file")
        indices = random.sample(range(chunkSize), partitions[i])
        data = data.iloc[indices, ]
        returnPanda = returnPanda.append(data)

    return returnPanda
