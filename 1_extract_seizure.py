import sys
import json
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.filterPrompt()


def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
        seizureDuration = \
            float(session['seizure']['stop']) - \
            float(session['seizure']['start'])
        edfRecord = EDF(session['edf'])
        edfRecord.loadData(
            float(session['seizure']['start']),
            float(session['seizure']['stop']))

        manifest.setSeizureDuration(seizureDuration)
        manifest.freq = edfRecord.ofreq
        manifest.seg = 1
        manifest.generateRecord()
        manifest.writeToManifest()
        edfRecord.saveFile(edfRecord.montageConversion(), manifest.fileName)


def main():
    EDF.setFilter(Injector.filter)
    DataManifest.setFolder(Injector.dataset)
    with open(f'./{Injector.location}.json') as f:
        patientList = set()
        data = json.load(f)
        DataManifest.buildDir()
        result = {}
        sessionsWithSeizures = 0
        for channel in path:
            patients = data[channel]['seizure']
            sessionsWithSeizures += len(patients)
            for patient in patients[:3]:
                patientList.add(patient['id'])
                seizureExtraction(patient)


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

print("Total seizure duration: " + str(DataManifest.totalDuration))
print("No. sessions w/ seizures: " + str(sessionsWithSeizures))
print("No. patients w/ seizures: " + str(len(patientList)))