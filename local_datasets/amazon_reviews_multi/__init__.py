import pandas as pd

# Vue que le datasets n'est plus disponible dans le module datasets je l'importe directement ici
try:
    train = pd.read_csv('./local_datasets/amazon_reviews_multi/train.csv')
    test = pd.read_csv('./local_datasets/amazon_reviews_multi/test.csv')
    validation = pd.read_csv('./local_datasets/amazon_reviews_multi/validation.csv')
    dataset = pd.concat([train, test, validation])
except:
    print('Please download the amazon_reviews_multi datasets here: https://www.kaggle.com/datasets/mexwell/amazon-reviews-multi')
    exit()