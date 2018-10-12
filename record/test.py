
from mne import Epochs, pick_types, find_events
from mne.io import concatenate_raws, read_raw_edf, read_raw_fif

raw = read_raw_fif('./testDir/00000492_s003_t000raw.fif',
                   preload=True)

# raw = read_raw_edf('./edf/train/03_tcp_ar_a/008/00000883/s012_2010_09_13/00000883_s012_t001.edf',
#                    preload=True, stim_channel='auto')
x = raw.info['ch_names']
print(x)
print(raw)
# raw.filter(7., 30., fir_design='firwin', skip_by_annotation='edge')

# picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False,
#                    exclude='bads')
# events = find_events(raw, shortest_event=0)

# epochs = Epochs(raw, events, proj=True, picks=picks,
#                 baseline=None, preload=True)
# epochs_train = epochs.copy().crop(tmin=1., tmax=2.)
# labels = epochs.events[:, -1] - 2

# print(raw.info)
# print(labels)

# fig = raw.copy() \
#     .pick_types(meg=False, eeg=True) \
#     .resample(sfreq=100) \
#     .filter(1, 30) \
#     .plot()
# fig = raw.copy() \
#     .pick_types(meg=False, eeg=True) \
#     .resample(sfreq=128) \
#     .filter(1, 30) \
#     .crop(6.2825, 35.8875) \
#     .save()
