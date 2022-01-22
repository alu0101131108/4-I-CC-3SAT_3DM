from clause import clause

class starST:

  def __init__(self, name, clause, stars):
    self.name = name     # c1
    self.triplet = []    # [c1, c1', b11]
    self.valid = self.satisfactionTesting(clause, stars)
  
  def satisfactionTesting(self, clause, stars):
    for varIndex in clause.indexes:
      # print("varindex: " + str(varIndex))
      # print("stars: " + str(len(stars)))
      # print("clause variables: " + str(len(clause.variables)))
      currentStar = stars[varIndex - 1]
      for triplet in currentStar.triplets:
        b = triplet[0]
        isPair = int(b[-1]) % 2 == 0
        clauseVarIndex = clause.indexes.index(varIndex)

        if clause.variables[clauseVarIndex] and isPair:
          self.triplet = [b, self.name, self.name + '\'']
          del(currentStar.triplets[varIndex - 1])
          return True

        if not clause.variables[clauseVarIndex] and not isPair:
          self.triplet = [b, self.name, self.name + '\'']
          del(currentStar.triplets[varIndex - 1])
          return True
      
    return False


      
