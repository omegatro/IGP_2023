import random
import pandas as pd
import sys

def read_random_rows(file_path, seed, fraction=0.05):
    'Ŗandomly sampling fraction of records from csv file into pandas dataframe based on: https://cmdlinetips.com/2022/07/randomly-sample-rows-from-a-big-csv-file/'
    random.seed(seed)
    if fraction < 1:
        return pd.read_csv(file_path, 
            skiprows=lambda x: x > 0 and random.random() >=fraction)
    else:
        return pd.read_csv(file_path)
    

if __name__ == "__main__":
    file_path = sys.argv[1]
    seed = 4321
    df = read_random_rows(file_path=file_path, seed=seed,fraction=1)
    print(df.describe())
    print(len(df))