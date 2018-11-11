import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.timeWindowPrompt()
Injector.filterPrompt()
Injector.setMontageConversionPrompt()


def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
        seizureDuration = \
            float(session['seizure']['stop']) - \
            float(session['seizure']['start'])
        for i in range(int(seizureDuration // Injector.timeWindow)):
            edfRecord = EDF(session['edf'])
            edfRecord.loadData(
                str(
                    float(session['seizure']['start']) +
                    Injector.timeWindow * i),
                str(
                    float(session['seizure']['start']) +
                    Injector.timeWindow * (i + 1)))
            manifest.seg = i + 1
            manifest.seizureDuration = seizureDuration
            manifest.freq = edfRecord.ofreq
            manifest.generateRecord()
            manifest.writeToManifest()
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
        patientList = set()
        data = json.load(f)
        DataManifest.buildDir()
        result = {}
        for channel in path:
            patients = data[channel]['seizure']
            for patient in patients:
                seizureExtraction(patient)
    print("Segments count: " + str(DataManifest.index))


def merge():
    merge_of_seizure = []
    count = 0
    subfolders = os.listdir(DataManifest.dirName)
    for folder in subfolders:
        files = os.listdir('{}/{}'.format(DataManifest.dirName, folder))
        for fileItem in files:
            raw = mne.io.read_raw_fif('{}/{}/{}'.format(
                DataManifest.dirName, folder, fileItem))
            merge_of_seizure.append(raw)
            count += 1
    mne.concatenate_raws(merge_of_seizure).save('{}/merged_seizure.fif'.format(
        DataManifest.dirName))
    print(f"You have {count} segments merged.")


import time
start_time = time.time()
main()
Injector.mergePrompt()
if Injector.mergeFiles:
    merge()
print("--- %s seconds ---" % (time.time() - start_time))
