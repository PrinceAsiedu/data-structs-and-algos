from msilib import sequence
from progression import Progression


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        
        increment - the fixed constant to add to each term (default 1)
        start     - the first term of the progression (default 0)
        """

        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment
    

if __name__ == '__main__':
    print('Arithmetic progression with increment 3:')
    ArithmeticProgression(3).print_progression(10)

    print('Arithmetic progression with increment 3 and start 5:')
    ArithmeticProgression(3, 5).print_progression(10)
