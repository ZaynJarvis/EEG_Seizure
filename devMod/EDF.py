from enum import Enum
from mne.io import concatenate_raws, read_raw_edf, RawArray
from mne import pick_types, create_info


def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


Channel = enum('FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2',
               'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'FZ', 'CZ', 'PZ')


class EDF:
    false = []
    sigChan = {}
    sigFreq = {}
    sfreq = 128.0

    def __init__(self, edf):
        self.raw = read_raw_edf(edf, preload=False, stim_channel=None)
        self.raw.rename_channels(mapping=self.changeChannel())
        self.updateFreqRecord()

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
            .resample(sfreq=EDF.sfreq) \
            .filter(1, 30, method='iir')
        return self.raw

    def montageConversion(self):
        info = create_info(
            ch_names=[
                "FP1-F7", "F7-T3", "T3-T5", "T5-O1", "FP2-F8", "F8-T4",
                "T4-T6", "T6-O2", "T3-C3", "C3-CZ", "CZ-C4", "C4-T4", "FP1-F3",
                "F3-C3", "C3-P3", "P3-O1", "FP2-F4", "F4-C4", "C4-P4", "P4-02"
            ],
            ch_types='eeg',
            sfreq=EDF.sfreq)
        data = [
            self.raw.get_data(Channel.FP1)[0] - self.raw.get_data(
                Channel.F7)[0],
            self.raw.get_data(Channel.F7)[0] - self.raw.get_data(
                Channel.T3)[0],
            self.raw.get_data(Channel.T3)[0] - self.raw.get_data(
                Channel.T5)[0],
            self.raw.get_data(Channel.T5)[0] - self.raw.get_data(
                Channel.O1)[0],
            self.raw.get_data(Channel.FP2)[0] - self.raw.get_data(
                Channel.F8)[0],
            self.raw.get_data(Channel.F8)[0] - self.raw.get_data(
                Channel.T4)[0],
            self.raw.get_data(Channel.T4)[0] - self.raw.get_data(
                Channel.T6)[0],
            self.raw.get_data(Channel.T6)[0] - self.raw.get_data(
                Channel.O2)[0],
            self.raw.get_data(Channel.T3)[0] - self.raw.get_data(
                Channel.C3)[0],
            self.raw.get_data(Channel.C3)[0] - self.raw.get_data(
                Channel.CZ)[0],
            self.raw.get_data(Channel.CZ)[0] - self.raw.get_data(
                Channel.C4)[0],
            self.raw.get_data(Channel.C4)[0] - self.raw.get_data(
                Channel.T4)[0],
            self.raw.get_data(Channel.FP1)[0] - self.raw.get_data(
                Channel.F3)[0],
            self.raw.get_data(Channel.F3)[0] - self.raw.get_data(
                Channel.C3)[0],
            self.raw.get_data(Channel.C3)[0] - self.raw.get_data(
                Channel.P3)[0],
            self.raw.get_data(Channel.P3)[0] - self.raw.get_data(
                Channel.O1)[0],
            self.raw.get_data(Channel.FP2)[0] - self.raw.get_data(
                Channel.F4)[0],
            self.raw.get_data(Channel.F4)[0] - self.raw.get_data(
                Channel.C4)[0],
            self.raw.get_data(Channel.C4)[0] - self.raw.get_data(
                Channel.P4)[0],
            self.raw.get_data(Channel.P4)[0] - self.raw.get_data(Channel.O2)[0]
        ]
        return RawArray(data, info)

    def changeChannel(self):
        ch = {}
        for i in self.raw.info['ch_names']:
            try:
                ch[i] = i.split(' ')[1].split('-')[0]
            except Exception:
                pass
        return ch

    def updateFreqRecord(self):
        EDF.sigFreq[self.raw.info['sfreq']] = EDF.sigFreq.get(
            self.raw.info['sfreq'], 0) + 1
        return self.raw.info['sfreq']

    def saveFile(self, rawData, fileName):
        rawData.save(fileName)
