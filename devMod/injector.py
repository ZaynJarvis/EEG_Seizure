class Injector:
    @classmethod
    def datasetPrompt(cls):
        chooseSet = input("Which data set are you using?\n" +
                          "a). For Training Dataset;\n" +
                          "b). For Testing Dataset.\n")

        while True:
            if chooseSet.lower() == 'a':
                cls.dataset = 'train'
                cls.location = 'original_data_manifest/Temple_University_Hospital_EEG'
                cls.folder = 'trainSet'
                cls.fileNameCrop = 3
                break
            elif chooseSet.lower() == 'b':
                cls.dataset = 'test'
                cls.location = 'original_data_manifest/dev_test'
                cls.folder = 'testSet'
                cls.fileNameCrop = 2
                break
            else:
                print('Input not valid...')
                chooseSet = input(
                    'Which data set are you using?\nType:\na). For Training Dataset;\nb). For Testing Dataset\n'
                )

    @classmethod
    def timeWindowPrompt(cls):
        cls.timeWindow = int(input("Set your time window?\n"))

    @classmethod
    def filterPrompt(cls):
        setFilter = input(
            "Set your filter:\n" +
            "a). Butterworth bandpass filter between 1 and 30 Hz;\n" +
            "b). IIR notch filter of 60 Hz and IIR high pass filter of 1 Hz.\n"
        )
        if setFilter.lower() == 'a':
            cls.filter = 'bandpass'
        elif setFilter.lower() == 'b':
            cls.filter = 'notch'
        else:
            print('Input not valid...')
            setFilter = input(
                "Set your filter:\n" +
                "a). Butterworth bandpass filter between 1 and 30 Hz;\n" +
                "b). IIR notch filter of 60 Hz and IIR high pass filter of 1 Hz.\n"
            )
