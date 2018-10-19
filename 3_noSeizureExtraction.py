import os
import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path

timeWindow = int(input("what's your time window?\n"))

# run: ```python data_segmentation.py prod``` for training dataset
#  or: ```python data_segmentation.py test``` for dev_test dataset

if sys.argv[1] == 'train':
    cropEnd = True
    db = 'original_data_manifest/Temple_University_Hospital_EEG'
    DataManifest.setFolder('trainSetSeg')
elif sys.argv[1] == 'test':
    cropEnd = False
    db = 'original_data_manifest/dev_test'
    DataManifest.setFolder('testSetSeg')


def noseizureExtraction(patient):
    for edf in patient['fileNames']:
        edfRecord = EDF(edf)
        seizureDuration = round(edfRecord.duration(), 4)
        manifest = DataManifest(
            edf.split("/")[-1], 'No', patient['info']['age'],
            patient['info']['gender'])

        for i in range(int(seizureDuration // timeWindow)):
            edfRecord = EDF(edf)
            edfRecord.loadData(timeWindow * i, timeWindow * (i + 1))
            manifest.seg = i + 1
            manifest.generateRecord()
            edfRecord.saveFile(edfRecord.montageConversion(),
                               manifest.fileName)


def main():
    with open(f'{db}.json') as f:
        data = json.load(f)
        os.makedirs(f'./{DataManifest.dirName}', exist_ok=True)
        for channel in path:
            patients = data[channel]['noSeizure']
            for patient in patients:
                noseizureExtraction(patient)


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

print("count: " + str(DataManifest.index))
