import os
import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.timeWindowPrompt()
Injector.filterPrompt()
Injector.setMontageConversionPrompt()


def noseizureExtraction(patient):
    for edf in patient['fileNames']:
        edfRecord = EDF(edf)
        seizureDuration = round(edfRecord.duration(), 4)
        manifest = DataManifest(
            edf.split("/")[-1], 'No', patient['info']['age'],
            patient['info']['gender'])

        for i in range(int(seizureDuration // Injector.timeWindow)):
            edfRecord = EDF(edf)
            edfRecord.loadData(Injector.timeWindow * i,
                               Injector.timeWindow * (i + 1))
            manifest.seg = i + 1
            manifest.generateRecord()
            if Injector.performConversion:
                edfRecord.saveFile(edfRecord.montageConversion(),
                                   manifest.fileName)
            else:
                edfRecord.saveFile(edfRecord.raw, manifest.fileName)


def main():
    EDF.setFilter(Injector.filter)
    DataManifest.setFolder('./{}_{}s_seg'.format(Injector.dataset,
                                                 Injector.timeWindow))
    with open(f'{Injector.location}.json') as f:
        data = json.load(f)
        os.makedirs(f'./{DataManifest.dirName}', exist_ok=True)
        for channel in path:
            patients = data[channel]['noSeizure']
            for patient in patients:
                noseizureExtraction(patient)
    print("Segments count: " + str(DataManifest.index))


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
