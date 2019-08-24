import json
import pandas as pd
import os.path
import sys

# Limit how many lines to read (cannot read whole file at once
# otherwise system runs out of memory).
# Recommend maximum 1e6 (1 million lines)
readLimit = 1e3


def loadJSON(fileLocation):
    data = []
    with open(fileLocation) as file:
        for i, line in enumerate(file):
            if i > 1e3:
                break
            data.append(json.loads(line))
    return pd.DataFrame(data)


if __name__ == '__main__':
    # Set this to the location of your JSON file
    fileLocation = '/Users/caitchison/Documents/Yelp/yelp_dataset/review.json'
    if not os.path.isfile(fileLocation):
        sys.exit(
            "%s does not exist - please change the code to match your directory" % fileLocation)
    data = loadJSON(fileLocation)
    print(data.info())
