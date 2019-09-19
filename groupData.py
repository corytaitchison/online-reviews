import pandas as pd
import numpy as np


def groupData(data, subsets, seed=12345):
    masks = []
    for i in range(len(subsets)):
        previous = subsets[i-1]
        if i == 0:
            previous = 0
        masks.append((data.interactions > previous) &
                     (data.interactions <= subsets[i]))

    # masks = [data.interactions == x for x in subsets]
    # if otherwise:
    #     masks.append(
    #         (data.interactions > subsets[-1]) & (data.interactions < maxVal))
    subsetSize = min([sum(mask) for mask in masks])

    print("Creating subsets of size %i" % subsetSize)

    newData = pd.DataFrame([])
    for mask in masks:
        df = data[mask].sample(n=subsetSize, random_state=seed)
        newData = newData.append(df)

    return newData
