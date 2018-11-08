import os
import sys
import json
from shutil import copyfile
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.preprocessPrompt()
if Injector.preprocess:
    Injector.timeWindowPrompt()
    Injector.filterPrompt()
    Injector.setMontageConversionPrompt()


def noseizureExtraction(patient):
    for edf in patient['fileNames']:
        manifest = DataManifest(
            edf.split("/")[-1], 'noseizure', patient['info']['age'],
            patient['info']['gender'])
        manifest.generateRecord()
        if Injector.preprocess:
            edfRecord = EDF(edf)
            seizureDuration = round(edfRecord.duration(), 4)
            for i in range(int(seizureDuration // Injector.timeWindow) - 1):
                edfRecord = EDF(edf)
                edfRecord.loadData(Injector.timeWindow * i,
                                   Injector.timeWindow * (i + 1))
                manifest.seg = i + 1
                manifest.filterName = Injector.filter
                manifest.generateRecord()
                manifest.writeToManifest()
                if Injector.performConversion:
                    edfRecord.saveFile(edfRecord.montageConversion(),
                                       manifest.fileName)
                else:
                    edfRecord.saveFile(edfRecord.raw, manifest.fileName)
        else:
            edfRecord.saveFile(EDF(session["edf"]).raw, manifest.fileName)


def main():
    EDF.setFilter(Injector.filter)
    if Injector.timeWindow:
        DataManifest.setFolder('./{}_{}s_noseizure_seg'.format(
            Injector.dataset, Injector.timeWindow))
    else:
        DataManifest.setFolder('./{}_noseizure'.format(
            Injector.dataset))
    with open(f'{Injector.location}.json') as f:
        data = json.load(f)
        os.makedirs(f'./{DataManifest.dirName}', exist_ok=True)
        for channel in path:
            patients = data[channel]['noSeizure']
            for patient in patients:
                noseizureExtraction(patient)
    print("Segments count: " + str(DataManifest.index))

def merge():
    merge_of_noseizure = []
    files = os.listdir('{}/{}'.format(DataManifest.dirName, 'noseizure'))
    random.shuffle(files)[:count]
    for fileItem in files:
        raw = mne.io.read_raw_fif('{}/{}/{}'.format(DataManifest.dirName, 'noseizure', fileItem))
        merge_of_noseizure.append(raw)
    edfRecord.saveFile(
        mne.concatenate_raws(merge_of_noseizure), '{}/merged_noseizure.fif'.format(path))

import time
start_time = time.time()
main()
Injector.mergePrompt()
if Injector.mergeFiles:
    merge()
print("--- %s seconds ---" % (time.time() - start_time))
