import json
import pandas as pd
from devMod import Injector

Injector.datasetPrompt()
Injector.timeWindowPrompt()

patientMap = {}


def mean(arr):
    return sum(arr) / len(arr)


def std(arr):
    m = mean(arr)
    return sum(map(lambda x: (x - m)**2, arr)) / len(arr)


with open(f'./{Injector.location}.json') as f:
    df = pd.read_csv(
        f'./{Injector.dataset}_{Injector.timeWindow}s_seg/manifest.csv').drop(
            ['index', 'originalFreq', 'sampleFreq', 'fileName'], axis=1)
    data = json.load(f)
    for channel in data.keys():
        for patient in data[channel]['seizure']:
            id = patient['id']
            record = df.loc[lambda df: df['patientID'] == int(id), :]
            try:
                x = patientMap[id]
            except Exception:
                patientMap[id] = {}
                patientMap[id]['age'] = set(record['age']).pop()
                patientMap[id]['gender'] = patient['info']['gender']
                patientMap[id]['Seizure Type'] = set(record['seizureType'])
                patientMap[id]['No.Seizures'] = 0

                sd = set(record['seizureDuration'])
                patientMap[id][
                    'seizureDuration'] = f'{round(mean(sd),4)} +/- {round(std(sd),4)}'
                patientMap[id]['No.EEGSegment'] = len(record)
            patientMap[id]['No.Seizures'] += int(
                patient['info']['seizureCount'])


def buildDict(key):
    info = patientMap[key]
    return {
        'Patient ID': key,
        'Age': info['age'],
        'Gender': info['gender'],
        'No.of seizures': info['No.Seizures'],
        'Seizure Type': info['Seizure Type'],
        'Seizure duration (mean ±SD)': info['seizureDuration'],
        'No. of EEG segments (5sec)': info['No.EEGSegment']
    }


import csv
with open(
        f'./original_data_manifest/{Injector.dataset}_{Injector.timeWindow}s_seg_manifest.csv',
        'w') as target:
    writer = csv.DictWriter(
        target,
        fieldnames=[
            'Patient ID', 'Age', 'Gender', 'No.of seizures', 'Seizure Type',
            'Seizure duration (mean ±SD)', 'No. of EEG segments (5sec)'
        ])
    writer.writeheader()
    writer.writerows(list(map(buildDict, patientMap.keys())))
