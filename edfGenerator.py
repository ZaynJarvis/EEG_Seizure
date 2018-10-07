import pyedflib
import os
import time
import json
import sys
import numpy as np
from mne.io import concatenate_raws, read_raw_edf
from mne import Epochs, pick_types, find_events

path = [
    "01_tcp_ar",
    "02_tcp_le",
    "03_tcp_ar_a"
]

if len(sys.argv) > 1 and sys.argv[1] == 'prod':
    cropEnd = True
    fn = 'Temple_University_Hospital_EEG'
else:
    cropEnd = False
    fn = 'dev_test'


def genFolder(PA):
    for p in PA:
        os.makedirs(f'./gen/train/{p}', exist_ok=True)


# result = [P1-F7,  F7-T3,  T3-T5,  T5-O1,  FP2-F8,  F8-T4,  T4-T6,  T6-O2,  T3-C3,  C3 -
#           CZ,  CZ-C4,  C4-T4,  FP1-F3,  F3-C3,  C3-P3,  P3-O1,  FP2-F4,  F4-C4,  C4-P4, P4-O2]


class EDF:
    false = []
    sigChan = {}
    commonChannel = \
        ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5',
         'T6', 'FZ', 'CZ', 'PZ']

    @classmethod
    def getEDF(cls, session, edf):

        # def writeFile(n, duration, freq, st):
        #     sigbufs = np.zeros((n, duration))
        #     for i in np.arange(n):
        #         sigbufs[i, :] = edfReader.readSignal(i)[int(
        #             float(session['seizure']['start'])*freq): int(
        #             float(session['seizure']['start'])*freq) + duration]
        #         fileName = session['edf'].split(
        #             "/")[-1].replace('edf', 'csv')
        #         np.savetxt(
        #             f'./gen/train/{channel}/{st}/{fileName}', sigbufs.T, delimiter=",")
        # raw = read_raw_edf(edf, preload=True, stim_channel='auto')

        print(edf)
        edfReader = pyedflib.EdfReader(edf)
        signal_labels = tuple(edfReader.getSignalLabels())

        # n = edfReader.signals_in_file
        # freq = edfReader.getSampleFrequencies()[1]
        # duration = int(round((float(session['seizure']['stop']) -
        #                       float(session['seizure']['start'])) * freq + 1))
        # st = session['seizure']['seizureType']
        # if st not in seiTypesGen:
        #     os.makedirs(f'./gen/train/{channel}/{st}', exist_ok=True)
        #     seiTypesGen[st] = 0
        # else:
        #     seiTypesGen[st] += 1

        if str(signal_labels) not in EDF.sigChan:
            EDF.sigChan[str(signal_labels)] = 0

            for i in EDF.commonChannel:
                for p in signal_labels:
                    if (i in p) and (i in EDF.commonChannel):
                        EDF.commonChannel.remove(i)
            if len(EDF.commonChannel) != 0:
                print(EDF.commonChannel)
                print(1)
                EDF.false.append(signal_labels)
        else:
            EDF.sigChan[str(signal_labels)] += 1

        # writeFile(n, duration, freq, st)

        edfReader._close()


with open(f'{fn}.json') as f:
    data = json.load(f)
    for channel in path:
        patients = data[channel]['noSeizure']
        for p in patients:
            for edf in p['fileNames']:
                EDF.getEDF('', edf)
        patients = data[channel]['seizure']
        for p in patients:
            for session in p['sessions']:
                EDF.getEDF(session, session['edf'])

with open(f'channels.json', 'w') as outfile:
    json.dump(EDF.sigChan, outfile)
