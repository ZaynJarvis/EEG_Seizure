from devMod import ExtraInfo


class Patient:
    countx = 0
    countn = 0
    manifest = {}
    dataset = ''

    def __init__(self, patientID, count, sessionID, EEG):
        self.count = count
        self.id = patientID
        self.fileName = None
        self.fileNameList = []
        self.info = {}
        self.info["EEG"] = EEG
        self.info["sessionID"] = sessionID
        self.info["seizureCount"] = count
        self.seizure = []
        self.noSeizure = []
        try:
            self.info["age"] = ExtraInfo.info[Patient.dataset][self.id]['age']
            self.info["gender"] = ExtraInfo.info[Patient.dataset][self.
                                                                  id]['gender']
        except Exception:
            self.info["age"] = 'unknown'
            self.info["gender"] = 'unknown'
            print(self.id)

    def addSession(self, fileName, start, stop, seizureType, edf):
        if fileName:
            self.fileName = fileName
        session = {}
        if start:
            Patient.countx += 1
            session["fileName"] = self.fileName
            session["edf"] = edf
            session["seizure"] = {}
            session["seizure"]["start"] = start
            session["seizure"]["stop"] = stop
            session["seizure"]["seizureType"] = seizureType
            self.seizure.append(session)
        else:
            self.noSeizure.append(edf)
            Patient.countn += 1

    def addInfo(self, description):
        try:
            with open(description) as f:
                content = f.read().split('HISTORY:')[-1].strip(' ')[:50]
                Patient.manifest[self.id] = Patient.manifest.get(
                    self.id, set()).union([content])
        except Exception:
            pass
