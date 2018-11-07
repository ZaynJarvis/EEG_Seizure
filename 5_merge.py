from mne.io import concatenate_raws, read_raw_edf, RawArray
import os
import random

dirname = input(
    'specify the root directory for data merge. e.g. ./train_5s_seg\n')
path = './{}'.format(dirname)
subfolders = os.listdir(path)
subfolders.remove('noseizure')
count = 0
merge_of_seizure = []
merge_of_noseizure = []

# seizure merge
for folder in subfolders:
    files = os.listdir('{}/{}'.format(path, folder))
    for fileItem in files:
        raw = mne.io.read_raw_fif('{}/{}/{}'.format(path, folder, fileItem))
        merge_of_seizure.append([raw])
        count += 1

# noseizure merge
files = os.listdir('{}/{}'.format(path, 'noseizure'))
random.shuffle(files)[:count]
for fileItem in files:
    raw = mne.io.read_raw_fif('{}/{}/{}'.format(path, 'noseizure', fileItem))
    merge_of_seizure.append([raw])

info = create_info(
    ch_names=EDF.montageConversionChannels, ch_types='eeg', sfreq=EDF.sfreq)

edfRecord.saveFile(
    RawArray(merge_of_seizure, info), '{}/merged_seizre.fif'.format(path))
edfRecord.saveFile(
    RawArray(merge_of_noseizure, info), '{}/merged_noseizre.fif'.format(path))
