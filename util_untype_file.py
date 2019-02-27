import os
# seizureFolder = input("seizure folder name?")
# noseizureFolder = input("seizure folder name?")
seizureFolder = "test/a"
noseizureFolder = "test/k"

distSeizureFolder = "./seizure/"
distNoseizureFolder = "./no-seizure/"

if not os.path.exists(distSeizureFolder):
  os.mkdir(distSeizureFolder)
if not os.path.exists(distNoseizureFolder):
  os.mkdir(distNoseizureFolder)

for folders in [[distSeizureFolder, seizureFolder], [distNoseizureFolder, noseizureFolder]]:
  for root, dirs, files in os.walk("./" + folders[1], topdown=False):
    for name in files:
      os.rename(os.path.join(root, name), folders[0] + name)
