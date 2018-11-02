import sys
import json
from shutil import copyfile
from itertools import chain
from devMod import EDF, DataManifest, path, Injector

Injector.datasetPrompt()
Injector.preprocessPrompt()
if Injector.preprocess:
    Injector.filterPrompt()
    Injector.setMontageConversionPrompt()


def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
            manifest.generateRecord()
        if Injector.preprocess:
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
            manifest.filterName = Injector.filter
            manifest.generateRecord()
            manifest.writeToManifest()
            if Injector.performConversion:
                edfRecord.saveFile(edfRecord.montageConversion(),
                                   manifest.fileName)
            else:
                edfRecord.saveFile(edfRecord.raw, manifest.fileName)
        else:
            copyfile(session["edf"], manifest.fileName)

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
            for patient in patients:
                patientList.add(patient['id'])
                seizureExtraction(patient)
    print("The record is set to use the following channels in sequence:")
    print("------------")
    if Injector.performConversion:
        edfChannels = EDF.montageConversionChannels
    else:
        edfChannels = EDF.commonChannels
    for i, c in enumerate(edfChannels):
        print("No.{:02d}: {}".format(i + 1, c))
    print("------------")
    print("Total number of seizures: " + str(DataManifest.index))
    print("Total seizure duration: " + str(DataManifest.totalDuration))
    print("No. sessions w/ seizures: " + str(sessionsWithSeizures))
    print("No. patients w/ seizures: " + str(len(patientList)))


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
