channels = {
    "01_tcp_ar", "02_tcp_le", "03_tcp_ar_a"
}

expected_TCP_montage_transform = ["FP1-F7", "F7-T3", "T3-T5", "T5-O1", "FP2-F8", "F8-T4",
                                  "T4-T6",
                                  "T6-O2",
                                  "A1-T3", "T3-C3", "C3-CZ",
                                  "CZ-C4", "C4-T4", "T4-A2", "FP1-F3", "F3-C3", "C3-P3", "P3-O1", "FP2-F4", "F4-C4",
                                  "C4-P4", "P4-O2"]


seiTypes = [['GNSZ', 'CPSZ', 'TCSZ', 'FNSZ', 'TNSZ', 'ABSZ', 'SPSZ'],
            ['CPSZ', 'FNSZ', 'GNSZ', 'TCSZ', 'ABSZ', 'MYSZ'],
            ['CPSZ', 'FNSZ', 'GNSZ', 'TCSZ']]

seiTypesFlat = ['GNSZ', 'CPSZ', 'TCSZ', 'FNSZ', 'TNSZ', 'ABSZ', 'SPSZ', 'MYSZ']

seiT = [
    {'GNSZ': 68, 'CPSZ': 62, 'TCSZ': 9, 'FNSZ': 273,
        'TNSZ': 16, 'ABSZ': 1, 'SPSZ': 40},
    {'CPSZ': 71, 'FNSZ': 182, 'GNSZ': 69, 'TCSZ': 14, 'ABSZ': 47, 'MYSZ': 1},
    {'CPSZ': 123, 'FNSZ': 227, 'GNSZ': 26, 'TCSZ': 1}
]

channel_config = [

    ([29, 151, 144, 6, 24, 19, 16, 21, 55, 1]),
    ([268, 18, 77, 19, 3]),
    ([224, 153, 1])

]

TCP_montage = ['FP1-F7', 'F7-T3', 'T3-T5', 'T5-O1', 'FP2-F8', 'F8-T4', 'T4-T6', 'T6-O2', 'T3-C3',
               'C3-CZ', 'CZ-C4', 'C4-T4', 'FP1-F3', 'F3-C3', 'C3-P3', 'P3-O1', 'FP2-F4', 'F4-C4', 'C4-P4', 'P4-O2']


unavailable = \
    [
        ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF', 'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF',
         'EEG F7-REF', 'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF',
         'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG 20-REF', 'EEG 21-REF', 'EEG 22-REF', 'EEG 23-REF', 'EEG 24-REF', 'EEG 25-REF', 'EEG 26-REF',
         'EEG 27-REF', 'EEG 28-REF', 'EEG 29-REF', 'EEG 30-REF', 'EEG 31-REF', 'EEG 32-REF'),  # 224 lost [A1,A2]

        ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF', 'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF',
         'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF',
         'EEG T1-REF', 'EEG T2-REF', 'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG EKG1-REF', 'EEG C3P-REF', 'EEG C4P-REF', 'EEG SP1-REF', 'EEG SP2-REF', 'EMG-REF',
         'EEG 29-REF', 'EEG 30-REF', 'EEG 31-REF', 'EEG 32-REF', 'IBI', 'BURSTS', 'SUPPR'),  # 153 lost [A1,A2]

        ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF', 'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF',
         'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF', 'EEG T1-REF', 'EEG T2-REF', 'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG EKG1-REF',
         'EMG-REF', 'IBI', 'BURSTS', 'SUPPR')  # 1 lost [A1,A2]
    ]

# edfReader = pyedflib.EdfReader(
#     './edf/train/01_tcp_ar/000/00000077/s003_2010_01_21/00000077_s003_t000.edf')
# n = edfReader.signals_in_file
# signal_labels = edfReader.getSignalLabels()
# duration = int((float(session['seizure']['stop']) -
#                 float(session['seizure']['start'])) * 250 + 1)
# print(signal_labels)
# sigbufs = np.zeros((n, edfReader.getNSamples()[0]))
# sigbufs = np.zeros((n, duration))
# for i in np.arange(n):
#     sigbufs[i, :] = edfReader.readSignal(i)[int(
#         float(session['seizure']['start'])*250): int(
#         float(session['seizure']['start'])*250) + duration]
#     fileName = session['edf'].split(
#         "/")[-1].replace('edf', 'csv')
#     np.savetxt(
#         f'./gen/train/{channel}/{fileName}', sigbufs, delimiter=",")


