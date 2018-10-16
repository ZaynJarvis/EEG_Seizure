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

256.0 HZ: 852 samples, 400.0 HZ: 242 samples, 250.0 HZ: 440 samples, 512.0 HZ: 41 samples

250.0 Hz: 97 samples, 256.0 Hz: 542 samples, 400.0 Hz: 55 samples, 512.0 Hz: 35 samples

{'1052': {'MEDICATIONS: Depakote and Topiramate.\nINTRODUCTION'},
 '10584': {'Adult female with MRSA pneumonia, sepsis, decline '},
 '2427': {'INTRODUCTION: Long-term video EEG monitoring is pe'},
 '2500': {'This is a 16-month-old with new gait disorder and '},
 '287': {'This is a __-year-old male admitted with the diagn'},
 '3884': {'\tForty-seven-year-old male with recurrent encephal'},
 '5346': {'Mixed edema, coma, now a new EEG pattern and seizu'},
 '7555': {'\nMEDICATIONS:  Keppra.\nINTRODUCTION:  This continu'},
 '7952': {'MEDICATIONS: Keppra, At1van, Aricept and others\nHI'},
 '9231': {'Adult female with advanced dementia, schizophrenia'},
 '9455': {'Cirrhosis, stroke, new onset seizures.\nMEDICATIONS'},
 '9902': {'REASON FOR STUDY:  Seizures.\nINTRODUCTION:  Digita'}}


{'492': 5891.0, '883': 10167.0, '906': 13034.0, '2521': 4236.0, '2707': 591.0, '2806': 1360.0, '2868': 0, '2991': 3005.0, '4049': 0, '5427': 23835.0, 
'6103': 0, '6175': 0, '6440':11790.0, '6444': 2881.0, '6535': 40906.0, '6563': 448.0, '6811': 6488.0, '6904': 0, '7032': 15957.0, '7095': 21.0, '7130': 0, 
'7235': 3618.0, '7584': 332.0, '8092': 3912.0, '8295': 80990.0, '8303': 27494.0, '8444': 16282.0, '8476': 55251.0, '8480': 38600.0, '8552': 26889.0, '8608': 0,
 '8615': 1793.0, '8616': 0, '9050': 1803.0, '9104': 1501.0, '9107': 81.0, '9158': 18193.0, '9232': 11001.0, '9623': 29542.0, '9630': 145.0, '9852': 3807.0, 
 '9885': 0, '10158': 14496.0, '10418': 51778.0, '10421': 0, '10427': 0, '10489': 26606.0, '10587': 4360.0, '10591': 26316.0, '21': 0, '281': 0, '302': 628.0, 
 '473': 1224.0, '529': 2444.0, '574': 1352.0, '609': 1186.0, '775': 60.0, '820': 0, '1006': 7666.0, '1113': 0, '1116': 0, '1324': 0, '1413': 0, '1479': 0, 
 '1543': 0, '1548': 0, '1587': 1217.0, '1795': 0, '1843': 0, '2445': 531.0, '2448': 0, '2484': 323.0, '2657': 0, '3053': 0, '3208': 0, '3401': 0, '3760': 0, 
 '3884': 280.0, '3977': 0, '4126': 1202.0, '4434': 0, '4456': 0, '4473': 4033.0, '4523': 0, '4596': 0, '4892': 0, '5034': 0, '5101': 0, '5346': 984.0, '5347': 0, 
 '5371': 1196.0, '5452': 1530.0, '5672': 2080.0, '5804': 1914.0, '6083': 1344.0, '6139': 0, '6351': 0, '6413': 2795.0, '6507': 0, '6514': 35196.0, '6544': 0, 
 '7128': 4910.0, '7234': 0, '7623': 0, '7835': 0, '7952': 0, '6': 3847.0, '975': 3211.0, '1052': 1071.0, '1753': 798.0, '2427': 0, '4569': 5625.0, '5044': 1937.0, 
 '5426': 2106.0, '5512': 1403.0, '5633': 0, '6000': 2521.0, '6107': 0, '6230': 6390.0, '6251': 394.0, '6520': 2785.0, '7092': 5409.0, '7170': 2773.0, '7196': 1708.0, 
 '7793': 602.0, '7797': 2168.0, '8029': 14460.0, '9162': 9011.0}


