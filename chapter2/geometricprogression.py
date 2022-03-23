from progression import Progression


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression. 
        
        base    - the fixed constant multiplied to each term (default 2)
        start   - the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base
    

if __name__ == '__main__':
    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 4:')
    GeometricProgression(4).print_progression(10)
