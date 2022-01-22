from reduction import reduction
from clause import clause
import sys
import json

### JSON READING ###

file = sys.argv[1]
with open('./' + file, 'r') as f:
  dataIn = json.loads(f.read())

vbles = []
for i in range(dataIn["numVbles"]):
  vble = "z" + str(i + 1)
  vbles.append(vble)

clausulas = []
clausulasNegation = []
clausulasKeys = list(dataIn["clausulas"].keys())
for i in range(dataIn["numClausulas"]):
  vblesClausulas = list(dataIn["clausulas"][clausulasKeys[i]].keys())
  vectorNeg = []
  vector = []
  for j in vblesClausulas:
    vectorNeg.append(dataIn["clausulas"][clausulasKeys[i]][j])
    vector.append(int(j))
  clausulasNegation.append(vectorNeg)
  clausulas.append(vector)

asignation = dataIn["asignacion"]
clausulasObj = []
for i in range(dataIn["numClausulas"]):
  clausulasObj.append(clause(clausulasNegation[i], clausulas[i]))

### Reduction ###
reducter = reduction(vbles, clausulasObj, asignation)
valid = reducter.to3DM()
if not valid:
  print("Asignation chosen does not satisfy the clauses.")
else: 
  reducter.showResult()
  
  ### Result to JSON ###
  W = []
  X = []
  Y = []

  for i in range(len(reducter.matching)):
    W.append(reducter.matching[i][0])
    X.append(reducter.matching[i][1])
    Y.append(reducter.matching[i][2])

  dataOut = {
    "W" : W,
    "X" : X,
    "Y" : Y
  }

  jsonOut = json.dumps(dataOut)

  with open('3DM.json', 'w') as outfile:
    outfile.write(jsonOut)
