import sys
import json
from devMod import EDF, DataManifest, path

if sys.argv[1] == 'prod':
    cropEnd = True
    db = 'original_data_manifest/Temple_University_Hospital_EEG'
    DataManifest.setFolder('trainSet')
elif sys.argv[1] == 'test':
    cropEnd = False
    db = 'original_data_manifest/dev_test'
    DataManifest.setFolder('testSet')

with open(f'{db}.json') as f:
    data = json.load(f)
    DataManifest.buildDir()
    for channel in path:
        # Nspatients = data[channel]['noSeizure']
        # for p in Nspatients:
        #     for edf in p['fileNames']:
        #         edfRecord = EDF(edf)
        #         pass
        Spatients = data[channel]['seizure']
        for p in Spatients:
            for session in p['sessions']:
                manifest = DataManifest(session["edf"].split("/")[-1],
                                        session['seizure']['seizureType'])

                edfRecord = EDF(session['edf'])

                manifest.freq = edfRecord.updateFreqRecord()
                manifest.writeToManifest()
                edfRecord.loadData(session['seizure']['start'],
                                   session['seizure']['stop'])
                edfRecord.saveFile(edfRecord.montageConversion(),
                                   manifest.fileName)
