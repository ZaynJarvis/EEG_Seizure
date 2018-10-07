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

if sys.argv[1] == 'prod':
    cropEnd = True
    fn = 'Temple_University_Hospital_EEG'
elif sys.argv[1] == 'test':
    cropEnd = False
    fn = 'dev_test'

commonChannel = \
    ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5',
     'T6', 'FZ', 'CZ', 'PZ']


class EDF:
    false = []
    sigChan = {}
    sigFreq = {}

    def __init__(self, edf):
        self.raw = read_raw_edf(edf, preload=False, stim_channel='auto')
        self.raw.rename_channels(mapping=self.changeChannel())
        # self.processed = self.raw.copy() \
        #     .pick_types(meg=False, eeg=True) \
        #     .resample(sfreq=128) \
        #     .filter(1, 30, method='iir') \
        #     # .crop(6.2825, 35.8875)

    def __del__(self):
        self.raw.close()
        print("close")

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
    with open(f'{fn}.json') as f:
        data = json.load(f)
        for channel in path:
            Nspatients = data[channel]['noSeizure']
            for p in Nspatients:
                for edf in p['fileNames']:
                    edfRecord = EDF(edf)
                    edfRecord.getFreq()
            Spatients = data[channel]['seizure']
            for p in Spatients:
                for session in p['sessions']:
                    edfRecord = EDF(session['edf'])
                    edfRecord.getFreq()


def test():
    with open(f'{fn}.json') as f:
        data = json.load(f)
        pt = data["01_tcp_ar"]["seizure"]
        for p in pt[:10]:
            for s in p['sessions']:
                e = EDF(s['edf'])


test()

# with open(f'channels.json', 'w') as outfile:
#     json.dump(EDF.sigChan, outfile)
# {'400.0': 99, '250.0': 279, '512.0': 35, '256.0': 1001}
# {'250.0': 1127, '400.0': 497, '256.0': 1152, '512.0': 46}
