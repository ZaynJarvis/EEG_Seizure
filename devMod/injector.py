class Injector:
    timeWindow = 0
    version = 'v1.5'
    @classmethod
    def datasetPrompt(cls):
        chooseSet = input("Which data set are you using?\n" +
                          "a). For Training Dataset;\n" +
                          "b). For Testing Dataset.\n")
        while True:
            if chooseSet.lower() == 'a':
                cls.dataset = 'train'
                cls.location = 'original_data_manifest/train-' + cls.version
                cls.folder = 'trainSet'
                cls.fileNameCrop = 3
                break
            elif chooseSet.lower() == 'b':
                cls.dataset = 'test'
                cls.location = 'original_data_manifest/test-' + cls.version
                cls.folder = 'testSet'
                cls.fileNameCrop = 2
                break
            else:
                print('Input not valid...')
                chooseSet = input(
                    'Which data set are you using?\nType:\na). For Training Dataset;\nb). For Testing Dataset\n'
                )

    @classmethod
    def preprocessPrompt(cls):
        preProcessOption = input("Preprocess the EDF signals?\n(Y/N)?\n")
        while True:
            if preProcessOption.lower() == 'y':
                cls.preprocess = True
                break
            elif preProcessOption.lower() == 'n':
                cls.preprocess = False
                break
            else:
                print('Input not valid...')
                preProcessOption = int(
                    input("Set montage conversion?\n(Y/N)?\n"))

    @classmethod
    def setMontageConversionPrompt(cls):
        setMontage = input("Set montage conversion?\n(Y/N)?\n")
        while True:
            if setMontage.lower() == 'y':
                cls.performConversion = True
                break
            elif setMontage.lower() == 'n':
                cls.performConversion = False
                break
            else:
                print('Input not valid...')
                setMontage = input("Set montage conversion?\n(Y/N)?\n")

    @classmethod
    def timeWindowPrompt(cls):
        cls.timeWindow = int(input("Set your time window?\n"))
        while cls.timeWindow <= 0:
            cls.timeWindow = int(input("Please set time window > 0.\n"))

    @classmethod
    def filterPrompt(cls):
        setFilter = input(
            "Set your filter:\n" +
            "a). Butterworth bandpass filter between 1 and 32 Hz;\n" + \
            "b). IIR notch filter of 50 Hz and 60 Hz and IIR high pass filter of 1 Hz;\n"
            )
        while True:
            if setFilter.lower() == 'a':
                cls.filter = 'bandpass'
                break
            elif setFilter.lower() == 'b':
                cls.filter = 'notch'
                break
            elif setFilter.lower() == 'c':
                cls.filter = 'none'
                break
            else:
                print('Input not valid...')
                setFilter = input(
                    "Set your filter:\n" +
                    "a). Butterworth bandpass filter between 1 and 30 Hz;\n" +
                    "b). IIR notch filter of 60 Hz and IIR high pass filter of 1 Hz.\n"
                )
    
    @classmethod
    def mergePrompt(cls):
        merge = input("Do you want to merge the data?\n(Y/N)?\n")
        while True:
            if merge.lower() == 'y':
                cls.mergeFiles = True
                break
            elif merge.lower() == 'n':
                cls.mergeFiles = False
                break
            else:
                print('Input not valid...')
                merge = input("Do you want to merge the data?\n(Y/N)?\n")
