class starTSFO:
  # name: string that identifies the star
  # index: index from star array
  # nClauses: number of clauses in the reduction
  def __init__ (self, name, index, nClauses):
    self.name = name
    self.index = index
    self.internals = []           # [ai1, ai2...]
    self.externals = []           # [bi1, bi2...]
    self.triplets = []            # [[bi1, ai1, ai2], [bi2, ai2, ai3], [bi3, ai3, a4], [bi4, ai4, ai5], [bi5, ai5, ai6], [bi6, ai6, ai1]]
    self.nClauses = nClauses
    self.truthSetting()
    
    
  # Truth Setting: Creating the star points
  def truthSetting (self):
    for i in range (1, self.nClauses * 2 + 1):
      self.externals.append('b' + str(self.index) + str(i))
      self.internals.append('a' + str(self.index) + str(i))
      self.triplets.append(['b' + str(self.index) + str(i), 'a' + str(self.index) + str(i), 'a' + str(self.index) + (str(i+1) if (i != self.nClauses * 2) else '1')]) 


  # Fan out: Chooses certain triplets acording to the assigned boolean.
  def fanOut(self, assigned):
    result = []
    if (not assigned):
      for i in range(self.nClauses-1, -1, -1):
        result.append(self.triplets[i*2+1])
        del(self.triplets[i*2+1])
    else:
      for i in range(self.nClauses-1, -1, -1):
        result.append(self.triplets[i*2])
        del(self.triplets[i*2])
    return result

