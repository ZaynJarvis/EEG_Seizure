import json
# commonChannel = ['FP1', 'F7', 'T3', 'T5', 'O1', 'FP2', 'F8', 'T4', 'T6',
#                  'O2', 'C3', 'CZ', 'C4', 'A1', 'F3', 'P3', 'F4', 'P4']

# commonChannel = ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'A1',
#                  'A2', 'FZ', 'CZ', 'PZ', 'ROC', 'LOC', 'EKG1', 'EMG-REF', '26', '27', '28', '29', '30', 'T1', 'T2', 'PHOTIC-REF', 'IBI', 'BURSTS', 'SUPPR']

# with open('channels.json') as f:
#     data = json.load(f)
#     k = list(data.keys())
#     for i in k:
#         test = ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8', 'T3', 'T4', 'T5',
#                 'T6', 'FZ', 'CZ', 'PZ']

#         for t in i.strip("(").strip(")").split(','):
#             for t0 in test:
#                 if t0 in t:
#                     test.remove(t0)
#         if len(test) > 0:
#             print(test)

result = ['FP1', 'FP2', 'F3', 'F4', 'C3', 'C4', 'P3', 'P4', 'O1',
          'O2', 'F7', 'F8', 'T3', 'T4', 'T5', 'T6', 'FZ', 'CZ', 'PZ']

print(len(result))
