class Progression:
    """Iterator producing a generic progression.add()
    
    Default iterator produces the whole numbers 0,1,2...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression"""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        
        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the 
        end of a finite progression
        """