from starTSFO import starTSFO
from starST import starST
from starGC import starGC
from clause import clause

class reduction:
  def __init__(self, variables, clauses, assignation):
    # 3SAT related (input).
    self.variables = variables      # Z:  [z1, z2, z3, z4, ...]
    self.clauses = clauses          # C:  [C1, C2, C3, ...]
    self.assignation = assignation  # A:  [False, True, True, False, ...]
    
    # 3DM related (output).
    self.stars = []
    self.matching  = []             # M': [[w1, x1, y1], [w2, x2, y2], ...]
    self.valid = True

  # Reduction.
  def to3DM(self):
    self.TSFO()
    self.ST()
    self.GC()
    return self.valid

  # Truth Settings and Fan Outs phase.
  def TSFO(self):
    for i in range(len(self.variables)):
      star = starTSFO(self.variables[i], i + 1, len(self.clauses))
      result = star.fanOut(self.assignation[i])
      self.stars.append(star)
      for triplet in result:
        self.matching.append(triplet)
    
  # Satisfaction Testing phase.
  def ST(self):       
    for i in range (len(self.clauses)):
      star = starST('c' + str(i + 1), self.clauses[i], self.stars)
      if not star.valid:
        self.valid = False
        break
      self.matching.append(star.triplet)
    
  # Garbage Collection phase.
  def GC(self):           
    i = 0
    for star in self.stars: 
      for triplet in star.triplets:
        i += 1
        star = starGC('q' + str(i), triplet[0])
        self.matching.append(star.triplet)

  # Prints M'.
  def showResult(self):
    print("   W      X      Y")
    for match in self.matching:
      print(match)