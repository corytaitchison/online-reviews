import pandas as pd
import numpy as np


def groupData(data, by, subsets, seed=12345):
    masks = []
    for i in range(1, len(subsets)):
        previous = subsets[i-1]
        masks.append((by > previous) &
                     (by <= subsets[i]))

    # masks = [data.interactions == x for x in subsets]
    # if otherwise:
    #     masks.append(
    #         (data.interactions > subsets[-1]) & (data.interactions < maxVal))
    subsetSize = min([sum(mask) for mask in masks if sum(mask) > 0])
    print("Creating subsets of size %i" % subsetSize)

    newData = pd.DataFrame([])
    for mask in masks:
        if len(data[mask]) == 0:
            continue
        df = data[mask].sample(n=subsetSize, random_state=seed)
        newData = newData.append(df)

    return newData
