# test_melodyomen.py
"""
Tests for MelodyOmen module.
"""

import unittest
from melodyomen import MelodyOmen

class TestMelodyOmen(unittest.TestCase):
    """Test cases for MelodyOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MelodyOmen()
        self.assertIsInstance(instance, MelodyOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MelodyOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
