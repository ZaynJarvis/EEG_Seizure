import json
import csv
import sys
from devMod import Patient, EDF, DataManifest, path, Injector
from shutil import copyfile
from itertools import chain


Injector.datasetPrompt()
currentPatient = None
Injector.version = 'v1.5'

def processData(fileName, currentPatient):
    if currentPatient != None:
        if currentPatient.count != '0':
            jsonOutput[fileName]["seizure"].append({
                "id":
                currentPatient.id,
                "info":
                currentPatient.info,
                "sessions":
                currentPatient.seizure
            })
            if currentPatient.noSeizure:
                jsonOutput[fileName]["noSeizure"].append({
                    "id":
                    currentPatient.id,
                    "info":
                    currentPatient.info,
                    "fileNames":
                    currentPatient.noSeizure
                })
        else:
            jsonOutput[fileName]["noSeizure"].append({
                "id":
                currentPatient.id,
                "info":
                currentPatient.info,
                "fileNames":
                currentPatient.noSeizure
            })


jsonOutput = {
    "01_tcp_ar": {
        "seizure": [],
        "noSeizure": []
    },
    "02_tcp_le": {
        "seizure": [],
        "noSeizure": []
    },
    "03_tcp_ar_a": {
        "seizure": [],
        "noSeizure": []
    }
}



with open(f'{Injector.location}.csv', newline='\n') as f:
    Patient.dataset = Injector.dataset
    reader = list(csv.reader(f, delimiter=','))
    reader = reader[1:]
    firstLine = True

    for row in reader:
        if firstLine:
            fileName = row[11].split('/')[3]
            firstLine = False
        if row[2]:
            processData(fileName, currentPatient)
            fileName = row[11].split('/')[3]
            currentPatient = Patient(row[2], row[10], row[3],
                                     ' | '.join(row[5:7]))
        currentPatient.addSession(row[4], row[12], row[13], row[14],
                                  row[11].replace('tse', 'edf'))
        currentPatient.addInfo('_'.join(row[11].split('_')[:-1]) + '.txt')
    fileName = row[11].split('/')[3]
    processData(fileName, currentPatient)



seizure = []
noSeizure = []

for channel in path:
    seizure.extend(jsonOutput[channel]['seizure'])
    noSeizure.extend(jsonOutput[channel]['noSeizure'])

with open(f'{Injector.location}.json', 'w') as outfile:
    json.dump(jsonOutput, outfile)
with open(f'{Injector.location}-seizure.json', 'w') as outfile:
    json.dump(seizure, outfile)

with open(f'{Injector.location}-no-seizure.json', 'w') as outfile:
    json.dump(noSeizure, outfile)

def seizureExtraction(patient):
    for session in patient['sessions']:
        manifest = DataManifest(
            session["edf"].split("/")[-1], session['seizure']['seizureType'],
            patient['info']['age'], patient['info']['gender'])
        manifest.generateRecord()
        seizureDuration = \
                float(session['seizure']['stop']) - \
                float(session['seizure']['start'])
        manifest.setSeizureDuration(seizureDuration)

def seizure():
    DataManifest.setFolder('./{}_seizure'.format(Injector.dataset))
    with open(f'./{Injector.location}.json') as f:
        patientList = set()
        data = json.load(f)
        result = {}
        sessionsWithSeizures = 0
        for channel in path:
            patients = data[channel]['seizure']
            sessionsWithSeizures += len(patients)
            for patient in patients:
                patientList.add(patient['id'])
                seizureExtraction(patient)
    print("------------")
    print("Total number of seizures: " + str(DataManifest.index))
    print("Total seizure duration: " + str(DataManifest.totalDuration))
    print("No. sessions w/ seizures: " + str(sessionsWithSeizures))
    print("No. patients w/ seizures: " + str(len(patientList)))
    print("------------")

def noSeizure():
    edfCount = 0
    DataManifest.setFolder('./{}_noseizure'.format(Injector.dataset))
    with open(f'./{Injector.location}.json') as f:
        patientList = set()
        data = json.load(f)
        result = {}
        sessionsWithSeizures = 0
        for channel in path:
            patients = data[channel]['noSeizure']
            sessionsWithSeizures += len(patients)
            for patient in patients:
                patientList.add(patient['id'])
                edfCount += len(patient['fileNames'])
    print("------------")
    print("Total files w/o seizures: " + str(edfCount))
    print("No. sessions w/o seizures: " + str(sessionsWithSeizures))
    print("No. patients w/o seizures: " + str(len(patientList)))
    print("------------")


import time
start_time = time.time()
seizure()
noSeizure()
print("--- %s seconds ---" % (time.time() - start_time))
