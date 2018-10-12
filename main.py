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
                                        session['seizure']['seizureType'],
                                        p['info']['age'], p['info']['gender'])
                seizureDuration = str(
                    float(session['seizure']['stop']) -
                    float(session['seizure']['start'])) + 's'

                for i in range(
                        int((float(session['seizure']['stop']) - float(
                            session['seizure']['start'])) // 5)):
                    edfRecord = EDF(session['edf'])
                    edfRecord.loadData(
                        str(float(session['seizure']['start']) + 5 * i),
                        str(float(session['seizure']['start']) + 5 * (i + 1)))
                    manifest.seg = i + 1
                    manifest.seizureDuration = seizureDuration
                    manifest.freq = edfRecord.updateFreqRecord()
                    manifest.generateRecord()
                    manifest.writeToManifest()

                    edfRecord.saveFile(edfRecord.montageConversion(),
                                       manifest.fileName)
