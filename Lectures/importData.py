import pandas as pd

advertising = pd.read_csv('./data/Advertising.csv', usecols=[1,2,3,4])
#advertising.info()

credit = pd.read_csv('./data/Credit.csv', usecols=list(range(1,12)))
credit['Student2'] = credit.Student.map({'No':0, 'Yes':1})

auto = pd.read_csv('./data/Auto.csv', na_values='?').dropna()
#auto.info()

preg = pd.read_csv('data/pregNSFG.csv.gz', compression='gzip')

live = pd.read_hdf('./data/JoinedpregNSFG.csv.gz', compression='gzip')

boston = pd.read_csv('./data/boston.csv')