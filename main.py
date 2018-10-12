import os
import sys
import csv
import json
import numpy as np
from enum import Enum
from mne.io import concatenate_raws, read_raw_edf, RawArray
from mne import Epochs, pick_types, find_events, create_info

sfreq = 128

path = [
    "01_tcp_ar",
    "02_tcp_le",
    "03_tcp_ar_a"
]

commonChannel = \
    ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5',
     'T6', 'FZ', 'CZ', 'PZ']


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


Channel = enum('FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5',
               'T6', 'FZ', 'CZ', 'PZ')
fieldnames = ['index', 'patientID', 'sessionID',
              'fileID', 'seizureType', 'fileName']


if sys.argv[1] == 'prod':
    cropEnd = True
    fn = 'Temple_University_Hospital_EEG'
    dirName = 'trainSet'
elif sys.argv[1] == 'test':
    cropEnd = False
    fn = 'dev_test'
    dirName = 'testSet'


class EDF:
    false = []
    sigChan = {}
    sigFreq = {}

    def __init__(self, edf):
        self.raw = read_raw_edf(edf, preload=False, stim_channel=None)
        self.raw.rename_channels(
            mapping=self.changeChannel())

    def __del__(self):
        self.raw.close()

    def loadData(self, start, stop):
        self.raw = self.raw.crop(tmin=float(start), tmax=float(stop))
        self.raw = self.raw.load_data() \
            .pick_channels(['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1',
                            'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'FZ', 'CZ', 'PZ']) \
            .reorder_channels(['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1',
                               'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'FZ', 'CZ', 'PZ']) \
            .pick_types(meg=False, eeg=True) \
            .resample(sfreq=sfreq) \
            .filter(1, 30, method='iir')
        return self.raw

    def montageConversion(self):
        info = create_info(
            ch_names=["FP1-F7",  "F7-T3",  "T3-T5",  "T5-O1",  "FP2-F8",  "F8-T4",  "T4-T6",  "T6-O2",  "T3-C3",  "C3-CZ",
                      "CZ-C4",  "C4-T4",  "FP1-F3",  "F3-C3",  "C3-P3",  "P3-O1",  "FP2-F4",  "F4-C4",  "C4-P4", "P4-02"],
            ch_types='eeg',
            sfreq=sfreq
        )
        data = [self.raw.get_data(Channel.FP1)[0]
                - self.raw.get_data(Channel.F7)[0],
                self.raw.get_data(Channel.F7)[0]
                - self.raw.get_data(Channel.T3)[0],
                self.raw.get_data(Channel.T3)[0]
                - self.raw.get_data(Channel.T5)[0],
                self.raw.get_data(Channel.T5)[0]
                - self.raw.get_data(Channel.O1)[0],
                self.raw.get_data(Channel.FP2)[0]
                - self.raw.get_data(Channel.F8)[0],
                self.raw.get_data(Channel.F8)[0]
                - self.raw.get_data(Channel.T4)[0],
                self.raw.get_data(Channel.T4)[0]
                - self.raw.get_data(Channel.T6)[0],
                self.raw.get_data(Channel.T6)[0]
                - self.raw.get_data(Channel.O2)[0],
                self.raw.get_data(Channel.T3)[0]
                - self.raw.get_data(Channel.C3)[0],
                self.raw.get_data(Channel.C3)[0]
                - self.raw.get_data(Channel.CZ)[0],
                self.raw.get_data(Channel.CZ)[0]
                - self.raw.get_data(Channel.C4)[0],
                self.raw.get_data(Channel.C4)[0]
                - self.raw.get_data(Channel.T4)[0],
                self.raw.get_data(Channel.FP1)[0]
                - self.raw.get_data(Channel.F3)[0],
                self.raw.get_data(Channel.F3)[0]
                - self.raw.get_data(Channel.C3)[0],
                self.raw.get_data(Channel.C3)[0]
                - self.raw.get_data(Channel.P3)[0],
                self.raw.get_data(Channel.P3)[0]
                - self.raw.get_data(Channel.O1)[0],
                self.raw.get_data(Channel.FP2)[0]
                - self.raw.get_data(Channel.F4)[0],
                self.raw.get_data(Channel.F4)[0]
                - self.raw.get_data(Channel.C4)[0],
                self.raw.get_data(Channel.C4)[0]
                - self.raw.get_data(Channel.P4)[0],
                self.raw.get_data(Channel.P4)[0]
                - self.raw.get_data(Channel.O2)[0]]
        return RawArray(data, info)

    def changeChannel(self):
        ch = {}
        x = self.raw.info['ch_names']
        for i in x:
            try:
                ch[i] = i.split(' ')[1].split('-')[0]
            except Exception:
                pass
        return ch

    def getFreq(self):
        if str(self.raw.info['sfreq']) in EDF.sigFreq.keys():
            EDF.sigFreq[str(self.raw.info['sfreq'])] += 1
        else:
            EDF.sigFreq[str(self.raw.info['sfreq'])] = 1

        return str(self.raw.info['sfreq'])


def main():
    index = 0
    with open(f'{fn}.json') as f:
        data = json.load(f)
        dataDic = {}
        os.makedirs(f'./{dirName}', exist_ok=True)
        with open(f'./{dirName}/manifest.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        for channel in path:
            # Nspatients = data[channel]['noSeizure']
            # for p in Nspatients:
            #     for edf in p['fileNames']:
            #         # edfRecord = EDF(edf)
            #         pass
            Spatients = data[channel]['seizure']
            for p in Spatients:
                dataDic['patientID'] = p['id']
                fileName = None
                count = 1
                for session in p['sessions']:
                    index += 1
                    dataDic['index'] = index
                    edfRecord = EDF(session['edf'])
                    edfRecord.loadData(
                        session['seizure']['start'], session['seizure']['stop'])
                    seizureType = session['seizure']['seizureType']
                    if fileName == session["edf"].split("/")[-1]:
                        count += 1
                    else:
                        fileName = session["edf"].split("/")[-1]
                        count = 1
                    patientID, sessionID, fileID = \
                        fileName.split('.')[0].split('_')
                    patientID = str(int(patientID))
                    sessionID = 's' + str(int(sessionID[1:]))
                    fileID = 't' + str(int(fileID[1:]))
                    os.makedirs(f'./{dirName}/{seizureType}', exist_ok=True)
                    destinationFileName = f'./{dirName}/{seizureType}/' + '_'.join(
                        [patientID, sessionID, fileID, '_se' + str(count), 'raw.fif'])
                    edfRecord.montageConversion().save(destinationFileName)

                    dataDic['sessionID'] = sessionID
                    dataDic['fileID'] = fileID
                    dataDic['seizureType'] = seizureType
                    dataDic['fileName'] = destinationFileName

                    with open(f'./{dirName}/manifest.csv', 'a') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow(dataDic)


def test():
    index = 0
    with open(f'{fn}.json') as f:
        data = json.load(f)
        Spatients = data["01_tcp_ar"]["seizure"]
        os.makedirs(f'./{dirName}', exist_ok=True)
        with open(f'./{dirName}/manifest.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        for p in Spatients[:5]:
            dataDic = {'patientID': p['id']}
            fileName = None
            count = 1
            for session in p['sessions']:
                index += 1
                dataDic['index'] = index
                edfRecord = EDF(session['edf'])
                edfRecord.loadData(
                    session['seizure']['start'], session['seizure']['stop'])
                seizureType = session['seizure']['seizureType']
                if fileName == session["edf"].split("/")[-1]:
                    count += 1
                else:
                    fileName = session["edf"].split("/")[-1]
                    count = 1
                patientID, sessionID, fileID = \
                    fileName.split('.')[0].split('_')
                patientID = str(int(patientID))
                sessionID = 's' + str(int(sessionID[1:]))
                fileID = 't' + str(int(fileID[1:]))
                os.makedirs(f'./{dirName}/{seizureType}', exist_ok=True)
                destinationFileName = f'./{dirName}/{seizureType}/' + '_'.join(
                    [patientID, sessionID, fileID, '_se' + str(count), 'raw.fif'])
                edfRecord.montageConversion().save(destinationFileName)

                dataDic['sessionID'] = sessionID
                dataDic['fileID'] = fileID
                dataDic['seizureType'] = seizureType
                dataDic['fileName'] = destinationFileName

                with open(f'./{dirName}/manifest.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(dataDic)


main()

# with open(f'channels.json', 'w') as outfile:
#     json.dump(EDF.sigChan, outfile)

# {'400.0': 99, '250.0': 279, '512.0': 35, '256.0': 1001}

# {'250.0': 1127, '400.0': 497, '256.0': 1152, '512.0': 46}
