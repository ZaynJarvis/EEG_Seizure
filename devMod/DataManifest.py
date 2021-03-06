import csv
import os


class DataManifest:
    fieldnames = [
        'patientID', 'age', 'gender', 'sessionID', 'fileID', 'segment',
        'originalFreq', 'sampleFreq', 'seizureDuration', 'seizureType',
        'fileName'
    ]
    index = 0
    fileList = {}
    totalDuration = 0

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
        os.makedirs(
            f'./{DataManifest.dirName}/{self.seizureType}', exist_ok=True)

    def __init__(self, fileName, seizureType, age, gender):
        self.age = age
        self.gender = gender
        self.ogFile = fileName
        self.seizureType = seizureType
        self.seg = None
        self.filterName = None
        self.seizureDuration = 0
        self.sessionCount = DataManifest.fileList.get(self.ogFile, 0) + 1
        DataManifest.fileList[self.ogFile] = self.sessionCount
        DataManifest.index += 1

    def generateRecord(self):
        patientID, sessionID, fileID = \
            self.ogFile.split('.')[0].split('_')

        self.patientID = str(int(patientID))
        self.sessionID = 's' + str(int(sessionID[1:]))
        self.fileID = 't' + str(int(fileID[1:]))
        self.fileName = f'./{DataManifest.dirName}/{self.seizureType}/' + '_'.join(
            [
                x for x in [
                    self.patientID, self.sessionID, self.fileID, 'se' +
                    str(self.sessionCount),
                    str(self.seg), self.filterName, 'raw.fif'
                ] if x is not None
            ])

    def setSeizureDuration(self, duration):
        DataManifest.totalDuration += duration
        self.seizureDuration = str(round(duration, 4))

    def buildDict(self):
        return {
            'age': self.age,
            'gender': self.gender,
            'patientID': self.patientID,
            'sessionID': self.sessionID,
            'fileID': self.fileID,
            'originalFreq': self.freq,
            'sampleFreq': 128.0,
            'seizureDuration': self.seizureDuration,
            'segment': self.seg,
            'seizureType': self.seizureType,
            'fileName': self.fileName
        }

    def writeToManifest(self):
        with open(f'./{DataManifest.dirName}/manifest.csv', 'a') as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=DataManifest.fieldnames)
            writer.writerow(self.buildDict())
