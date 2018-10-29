import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.timeWindowPrompt()
Injector.filterPrompt()


def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
        seizureDuration = str(
            round(
                float(session['seizure']['stop']) - float(
                    session['seizure']['start']), 4))

        for i in range(
                int((float(session['seizure']['stop']) - float(
                    session['seizure']['start'])) // timeWindow)):
            edfRecord = EDF(session['edf'])
            edfRecord.loadData(
                str(float(session['seizure']['start']) + timeWindow * i),
                str(float(session['seizure']['start']) + timeWindow * (i + 1)))
            manifest.seg = i + 1
            manifest.seizureDuration = seizureDuration
            manifest.freq = edfRecord.ofreq
            manifest.generateRecord()
            manifest.writeToManifest()

            edfRecord.saveFile(edfRecord.montageConversion(),
                               manifest.fileName)


def main():
    EDF.applyFilter = Injector.filter
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


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

print("count: " + str(DataManifest.index))
