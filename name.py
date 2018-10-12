from pprint import pprint
import pickle
import re
with open('test.pkl', 'rb') as f:
    des = pickle.load(f)
new = {}
refind = {}
count = 0

for k, v in des.items():
    r = ''.join(v)
    ageD = re.findall('\d+-? *ye?a?rs?-? ?old', r)
    gender = re.findall('(gentleman|f?e?male|w?o?man|lady|girl)', r)
    des[k] = {}
    if ageD or gender:
        if ageD:
            age = re.match(r'\d+', ageD[0]).group()
            des[k] = {'age': age, 'gender': 'unknown'}
        if gender: des[k] = {'age': age, 'gender': gender[0]}
    else:
        print(v)
        des[k] = {'age': 'unknown', 'gender': 'unknown'}
        count += 1

pprint(des)

with open('test_Age_Gender.pkl', 'wb') as f:
    pickle.dump(des, f)
pprint(des)