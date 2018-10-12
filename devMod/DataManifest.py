import csv
import os


class DataManifest:
    fieldnames = [
        'index', 'patientID', 'sessionID', 'fileID', 'originalFreq',
        'sampleFreq', 'seizureType', 'fileName'
    ]
    index = 0

    fileList = {}

    @classmethod
    def setFolder(cls, dirName):
        cls.dirName = dirName

    @classmethod
    def buildDir(self):
        os.makedirs(f'./{DataManifest.dirName}', exist_ok=True)
        with open(f'./{DataManifest.dirName}/manifest.csv', 'w') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=DataManifest.fieldnames)
            writer.writeheader()

    def __init__(self, fileName, seizureType):
        DataManifest.index += 1
        self.ogFile = fileName
        self.seizureType = seizureType
        os.makedirs(
            f'./{DataManifest.dirName}/{self.seizureType}', exist_ok=True)
        self.sessionCount = DataManifest.fileList.get(self.ogFile, 0) + 1
        DataManifest.fileList[self.ogFile] = self.sessionCount
        self.generateRecord()

    def generateRecord(self):
        patientID, sessionID, fileID = \
            self.ogFile.split('.')[0].split('_')

        self.patientID = str(int(patientID))
        self.sessionID = 's' + str(int(sessionID[1:]))
        self.fileID = 't' + str(int(fileID[1:]))
        self.fileName = f'./{DataManifest.dirName}/{self.seizureType}/' + '_'.join(
            [
                patientID, sessionID, fileID, '_se' + str(self.sessionCount),
                'raw.fif'
            ])

    def buildDict(self):
        return {
            'index': DataManifest.index,
            'patientID': self.patientID,
            'sessionID': self.sessionID,
            'fileID': self.fileID,
            'originalFreq': self.freq,
            'sampleFreq': 128,
            'seizureType': self.seizureType,
            'fileName': self.fileName
        }

    def writeToManifest(self):
        with open(f'./{DataManifest.dirName}/manifest.csv', 'a') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=DataManifest.fieldnames)
            writer.writerow(self.buildDict())
