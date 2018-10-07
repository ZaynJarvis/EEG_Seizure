
from mne import Epochs, pick_types, find_events
from mne.io import concatenate_raws, read_raw_edf

raw = read_raw_edf('./edf/train/03_tcp_ar_a/008/00000883/s012_2010_09_13/00000883_s012_t001.edf',
                   preload=True, stim_channel='auto')
ch = {}
x = raw.info['ch_names']
for i in x:
    try:
        ch[i] = i.split(' ')[1].split('-')[0]
    except Exception:
        pass

raw.rename_channels(mapping=ch)
x = raw.info['ch_names']

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
(raw.info)
# fig = raw.copy() \
#     .pick_types(meg=False, eeg=True) \
#     .resample(sfreq=128) \
#     .filter(1, 30) \
#     .crop(6.2825, 35.8875) \
#     .save()