# error in test set
[
    ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF',
     'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF', 'EEG F8-REF', 'EEG T3-REF',
     'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF', 'EEG A1-REF', 'EEG A2-REF', 'EEG FZ-REF', 'EEG CZ-REF',
     'EEG PZ-REF', 'EEG ROC-REF', 'EEG LOC-REF', 'EEG EKG1-REF', 'EMG-REF', 'EEG 26-REF', 'EEG 27-REF',
     'EEG 28-REF', 'EEG 29-REF', 'EEG 30-REF', 'EEG T1-REF', 'EEG T2-REF', 'PHOTIC-REF', 'IBI',
     'BURSTS', 'SUPPR'),  # 288
    ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF',
     'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF', 'EEG F8-REF', 'EEG T3-REF',
     'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF', 'EEG A1-REF', 'EEG A2-REF', 'EEG FZ-REF', 'EEG CZ-REF',
     'EEG PZ-REF', 'EEG ROC-REF', 'EEG LOC-REF', 'EEG EKG1-REF', 'EEG T1-REF', 'EEG T2-REF',
     'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR'),  # 215
    ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF', 'EEG P3-REF',
     'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF', 'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF',
     'EEG T5-REF', 'EEG T6-REF', 'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG EKG-REF', 'EEG A1-REF',
     'EEG A2-REF', 'EEG T1-REF', 'EEG T2-REF', 'EEG SP1-REF', 'EEG SP2-REF', 'EEG LUC-REF', 'EEG RLC-REF',
     'EEG RESP1-REF', 'EEG RESP2-REF', 'EEG 31-REF', 'EEG 32-REF'),  # 86
    ('EEG FP1-REF', 'EEG FP2-REF', 'EEG F3-REF', 'EEG F4-REF', 'EEG C3-REF', 'EEG C4-REF',
     'EEG P3-REF', 'EEG P4-REF', 'EEG O1-REF', 'EEG O2-REF', 'EEG F7-REF',
     'EEG F8-REF', 'EEG T3-REF', 'EEG T4-REF', 'EEG T5-REF', 'EEG T6-REF', 'EEG T1-REF', 'EEG T2-REF',
     'EEG FZ-REF', 'EEG CZ-REF', 'EEG PZ-REF', 'EEG EKG1-REF', 'EMG-REF', 'EEG A1-REF', 'EEG A2-REF',
     'EEG 31-REF', 'EEG 32-REF', 'IBI', 'BURSTS', 'SUPPR')  # 48
]


['F7', 'T5', 'FP2', 'T4', 'O2', 'CZ', 'F3', 'F4']
['T5', 'T4', 'CZ', 'F4']
['T4', 'F4']
['F4']


# filter
['EMG-REF', '26', '27', '28', '29', '30']
['ROC', 'LOC', 'EKG1', 'EMG-REF', '26', '27', '28',
    '29', '30', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['ROC', 'LOC', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30']
['ROC', 'LOC', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['26', '27', '28', '29', '30']
['ROC', 'LOC', 'EKG1', 'EMG-REF', '26', '27',
    '28', '29', '30', 'T1', 'T2', 'PHOTIC-REF']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30']
['ROC', 'LOC', '26', '27', '28', '29', '30']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['ROC', 'LOC', 'EKG1', 'EMG-REF', '26', '27', '28',
    '29', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['ROC', 'LOC', 'EKG1', 'EMG-REF', 'T1', 'T2',
    'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['ROC', 'LOC', 'EKG1', 'EMG-REF', '26', '27',
    'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['ROC', 'LOC', 'EKG1', 'EMG-REF', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['ROC', 'LOC', 'EKG1', 'EMG-REF', 'T1', 'T2',
    'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['A1', 'A2', 'ROC', 'LOC', 'EKG1', 'EMG-REF', 'T1',
    'T2', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']
['A1', 'A2', 'ROC', 'LOC', '26', '27', '28', 'PHOTIC-REF']
['A1', 'A2', 'ROC', 'LOC', '26', '27', '28', '29', '30', 'PHOTIC-REF']
['A1', 'A2', 'ROC', 'LOC', 'EMG-REF', '26', '27', '28', '29', '30', 'PHOTIC-REF']
