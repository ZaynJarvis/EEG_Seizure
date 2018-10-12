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


{'EEG FP1-REF': 'FP1', 'EEG FP2-REF': 'FP2', 'EEG F3-REF': 'F3', 'EEG F4-REF': 'F4',
 'EEG C3-REF': 'C3', 'EEG C4-REF': 'C4', 'EEG P3-REF': 'P3', 'EEG P4-REF': 'P4',
 'EEG O1-REF': 'O1', 'EEG O2-REF': 'O2', 'EEG F7-REF': 'F7', 'EEG F8-REF': 'F8',
 'EEG T3-REF': 'T3', 'EEG T4-REF': 'T4', 'EEG T5-REF': 'T5', 'EEG T6-REF': 'T6',
 'EEG A1-REF': 'A1', 'EEG A2-REF': 'A2', 'EEG FZ-REF': 'FZ', 'EEG CZ-REF': 'CZ',
 'EEG PZ-REF': 'PZ', 'EEG ROC-REF': 'ROC', 'EEG LOC-REF': 'LOC', 'EEG EKG1-REF':
 'EKG1', 'EEG 26-REF': '26', 'EEG 27-REF': '27', 'EEG 28-REF': '28',
 'EEG 29-REF': '29', 'EEG 30-REF': '30', 'EEG T1-REF': 'T1', 'EEG T2-REF': 'T2',
 'STI 014': '014', 'EEG EKG-REF': 'EKG', 'EEG SP1-REF': 'SP1', 'EEG SP2-REF': 'SP2',
 'EEG LUC-REF': 'LUC', 'EEG RLC-REF': 'RLC', 'EEG RESP1-REF': 'RESP1', 'EEGRESP2-REF':
 'RESP2', 'EEG 31-REF': '31', 'EEG 32-REF': '32', 'EEG C3P-REF': 'C3P', 'EEG C4P-REF':
 'C4P', 'EEG OZ-REF': 'OZ', 'ECG EKG-REF': 'EKG',
    'PULSE RATE': 'RATE', 'EEG FP1-LE': 'FP1', 'EEG FP2-LE': 'FP2', 'EEG F3-LE': 'F3',
 'EEG F4-LE': 'F4', 'EEG C3-LE': 'C3', 'EEG C4-LE': 'C4', 'EEG A1-LE': 'A1',
     'EEG A2-LE': 'A2', 'EEG P3-LE': 'P3', 'EEG P4-LE': 'P4', 'EEG O1-LE': 'O1',
     'EEG O2-LE': 'O2', 'EEG F7-LE': 'F7', 'EEG F8-LE': 'F8', 'EEG T3-LE': 'T3',
     'EEG T4-LE': 'T4', 'EEG T5-LE': 'T5', 'EEG T6-LE': 'T6', 'EEG FZ-LE': 'FZ',
     'EEG CZ-LE': 'CZ', 'EEG PZ-LE': 'PZ', 'EEG OZ-LE': 'OZ', 'EEG PG1-LE': 'PG1',
     'EEG PG2-LE': 'PG2', 'EEG EKG-LE': 'EKG', 'EEG SP2-LE': 'SP2', 'EEG SP1-LE': 'SP1',
 'EEG RLC-LE': 'RLC', 'EEG LUC-LE': 'LUC', 'EEG 30-LE': '30', 'EEG T1-LE': 'T1',
 'EEG T2-LE': 'T2', 'EEG 26-LE': '26', 'EEG 27-LE': '27', 'EEG 28-LE': '28',
 'EEG 29-LE': '29', 'EEG 31-LE': '31', 'EEG 32-LE': '32', 'PHOTIC PH': 'PH',
 'EEG 23-LE': '23', 'EEG 24-LE': '24', 'EEG 20-REF': '20', 'EEG 21-REF': '21',
 'EEG 22-REF': '22', 'EEG 23-REF': '23', 'EEG 24-REF': '24', 'EEG 25-REF': '25'}