{'6413': 2795.0, '8480': 19300.0, '5452': 765.0, '6351': 0, '5804': 957.0, '5633': 0, '5672': 1829.0, '8295': 40495.0, '8092': 3912.0, '609': 1186.0, '1006': 3833.0, 
'10418': 25889.0, '4126': 1202.0, '1479': 0, '7234': 0, '2707': 591.0, '2521': 4236.0, '9158': 18193.0, '2427': 0, '8444': 8141.0, '4569': 1875.0, '1795': 0, 
'6440': 2358.0, '775': 60.0, '5512': 1403.0, '9162': 9011.0, '6535': 20453.0, '4434': 0, '820': 0, '6811': 5275.0, '3053': 0, '1753': 798.0, '6507': 0, '6563': 448.0, 
'6': 3847.0, '6175': 0, '7092': 5409.0, '2657': 0, '5044': 1937.0, '10158': 7248.0, '7196': 1708.0, '6514': 20047.0, '302': 314.0, '6544': 0, '1587': 1217.0, 
'8552': 26889.0, '7170': 4245.0, '7835': 0, '10421': 0, '8029': 7230.0, '906': 15569.0, '3977': 0, '9232': 11001.0, '3208': 0, '8476': 18417.0, '5034': 0, 
'7584': 166.0, '2484': 323.0, '6083': 1344.0, '6251': 394.0, '2868': 2759.0, '5346': 984.0, '2991': 5411.0, '5371': 1196.0, '10587': 4360.0, '5427': 25038.0, 
'2448': 0, '6000': 2521.0, '7128': 2455.0, '6103': 2207.0, '7235': 1809.0, '975': 3211.0, '7130': 0, '6444': 2881.0, '5347': 0, '9104': 1501.0, '8608': 0, 
'6520': 2785.0, '4892': 0, '473': 1224.0, '1113': 0, '6139': 0, '5426': 2254.0, '492': 3126.0, '4596': 0, '1548': 0, '21': 0, '4473': 4033.0, '5101': 0, '281': 0, 
'9623': 29542.0, '1052': 1071.0, '1324': 0, '8616': 0, '9107': 81.0, '7623': 0, '9050': 1803.0, '6230': 9429.0, '7095': 21.0, '9852': 3807.0, '3401': 0, '883':2722.0, 
'2445': 531.0, '3760': 0, '4456': 0, '2806': 1360.0, '1843': 0, '9630': 145.0, '8303': 13747.0, '10427': 0, '3884': 280.0, '6107': 0, '8615': 1793.0, '7793': 602.0, 
'4049': 0, '9885': 0, '1413': 0, '10591': 13158.0, '6904': 0, '7797': 2168.0, '7032': 5319.0, '574': 1352.0, '1116': 0, '1543': 1739.0, '7952': 0, '529': 2467.0, 
'10489': 26606.0, '4523': 1479.0}
['6351', '5633', '1479', '7234', '2427', '1795', '4434', '820', '3053', '6507', '6175', '2657', '6544', '7835', '10421', '3977', '3208', '5034', '2448', 
'7130', '5347', '8608', '4892', '1113', '6139', '4596', '1548', '21', '5101', '281', '1324', '8616', '7623', '3401', '3760', '4456', '1843', '10427', '6107',
 '4049', '9885', '1413', '6904', '1116', '7952']
 45

{'8460': 10195.0, '5943': 4066.0, '10106': 5228.0, '9866': 7989.0, '9697': 13490.0, '10639': 5968.0, '8479': 3132.0, '2297': 1211.0, '5479': 7297.0, '1981': 3693.0,
 '675': 0, '4671': 13309.0, '9578': 87778.0, '10547': 0, '258': 20.0, '6986': 1249.0, '9570': 8857.0, '10062': 3632.0, '3281': 1457.0, '1770': 2730.0, '8512': 11364.0,
  '10861': 0, '4151': 1189.0,'5625': 1280.0, '10022': 22987.0, '8889': 8126.0, '4087': 2401.0, '8606': 0, '1027': 1258.0, '8453': 27477.0, '5213': 0, '9839': 18832.0,
   '9842': 901.0, '8174': 1454.0, '3635': 0,'6546': 16694.0, '3306': 0, '1984': 0, '8544': 25509.0}
['675', '10547', '10861', '8606', '5213', '3635', '3306', '1984']
8