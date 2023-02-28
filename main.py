from urllib.request import urlretrieve

url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'

urlretrieve(url, 'medical.csv')