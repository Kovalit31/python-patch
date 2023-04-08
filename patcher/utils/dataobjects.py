class Hunk(object):
  """ Parsed hunk data container (hunk starts with @@ -R +R @@) """

  def __init__(self):
    self.startsrc=None #: line count starts with 1
    self.linessrc=None
    self.starttgt=None
    self.linestgt=None
    self.invalid=False
    self.desc=''
    self.text=[]

#  def apply(self, estream):
#    """ write hunk data into enumerable stream
#        return strings one by one until hunk is
#        over
#
#        enumerable stream are tuples (lineno, line)
#        where lineno starts with 0
#    """
#    pass


class Patch(object):
  """ Patch for a single file.
      If used as an iterable, returns hunks.
  """
  def __init__(self):
    self.source = None 
    self.target = None
    self.hunks = []
    self.hunkends = []
    self.header = []

    self.type = None

  def __iter__(self):
    for h in self.hunks:
      yield h