import json
import csv
import sys
from devMod import Patient, Injector, path


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

with open(f'{Injector.location}.json', 'w') as outfile:
    json.dump(jsonOutput, outfile)

seizure = []
noSeizure = []

for channel in path:
    seizure.extend(jsonOutput[channel]['seizure'])
    noSeizure.extend(jsonOutput[channel]['noSeizure'])

with open(f'{Injector.location}-seizure.json', 'w') as outfile:
    json.dump(seizure, outfile)

with open(f'{Injector.location}-no-seizure.json', 'w') as outfile:
    json.dump(noSeizure, outfile)

print("Patient with seizure " + str(Patient.countx))
print("Patient without seizure " + str(Patient.countn))