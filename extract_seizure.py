import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path

# run: ```python extract_seizure.py prod``` for training dataset
#  or: ```python extract_seizure.py test``` for dev_test dataset

if sys.argv[1] == 'train':
    cropEnd = True
    db = 'original_data_manifest/Temple_University_Hospital_EEG'
    DataManifest.setFolder('trainSet')
elif sys.argv[1] == 'test':
    cropEnd = False
    db = 'original_data_manifest/dev_test'
    DataManifest.setFolder('testSet')


def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
        seizureDuration = str(
            round(
                float(session['seizure']['stop']) - float(
                    session['seizure']['start']), 4))
        edfRecord = EDF(session['edf'])
        edfRecord.loadData(
            float(session['seizure']['start']),
            float(session['seizure']['stop']))

        manifest.seizureDuration = seizureDuration
        manifest.freq = edfRecord.ofreq
        manifest.seg = 1
        manifest.generateRecord()
        manifest.writeToManifest()
        edfRecord.saveFile(edfRecord.montageConversion(), manifest.fileName)


def noseizureExtraction(data, patientId):
    aggregate = filter(lambda x: x['id'] == patientId, data)
    files = list(map(lambda x: x['fileNames'], aggregate))
    itemList = chain.from_iterable(files)
    a = 0
    for record in itemList:
        edfRecord = EDF(record)
        a += edfRecord.duration()
    return a


def main():
    with open(f'{db}.json') as f:
        patientList = set()
        data = json.load(f)
        DataManifest.buildDir()
        result = {}
        for channel in path:
            patients = data[channel]['seizure']
            for patient in patients:
                seizureExtraction(patient)


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))