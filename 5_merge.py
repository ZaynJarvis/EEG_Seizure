from devMod import Injector

dirName = input('Merge data directory: \ne.g. \'./train_5s_seg\'\n')


def seizureMerge(dirName):
    merge_of_seizure = []
    count = 0
    subfolders = os.listdir(dirName)
    for folder in subfolders:
        files = os.listdir('{}/{}'.format(dirName, folder))
        for fileItem in files:
            raw = mne.io.read_raw_fif('{}/{}/{}'.format(
                dirName, folder, fileItem))
            merge_of_seizure.append(raw)
            count += 1
    edfRecord.saveFile(
        mne.concatenate_raws(merge_of_seizure),
        '{}/merged_seizure.fif'.format(dirName))
    print(f"You have {count} seizure segments merged.")
    return count


def noseizureMerge(dirName, count):
    merge_of_noseizure = []
    files = os.listdir('{}/{}'.format(dirName, 'noseizure'))
    random.shuffle(files)[:count]
    for fileItem in files:
        raw = mne.io.read_raw_fif('{}/{}/{}'.format(dirName, 'noseizure',
                                                    fileItem))
        merge_of_noseizure.append(raw)
    edfRecord.saveFile(
        mne.concatenate_raws(merge_of_noseizure),
        '{}/merged_noseizure.fif'.format(path))
    print(f"You have {count} noseizure segments merged.")


count = seizureMerge(dirName)
noseizureMerge(dirName, count)
