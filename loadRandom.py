import random
import pandas as pd
import sys
import re
import csv


def loadRandom(location, targetNum=1e5, seed=12345):
    random.seed(seed)
    # size of data set
    n = 6685900
    include = sorted(random.sample(range(n), int(targetNum)))
    data = []
    if "json" in location:
        import json
        loadFunc = json.loads
    elif "csv" in location:
        sys.exit("Please load in the json file, not csv")
        # import csv
        # def loadFunc(line): return list(csv.reader(line))[0]
    with open(location) as file:
        for i, line in enumerate(file):
            try:
                if i == include[0]:
                    del include[0]
                    data.append(loadFunc(line))
            except IndexError:
                break
    return pd.DataFrame(data)


def loadRandom2(location, targetNum=1e6, seed=12345, n=6000000-1):
    random.seed(seed)
    # number of records in file (excludes header)
    # n = sum(1 for line in open(location, encoding="utf8") if re.search(
    #     "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", line))
    # the 0-indexed header will not be included in the skip list
    skip = sorted(random.sample(range(1, n+1), n-int(targetNum)))
    return pd.read_csv(location, skiprows=skip, dtype={'text': str})


if __name__ == '__main__':
    location = '/Users/caitchison/Documents/Yelp/yelp_dataset/restaurants_only.csv'
    data = loadRandom2(location, 1e5, seed=2019, n=3778803)
    with open('LIWC/sample4.csv', mode='w') as file:
        # quoting=csv.QUOTE_ALL
        writer = csv.writer(file, delimiter=',', quotechar='"')
        writer.writerow(['text', 'useful', 'cool', 'funny', 'date'])
        for i in range(len(data)):
            writer.writerow([data['text'][i], data['useful']
                             [i], data['cool'][i], data['funny'][i]])
