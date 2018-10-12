import pickle
from pprint import pprint
with open('./devMod/test_Age_Gender.pkl', 'rb') as f:
    test = pickle.load(f)

with open('./devMod/train_Age_Gender.pkl', 'rb') as f:
    train = pickle.load(f)
info = {'train': train, 'test': test}
