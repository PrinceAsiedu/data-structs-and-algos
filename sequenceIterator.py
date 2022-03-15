class SequenceIterator:
    """An iterator for any Python sequence types."""

    def __init__(self, sequence):
        self._seq = sequence  # Keep a reference to the underlying data
        self._k = -1          # will increment to 0 on first call to next

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1 
        if self._k < len(self._seq):
            return (self._seq[self._k])  # return the data element
        else:
            # there are no more elements in the sequence
            raise StopIteration('Iteration has reached end of sequence or has stopped for some reason.') 

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self


if __name__ == '__main__':
    from time import sleep
    names = ['abena', 'ben', 'clifford', 'daniel', 'emma']
    iterator = SequenceIterator(names)
    for i in range(len(names)):
        a = next(iterator)
        print(a)
        # sleep(4) here to demonstrate the coolness of an iterator