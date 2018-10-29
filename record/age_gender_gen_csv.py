import pickle
import csv

fn = 'train'
with open(f'./devMod/{fn}_Age_Gender.pkl', 'rb') as f:
    des = pickle.load(f)
male = 0
female = 0
unknown = 0
ageCount = 0
ageSum = 0
with open(f'./original_data_manifest/{fn}_age_gender.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['PatientID', 'age', 'gender'])
    for i in des.keys():
        if des[i]['gender'] == 'male':
            male += 1
        elif des[i]['gender'] == 'female':
            female += 1
        else:
            unknown += 1
        if des[i]['age'] != 'unknown':
            ageSum += int(des[i]['age'])
            ageCount += 1
        writer.writerow([i, des[i]['age'], des[i]['gender']])
    writer.writerow(['avg_age', 'maleCount', 'femaleCount', 'unknownGender'])
    writer.writerow([
        str(round(ageSum / ageCount, 2)),
        str(male),
        str(female),
        str(unknown)
    ])
