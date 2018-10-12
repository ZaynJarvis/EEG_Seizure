import json
import csv
import sys

if sys.argv[1] == 'prod':
    cropEnd = True
    fn = 'original_data_manifest/Temple_University_Hospital_EEG'
    fileNameCrop = 3
elif sys.argv[1] == 'test':
    cropEnd = True
    fn = 'original_data_manifest/dev_test'
    fileNameCrop = 2


class Patient:
    countx = 0
    countn = 0

    def __init__(self, patientID, count, sessionID, EEG):
        self.count = count
        self.id = patientID
        self.fileName = None
        self.fileNameList = []
        self.info = {}
        self.info["EEG"] = EEG
        self.info["sessionID"] = sessionID
        self.info["seizureCount"] = count
        self.seizure = []
        self.noSeizure = []

    def addSession(self, fileName, start, stop, seizureType, edf):
        if fileName:
            self.fileName = fileName
        session = {}
        if start:
            Patient.countx += 1
            session["fileName"] = self.fileName
            session["edf"] = edf
            session["seizure"] = {}
            session["seizure"]["start"] = start
            session["seizure"]["stop"] = stop
            session["seizure"]["seizureType"] = seizureType
            self.seizure.append(session)
        else:
            self.noSeizure.append(edf)
            Patient.countn += 1


def processData(fileName):
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

currentPatient = None

with open(f'{fn}.csv', newline='\n') as f:
    reader = list(csv.reader(f, delimiter=','))
    if cropEnd:
        reader = reader[2:-4]
    else:
        reader = reader[2:]
    firstLine = True
    for row in reader:
        if firstLine:
            fileName = row[12].split('/')[fileNameCrop]
            firstLine = False
        if row[2]:
            processData(fileName)
            fileName = row[12].split('/')[fileNameCrop]
            currentPatient = Patient(row[2], row[11], row[4],
                                     ' | '.join(row[6:8]))
        currentPatient.addSession(row[5], row[13], row[14], row[15],
                                  row[12].replace('tse', 'edf'))
    fileName = row[12].split('/')[fileNameCrop]
    processData(fileName)

with open(f'{fn}.json', 'w') as outfile:
    json.dump(jsonOutput, outfile)