{'EEG FP1-REF': 'FP1', 'EEG FP2-REF': 'FP2', 'EEG F3-REF': 'F3', 'EEG F4-REF': 'F4',
 'EEG C3-REF': 'C3', 'EEG C4-REF': 'C4', 'EEG P3-REF': 'P3', 'EEG P4-REF': 'P4',
 'EEG O1-REF': 'O1', 'EEG O2-REF': 'O2', 'EEG F7-REF': 'F7', 'EEG F8-REF': 'F8',
 'EEG T3-REF': 'T3', 'EEG T4-REF': 'T4', 'EEG T5-REF': 'T5', 'EEG T6-REF': 'T6',
 'EEG A1-REF': 'A1', 'EEG A2-REF': 'A2', 'EEG FZ-REF': 'FZ', 'EEG CZ-REF': 'CZ',
 'EEG PZ-REF': 'PZ', 'EEG ROC-REF': 'ROC', 'EEG LOC-REF': 'LOC', 'EEG EKG1-REF':
 'EKG1', 'EEG 26-REF': '26', 'EEG 27-REF': '27', 'EEG 28-REF': '28',
 'EEG 29-REF': '29', 'EEG 30-REF': '30', 'EEG T1-REF': 'T1', 'EEG T2-REF': 'T2',
 'STI 014': '014', 'EEG EKG-REF': 'EKG', 'EEG SP1-REF': 'SP1', 'EEG SP2-REF': 'SP2',
 'EEG LUC-REF': 'LUC', 'EEG RLC-REF': 'RLC', 'EEG RESP1-REF': 'RESP1', 'EEGRESP2-REF':
 'RESP2', 'EEG 31-REF': '31', 'EEG 32-REF': '32', 'EEG C3P-REF': 'C3P', 'EEG C4P-REF':
 'C4P', 'EEG OZ-REF': 'OZ', 'ECG EKG-REF': 'EKG',
    'PULSE RATE': 'RATE', 'EEG FP1-LE': 'FP1', 'EEG FP2-LE': 'FP2', 'EEG F3-LE': 'F3',
 'EEG F4-LE': 'F4', 'EEG C3-LE': 'C3', 'EEG C4-LE': 'C4', 'EEG A1-LE': 'A1',
     'EEG A2-LE': 'A2', 'EEG P3-LE': 'P3', 'EEG P4-LE': 'P4', 'EEG O1-LE': 'O1',
     'EEG O2-LE': 'O2', 'EEG F7-LE': 'F7', 'EEG F8-LE': 'F8', 'EEG T3-LE': 'T3',
     'EEG T4-LE': 'T4', 'EEG T5-LE': 'T5', 'EEG T6-LE': 'T6', 'EEG FZ-LE': 'FZ',
     'EEG CZ-LE': 'CZ', 'EEG PZ-LE': 'PZ', 'EEG OZ-LE': 'OZ', 'EEG PG1-LE': 'PG1',
     'EEG PG2-LE': 'PG2', 'EEG EKG-LE': 'EKG', 'EEG SP2-LE': 'SP2', 'EEG SP1-LE': 'SP1',
 'EEG RLC-LE': 'RLC', 'EEG LUC-LE': 'LUC', 'EEG 30-LE': '30', 'EEG T1-LE': 'T1',
 'EEG T2-LE': 'T2', 'EEG 26-LE': '26', 'EEG 27-LE': '27', 'EEG 28-LE': '28',
 'EEG 29-LE': '29', 'EEG 31-LE': '31', 'EEG 32-LE': '32', 'PHOTIC PH': 'PH',
 'EEG 23-LE': '23', 'EEG 24-LE': '24', 'EEG 20-REF': '20', 'EEG 21-REF': '21',
 'EEG 22-REF': '22', 'EEG 23-REF': '23', 'EEG 24-REF': '24', 'EEG 25-REF': '25'}


# train
# -- seizure --
distribution: {256.0: 117, 400.0: 127, 250.0: 165, 512.0: 3}
count: 412
# -- no seizure --
distribution: {250.0: 440, 400.0: 242, 256.0: 852, 512.0: 41}
count: 1575
# -- total --
distribution: {256.0: 852, 400.0: 242, 250.0: 440, 512.0: 41}
count: 1987

# test
# -- seizure --
distribution: {250.0: 42, 256.0: 209, 400.0: 33}
count: 284
# -- no seizure --
distribution: {400.0: 55, 250.0: 97, 512.0: 35, 256.0: 542}
count: 729
# -- total --
distribution: {250.0: 97, 256.0: 542, 400.0: 55, 512.0: 35}
count: 1013