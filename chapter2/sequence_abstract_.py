from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
    
    @abstractmethod
    def __getitem__(self):
        """Return the element at index j of the sequence."""
    
    def __contains__(self, val):
        """Return True if val can be found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:      # found a match
                return True
        return False
    
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:      # check for leftmost match
                return j
        raise ValueError('value not in sequence') # raise error if no match is found
    
    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


class MySequence(Sequence):

    def __init__(self, elements=None):
        self._elements = elements

    def __len__(self):
        k = 0
        for i in self._elements:
            k+=1
        return k

    def __getitem__(self, val):
        if val in self._elements:
            return val
        else: return False