import os
import json
__import__('0_getData')

print("Select the way to copy files")
while True:
  selection = input(\
'''
Case 1: all raw edf files
Case 2: edf files with / without seizure 
Case 3: edf files with respect to seizure types

''')
  if selection in ['1', '2', '3']:
    break

if selection in ['2', '3']:
  seizureFolder = input("source seizure folder name?")
  noseizureFolder = input("source non-seizure folder name?")

distSeizureFolder = "./seizure/"
distNoseizureFolder = "./no-seizure/"
root = os.getcwd()

def noSeperate():
  folder = "edfFiles"
  try:
    os.mkdir(folder)
  except Exception:
    pass
  with open(f'./{Injector.location}.json') as f:
    data = json.load(f)
    for channel in path:
        patients = data[channel]['seizure']
        for patient in patients:
            for session in patient['sessions']:
              fileName = session["edf"].split("/")[-1]
              session['seizure']['seizureType']
              os.rename(os.path.join(root, session["edf"]), os.path.join(root, folder, fileName))
        patients = data[channel]['noseizure']
        for patient in patients:
            for _fileName in files = patient["fileNames"]:
              fileName = _fileName.split("/")[-1]
              os.rename(os.path.join(root, session["edf"]), os.path.join(root, folder, fileName))

def seperateOnSeizure():
  try:
    os.mkdir(folder)
  except Exception:
    pass
  with open(f'./{Injector.location}.json') as f:
    data = json.load(f)
    for channel in path:
        patients = data[channel]['seizure']
        for patient in patients:
            for session in patient['sessions']:
              fileName = session["edf"].split("/")[-1]
              session['seizure']['seizureType']
              os.rename(os.path.join(root, session["edf"]), os.path.join(root, 'seizure', fileName))
        patients = data[channel]['noseizure']
        for patient in patients:
            for _fileName in files = patient["fileNames"]:
              fileName = _fileName.split("/")[-1]
              os.rename(os.path.join(root, session["edf"]), os.path.join(root, 'noseizure', fileName))


def seperateOnSeizure():
  try:
    os.mkdir(folder)
  except Exception:
    pass
  with open(f'./{Injector.location}.json') as f:
    data = json.load(f)
    for channel in path:
        patients = data[channel]['seizure']
        for patient in patients:
            for session in patient['sessions']:
              fileName = session["edf"].split("/")[-1]
              seizureType = session['seizure']['seizureType']
              path = os.path.join(root, 'seizure', seizureType)
              if not os.path.exists(path):
                os.mkdir(path)
              os.rename(os.path.join(root, session["edf"]), os.path.join(path, fileName))
        patients = data[channel]['noseizure']
        for patient in patients:
            for _fileName in files = patient["fileNames"]:
              fileName = _fileName.split("/")[-1]
              os.rename(os.path.join(root, session["edf"]), os.path.join(root, 'noseizure', fileName))

if selection == '1':
  noSeperate()
elif selection == '2':
  seperateOnSeizure()
elif selection == '3':
  seperateOnType()
