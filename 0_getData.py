import json
import csv
import sys
from devMod import Patient, Injector


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

Injector.datasetPrompt()

currentPatient = None

with open(f'{Injector.location}.csv', newline='\n') as f:
    Patient.dataset = Injector.dataset
    reader = list(csv.reader(f, delimiter=','))
    reader = reader[2:-4]
    firstLine = True
    for row in reader:
        if firstLine:
            fileName = row[12].split('/')[Injector.fileNameCrop]
            firstLine = False
        if row[2]:
            processData(fileName, currentPatient)
            fileName = row[12].split('/')[Injector.fileNameCrop]
            currentPatient = Patient(row[2], row[11], row[4],
                                     ' | '.join(row[6:8]))
        currentPatient.addSession(row[5], row[13], row[14], row[15],
                                  row[12].replace('tse', 'edf'))
        currentPatient.addInfo('_'.join(row[12].split('_')[:-1]) + '.txt')
    fileName = row[12].split('/')[Injector.fileNameCrop]
    processData(fileName, currentPatient)

with open(f'{Injector.location}.json', 'w') as outfile:
    json.dump(jsonOutput, outfile)
